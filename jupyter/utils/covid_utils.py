import os
import scipy
import datetime as dt
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

from matplotlib import rc
from scipy import stats as st
from scipy.special import logsumexp
from matplotlib.colors import ListedColormap


def growth(t, a, tau, b):
    """Exponential growth function."""
    return a * np.exp(t / tau) + b


# get first dates at which states got their first case
def get_first(df, col, min):
    """Get first dates of events reported"""
    first_dates = []
    for n, g in df.groupby('state'):
        if g[g[col] > min].cases.nunique() > 0:
            first_dates += [g[g[col] > min].date.min()]

    plt.plot(np.arange(0, len(first_dates)),
             np.sort(np.array(first_dates)),
             label='First ' + col)


def plot_time(df, col, min_cases=100, ymin=100, **kwargs):
    """Plot col thru time, and fit an exponential growth curve"""
    Tau = {}
    Cov = {}
    # go through each state:
    for n, g in df[df.cases > min_cases].groupby('state'):
        # continue only for states with non-zero reports:
        g = g[g[col] > 0]
        if len(g) < 6:
            continue
        # standardize time to first report:
        x = (g.date - g.date.min()) / dt.timedelta(days=1)

        # line of best fit:
        fit, covs = scipy.optimize.curve_fit(growth, x, g[col])
        a, tau, b = fit
        Cov[n] = np.diag(np.abs(covs))[1]
        Tau[n] = tau

        # plot:
        plt.plot(x, g[col], lw=3, **kwargs)
        plt.plot(x, growth(x, a, tau, b), ls='--', color='black', lw=1)
    # annotate:
    plt.xlabel('Days since {0} cases'.format(min_cases))
    plt.ylabel(col)
    plt.ylim(ymin, df[col].max() * 2)
    plt.yscale('log')
    return Tau, Cov


def scatter_plot_per_state(df, CFR=False, xcol='cases', ycol='deaths', ax=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=(6, 6))

    for n, g in df[df.deaths >= 1].groupby('state'):
        if len(g) < 5:
            continue
        if CFR:
            y = g[ycol] / g[xcol]
            y = pd.Series(y).rolling(window=5,
                                     win_type='gaussian',
                                     center=True).mean(std=2)

        else:
            y = g[ycol]
            y = pd.Series(y).rolling(window=7,
                                     win_type='gaussian',
                                     center=True).mean(std=2).round()

        if n in ['Washington', 'New York', 'Massachusetts', 'New Jersey']:
            ax.scatter(g[xcol], y, label=n, zorder=np.inf, s=25)
            # ax.plot(g[xcol], y, color='black', alpha=0.2)
        else:
            ax.plot(g[xcol], y, color='black', alpha=0.1)


def plot_cases_vs_deaths(df, CFR=False, xcol='cases', ycol='deaths', ax=None):
    df = df[df.deaths >= 1]

    x = np.linspace(10**0, 10**6, 10)

    if ax is None:
        fig, ax = plt.subplots(figsize=(6, 6))

    scatter_plot_per_state(df, CFR, xcol, ycol, ax=ax)

    if CFR:
        ax.axhline(.1, label='10\% mortality rate', color='black', ls='-')
        ax.axhline(.01, label='1\% mortality rate', color='black', ls='--')
        ax.axhline(.03, label='2\% mortality rate', color='black', ls='-.')
    else:
        ax.plot(x, x / 10,
                 label='10\% mortality rate', color='black', ls='-')
        ax.plot(x, x / 100,
                 label='1\% mortality rate', color='black', ls='--')

    ax.set_xlim(df[df.deaths >= 1][xcol].min() / 2,
                df[df.deaths >= 1][xcol].max() * 2)

    if CFR:
        cfr = df[df.deaths >= 1][ycol] / df[df.deaths >= 1][xcol]
        ax.set_ylim(np.max([10 ** -3, cfr.min()]) / 2, 1)
    else:
        ax.set_ylim(df[df.deaths >= 1][ycol].min() / 2,
                    df[df.deaths >= 1][ycol].max() * 2)


    # plt.legend(loc=(1, .3))
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel('Cases')
    # plt.legend()

    if CFR:
        ax.set_ylabel('Case Fatality Rate')
    else:
        ax.set_ylabel('Deaths')

    return ax


def common_entries(*dcts):
    """Given two dictionaries, find KEY intersection, return list of tuples"""
    tup = []
    names = []
    for i in set(dcts[0]).intersection(*dcts[1:]):
        tup += [tuple(d[i] for d in dcts)]
        names += [i]
    return tup, names


