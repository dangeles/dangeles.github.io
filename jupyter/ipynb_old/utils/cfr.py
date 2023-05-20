"""
A default python script with all my most used libraries.
python: 3.6.7
Author: David Angeles-Albores
contact: dangeles@mit.edu
"""
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.impute import KNNImputer
from sklearn.neighbors import kneighbors_graph
import leidenalg as la
import igraph as ig

import pywt
from pywt import dwt
from pywt import waverec
from pywt import wavedec
from pywt import upcoef

from matplotlib import rc

rc('text', usetex=True)
rc('text.latex', preamble=r'\usepackage{cmbright}')
rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica']})

rc = {'lines.linewidth': 2,
      'axes.labelsize': 18,
      'axes.titlesize': 18,
      'axes.facecolor': 'DFDFE5'}
sns.set_context('notebook', rc=rc)
sns.set_style("dark")

mpl.rcParams['xtick.labelsize'] = 16
mpl.rcParams['ytick.labelsize'] = 16
mpl.rcParams['legend.fontsize'] = 14


def fetch_data():
    # load into a dataframe:
    pop = pd.read_excel('../data/nst-est2019-01.xlsx', comment='#', header=1)

    # fetch NYT data:
    url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv'
    df = pd.read_csv(url, usecols=[0, 1, 3, 4], parse_dates=['date'], squeeze=True)

    pop.columns = np.append(np.array(['state']), pop.columns[1:].values)
    pop.state = pop.state.str.strip('.')

    # merge dfs:
    df = df.merge(pop, left_on='state', right_on='state')

    # calculate per population numbers:
    df['normedPopCases'] = df.cases/ df[2019] * 10 ** 6
    df['normedPopDeaths'] = df.deaths / df[2019] * 10 ** 6
    return df

def madev(d, axis=None):
    """ Mean absolute deviation of a signal """
    return np.mean(np.absolute(d - np.mean(d, axis)), axis)


def wavelet_denoising(coeff, wavelet='db4', level=1):
    sigma = (1/0.6745) * madev(coeff[-level])
    uthresh = sigma * np.sqrt(2 * np.log(len(coeff[0] * 2)))
    coeff[1:] = (pywt.threshold(i, value=uthresh, mode='hard') for i in coeff[1:])
    return coeff


def wavelet_smooth(df, col='cases', period=1, wavelet='db20', level=2):
    smoothCases = df[col].diff(period)
    smoothCases[smoothCases < 0] = -1
    smoothCases.replace(-1, method='ffill', inplace=True)

    coeffsCases = wavedec(smoothCases.fillna(0), wavelet, level=level)
    coeffsCases = wavelet_denoising(coeffsCases)
    reconsCases = upcoef(part='a', coeffs=coeffsCases[0], wavelet=wavelet, level=level)
    reconsCases[reconsCases < 0] = 0

    error = [((smoothCases - reconsCases[n:len(smoothCases) + n]) ** 2).sum()
               for n in range(len(reconsCases) - len(smoothCases))]
    align = np.argmin(error)

    reconsCases = reconsCases[align:align + len(df)]
    reconsCases = pd.Series(reconsCases, index=df.index)
    return reconsCases


def smooth_active(df, period=1, window=10, **wave_args):
    l = []
    for s, g in df.groupby('state'):
        smoothCases = wavelet_smooth(g, 'normedPopCases', period=period, **wave_args)
        smoothDeaths = wavelet_smooth(g, 'normedPopDeaths', level=3, period=period)

        smoothCFR = smoothDeaths / smoothCases
        smoothCFR[smoothCases == 0] = np.nan
        smoothCFR[smoothDeaths == 0] = 0

        smoothReff = smoothCases.rolling(window=7).sum() / smoothCases.rolling(window=7).sum().shift(7)
        smooth = pd.DataFrame(list(zip(smoothCases.values, smoothDeaths.values,\
                                       smoothCFR.values, smoothReff.values)),
                              index=g.date,
                              columns=['CasesPerPeriod', 'DeathsPerPeriod',
                                       'CFR', 'Reff'])
        smooth['state'] = s
        l += [smooth]

    smooth = pd.concat(l)
    smooth.loc[smooth.index < dt.datetime(2020, 6, 1)].fillna(0, inplace=True)
    return smooth


