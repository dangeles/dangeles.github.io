import os
import scipy
import datetime as dt
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rc
from scipy.signal import savgol_filter


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
        Cov[n] = fit[1]
        Tau[n] = tau

        # plot:
        plt.plot(x, g[col], lw=5, **kwargs)
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
        else:
            y = g[ycol]
        if n in ['Washington', 'New York', 'Massachusetts', 'New Jersey']:
            ax.scatter(g[xcol], y, label=n, zorder=np.inf, s=75)
        else:
            ax.scatter(g[xcol], y, color='black', alpha=0.2)


def plot_cases_vs_deaths(df, CFR=False, xcol='cases', ycol='deaths', ax=None):

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
        ax.set_ylim(cfr.min() / 2, 1)
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
    points, names = common_entries(tau_cases, tau_deaths)
    covs, names = common_entries(cov_cases, cov_deaths)

    mean_covs = np.array([np.sqrt(1/2 * (c[0]**2 + c[1]**2)) for c in covs])
    normed_covs = mean_covs / np.max(mean_covs)

    filtered = [points[i] for i, v in enumerate(normed_covs) if v < 0.01]
    filt_names = [names[i] for i, v in enumerate(normed_covs) if v < 0.01]
    filt_vars = normed_covs[normed_covs < 0.01]
    return filtered, filt_names, filt_vars



def plot_params(f, tau_cases, tau_deaths, cov_cases, cov_deaths):
    filtered, filt_names, filt_vars = filter(tau_cases, tau_deaths,
                                             cov_cases, cov_deaths)
    fig, ax = plt.subplots(figsize=(8, 8))

    first = True
    for i, t in enumerate(filtered):
        if (filt_names[i] in
            ['Washington', 'New York', 'Massachusetts', 'New Jersey']):
            plt.scatter(f(t[0]), f(t[1]), s=filt_vars.min() * 50 / filt_vars[i],
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


def plot_smooth(ax, df, cond, norm_func=None, intercept = False, smooth=True,
                gradient=False, col='cases', factor=1):
    color = {'New York': 'red',
             'New Jersey': 'blue',
             'Massachusetts': 'orange',
             'Washington': 'purple',
             'California': 'green'}
    if norm_func is None:
        norm_func = lambda x: x

    if intercept:
        add = df[cond][col].min(),
    else:
        add = 0

    for n, g in df[cond].groupby('state'):
        x = (g.date - g.date.min()) / dt.timedelta(days=1)

        if len(g) < 15:
            continue

        if smooth:
            y = factor * savgol_filter(norm_func(g[col]) + add, 7, 3)
        else:
            y = factor * norm_func(g[col]) + add

        if gradient:
            y = np.gradient(y, x)

        if n not in ['New Jersey', 'New York', 'Massachusetts',
                     'Washington', 'California']:
            ax.plot(x, y, color='black', alpha=0.2)
        else:
            ax.scatter(x, y, label=n, zorder=np.inf, s=50, color=color[n])
            ax.plot(x, y, zorder=np.inf, lw=1, color=color[n])


def plot(ax, df, col1, col2, col3, n1=10, n2=10 ** -6, n3=1, ylab='case',
         gradient=False, factor1=1, factor2=10 ** 6 , factor3=100):
    cond = df[col1] > n1
    plot_smooth(ax[0], df, cond, col=col1, gradient=gradient, factor=factor1)

    cond = df[col2] > n2
    plot_smooth(ax[1], df, cond, col=col2, gradient=gradient, factor=factor2)

    cond = df[col3] > n3
    plot_smooth(ax[2], df, cond, col=col3, gradient=gradient, factor=factor3)

    ax[0].set_xlabel('Days since {1} {0}s'.format(ylab, n1))
    ax[1].set_xlabel('Days since 1 {0} / 1M people'.format(ylab))
    ax[2].set_xlabel('Days since 1 {0} sq. mi / 100 people'.format(ylab))

    ax[0].set_title('{0}s'.format(ylab))
    ax[1].set_title('{0}s per {1:.0e} people'.format(ylab, factor2))
    ax[2].set_title('{0}s per Density'.format(ylab))
    return ax