def filter(tau_cases, tau_deaths, cov_cases, cov_deaths):
    """
    This function has an error in the way the covariance error is computed!
    """
    points, names = common_entries(tau_cases, tau_deaths)
    covs, names = common_entries(cov_cases, cov_deaths)
    mean_err = np.array([np.sqrt(1/2 * (c[0] + c[1])) for c in covs])
    normed_err = mean_err / np.max(mean_err)

    filtered = [points[i] for i, v in enumerate(normed_err) if v < 0.01]
    filt_names = [names[i] for i, v in enumerate(normed_err) if v < 0.01]
    filt_vars = normed_err[normed_err < 0.01]
    return filtered, filt_names, filt_vars



def plot_params(f, tau_cases, tau_deaths, cov_cases, cov_deaths):
    filtered, filt_names, filt_vars = filter(tau_cases, tau_deaths,
                                             cov_cases, cov_deaths)
    fig, ax = plt.subplots(figsize=(8, 8))

    first = True
    for i, t in enumerate(filtered):
        if (filt_names[i] in
            ['Washington', 'New York', 'Massachusetts', 'New Jersey']):
            plt.scatter(f(t[0]), f(t[1]), s=filt_vars[i] * 5 / filt_vars.min(),
                        label=filt_names[i])
        else:
            if first:
                plt.scatter(f(t[0]), f(t[1]),
                            s=filt_vars.min() * 50 / filt_vars[i],
                            color='black', zorder=0, label='Other')
            else:
                plt.scatter(f(t[0]), f(t[1]),
                            s=filt_vars.min() * 50 / filt_vars[i],
                            color='black', zorder=0, label='_Other')
            first = False

    plt.legend()


def plot_smooth(ax, df, cond, intercept = False,
                gradient=False, col='cases',
                alpha=0.3, window=8, factor=1):

    if intercept:
        add = df[cond][col].min(),
    else:
        add = 0

    curr = []
    for n, g in df[cond].groupby('state'):
        x = (g.date - g.date.min()) / dt.timedelta(days=1)

        if len(g) < 15:
            continue

        y = factor * g.normedPopDeaths
        y = y.rolling(window=window, win_type='gaussian',
                      center=True).mean(std=2).round()

        y = y.diff()
        curr += [[n, y.dropna().values[-1]]]

    last = pd.DataFrame(curr, columns=['state', 'new_cases'])
    last.sort_values('new_cases', inplace=True)

    fancy = last.state.values[-4:]
    for n, g in df[cond].groupby('state'):
        x = (g.date - g.date.min()) / dt.timedelta(days=1)

        if len(g) < 15:
            continue

        y = factor * g[col]
        if gradient:
            # smooth and remove outliers
            ydiff = y.diff()
            y_smooth = ydiff.rolling(win_type='gaussian',
                                     window=window, center=True).mean(std=10)
            res = ydiff - y_smooth
            zscores = np.abs(res/ res.rolling(window * 2).std())
            ydiff[zscores > 2] = y_smooth[zscores > 2]
            y = ydiff

        y = y.rolling(window=window, win_type='gaussian',
                      center=True).mean(std=2)

        if n not in fancy:
            ax.plot(x, y, color='black', alpha=alpha)
        else:
            # ax.scatter(x, y, label=n, zorder=np.inf, s=35, color=color[n])
            # ax.plot(x, y, zorder=np.inf, lw=1, color=color[n])
            p = ax.scatter(x, y, label=n, zorder=np.inf, s=15)
            ax.plot(x, y, zorder=np.inf, lw=2, color=p.get_facecolor()[0])


def plot(ax, df, col1, col2, n1=10, n2=10 ** -6, ylab='case',
         gradient=False, factor1=1, factor2=10 ** 6,
         alpha=0.3, window=10):
    cond = df[col1] > n1
    plot_smooth(ax[0], df, cond, col=col1, gradient=gradient, factor=factor1,
                alpha=alpha, window=window)

    cond = df[col2] > n2
    plot_smooth(ax[1], df, cond, col=col2, gradient=gradient, factor=factor2,
                alpha=alpha, window=window)

    ax[0].set_xlabel('Days since {1} {0}s'.format(ylab, n1))
    ax[1].set_xlabel('Days since 1 {0} / 1M people'.format(ylab))

    ax[0].set_title('{0}s'.format(ylab))
    ax[1].set_title('{0}s per {1:.0e} people'.format(ylab, factor2))
    return ax