def pivot_transform_impute(data, values='CasesPerPeriod', transform=np.log1p,
                           drop_thresh=10, n_neighbors=5, p=1):
    mat = data.pivot(columns='state', values=values).dropna(thresh=drop_thresh)
    mat[np.isnan(mat)].loc[mat.index < dt.datetime(2020, 6, 1)] = 0
    mat[mat < 0] = np.nan
    mat = transform(mat)
    mat = pd.DataFrame(KNNImputer(n_neighbors=n_neighbors).fit_transform(mat),
                       columns=mat.columns, index=mat.index)
    return mat


def pca_plot(smooth, values, n_comps=10, plot=True, **kwargs):
    mat = pivot_transform_impute(smooth, values, **kwargs)
    pca = PCA(n_comps)
    coords = pca.fit_transform(StandardScaler().fit_transform(mat))

    if plot == True:
        ncols = np.int(np.ceil(n_comps / 2))
        fig, ax = plt.subplots(ncols=ncols,
                               nrows=2, sharex=True, figsize=(5 * ncols, 10))

        for i in range(n_comps):
            y = (i % ncols)
            x = int((i - y) / ncols)
            ax[x, y].scatter(mat.index, coords[:, i])
            ax[x, y].set_title('PC' + str(i + 1))

        fig.autofmt_xdate(rotation=45)

    return pca


def partition(pca, smooth, resolution=1, n_neighbors=10, p=2):

    mat = pivot_transform_impute(smooth, 'CasesPerPeriod')
    comps = pd.DataFrame(pca.components_, columns=mat.columns)
    knn = kneighbors_graph(comps.T, n_neighbors=n_neighbors, mode='distance', p=2)
    sources, targets = knn.nonzero()
    G = ig.Graph(directed=True)
    G.add_vertices(knn.shape[0])
    edges = list(zip(sources, targets))
    G.add_edges(edges)

    partition = la.find_partition(G, la.RBConfigurationVertexPartition,
                                  resolution_parameter=resolution,
                                  seed = 42)

    groups = pd.Series(partition.membership, index=comps.T.index)
    return groups


def plot_partitions(smooth, values, groups, pivot_kwargs={}, plot_kwargs={}):
    mat = pivot_transform_impute(smooth, values, **pivot_kwargs)
    k = groups.max() + 1
    tidy = lambda x: x.reset_index().melt(id_vars='date',
                                          var_name='state',
                                          value_name=values)

    if k == 1:
        fig, ax = plt.subplots(figsize=(6, 5))
        data = tidy(mat)
        sns.lineplot(x='date', y=values, color='black', alpha=1,
                        ax=ax, data=data)
        ax.plot(mat.index, np.median(mat, axis=1), lw=4, color='red',
                label='Mean Behavior')
        sns.lineplot(x='date', y=values, color='blue', lw=2, ax=ax,
                        data=data[data.state == 'New York'])
        sns.lineplot(x='date', y=values, color='tab:blue', lw=2, ax=ax,
                        data=data[data.state == 'Massachusetts'])
        sns.lineplot(x='date', y=values, color='orange', lw=2, ax=ax,
                            data=data[data.state == 'Florida'])

    else:
        fig, ax = plt.subplots(figsize=(6 * k, 5), ncols=k, sharex=True,
                               sharey=False)
        for g in range(k):
            sub = mat[groups[groups == g].index]
            data = tidy(sub)
            sns.lineplot(x='date', y=values, color='blue', lw=2, ax=ax[g],
                            data=data[data.state == 'New York'])
            sns.lineplot(x='date', y=values, color='tab:blue', lw=2, ax=ax[g],
                            data=data[data.state == 'Massachusetts'])
            sns.lineplot(x='date', y=values, color='red', lw=2, ax=ax[g],
                            data=data[data.state == 'Florida'])
            sns.lineplot(x='date', y=values, color='gray', lw=1, alpha=0.3,
                            ax=ax[g], data=data, units='state',
                            estimator=None)
            # ax[g].plot(sub.index, np.median(sub, axis=1), lw=3, color='red',
            #            label='Mean Behavior')
            ax[g].legend([])
            if g != 0:
                ax[g].set_ylabel('')

    plt.tight_layout()
    fig.autofmt_xdate(rotation=45)
    return fig, ax


def plot_cases(cases):
    fig, ax = plt.subplots(figsize=(14, 5), ncols=2)
    ax[0].scatter(cases.index, cases.CaseSum, color='black')
    ax[0].plot(cases.index, cases.smoothCaseSum, color='red')

    ax[1].scatter(cases.index, cases.DeathSum, color='black')
    ax[1].plot(cases.index, cases.smoothDeathSum, color='red')

    ax[0].set_xlabel('Case Sum')
    ax[1].set_xlabel('Death Sum')
    fig.autofmt_xdate(rotation=45)