def bayes_prob(t, r, cases, prev, gamma=1/10, p_prev=1):
    """
    Bayes update rule for R0 through time.

    Params:
    -------
    t:  int. used to tell whether this is the first timepoint or not
    r:  float. viral reproductive number
    cases:  int. number of cases at time t
    prev:   int. number of cases at time t-1
    gamma:  float. 1 / serial interval for disease
    p_prev: array. posterior at time t-1

    Output:
    -------
    p:  array. posterior at time t
    """
    l = prev * np.exp(gamma * ( r - 1))
    # probability function:
    if t > 0:
        prior = st.norm(loc=r, scale=0.25).pdf(r[:, None])
        prior /= prior.sum()
    else:
        prior = st.norm(loc=4, scale=.01).pdf(r[:, None])
        prior /= prior.sum()


    p = st.poisson.logpmf(cases, l)
    p = np.exp(p - logsumexp(p)) * p_prev @ prior
    p /= p.sum()

    return p


def r_calc(d, col='newCases', gamma=1/10):
    """
    Find the maximum a posteriori estimate for R_t
    """
    t = 0
    r = np.linspace(.5, 6, 1000)
    maxR = np.repeat(-1., len(d))
    maxp = 0
    prev = 1
    p_prev = 1
    for date, g in d.groupby('date'):
        if np.isnan(g[col].values[0]):
            t += 1
            continue

        p = bayes_prob(t, r, g[col].values[0], prev, gamma, p_prev)
        prev = g[col].unique()[0]

        if np.isnan(p).all():
            maxR[t] = -1
        else:
            p_prev = p
            maxR[t] = r[np.where(p == p.max())]

        t += 1
    return maxR

def plot_rt(states, df, cond, gamma=1/10, figsize=(20, 8)):
    fig, ax = plt.subplots(ncols=len(states), nrows=2, figsize=figsize,
                           sharey='row', sharex='col')

    i = 0
    for n, g in df[cond].groupby('state'):
        if n not in states:
            continue
        gp = g.copy()
        gp['newCases'] = gp.cases.diff().rolling(window=8,
                                                 win_type='gaussian',
                                                 center=True).mean(std=2).round()
        gp['newDeaths'] = gp.deaths.diff().rolling(window=8,
                                                   win_type='gaussian',
                                                   center=True).mean(std=2).round()

        maxR = r_calc(gp, gamma=gamma)
        maxRd = r_calc(gp, col='newDeaths', gamma=gamma)

        x = (gp.date - gp.date.min()) / dt.timedelta(days=1)
        condR = maxR > 0
        condRd = maxRd > 0

        xR = x[condR]
        xRd = x[condRd]
        maxR = maxR[condR]
        maxRd = maxRd[condRd]

        ABOVE = [1,0,0]
        MIDDLE = [1,1,1]
        BELOW = [0,0,0]
        color_mapped = lambda y: np.clip(y, .5, 1.5)-.5
        cmap = ListedColormap(np.r_[
                np.linspace(BELOW,MIDDLE,25),
                np.linspace(MIDDLE,ABOVE,25)
            ])

        if len(states) > 1:
            ax[0, i].scatter(xR, maxR, color=cmap(color_mapped(maxR)))
            ax[1, i].scatter(xRd, maxRd, color=cmap(color_mapped(maxRd)))
            ax[0, i].set_title(n)

        else:
            ax[0].scatter(xR, maxR, color=cmap(color_mapped(maxR)))
            ax[1].scatter(xRd, maxRd, color=cmap(color_mapped(maxRd)))
            ax[0].set_title(n)
        i += 1

    if len(ax) > 1:
        for ai in ax:
            if type(ai) is not np.ndarray:
                break
            for aij in ai:
                aij.axhline(1, color='black', zorder=0, ls='--')

        for ai in ax[0]:
            ai.set_ylim(0, 8)
        for ai in ax[1]:
            ai.set_ylim(0, 5)

    if len(states) > 1:
        ax[0, 0].set_ylabel('$R_t$ based on cases')
        ax[1, 0].set_ylabel('$R_t$ based on deaths')
    else:
        ax[0].set_ylabel('$R_t$ based on cases')
        ax[1].set_ylabel('$R_t$ based on deaths')

    # _ = plt.figtext(.5, .045, 'Days since 1 death', fontsize=25, ha='center')
