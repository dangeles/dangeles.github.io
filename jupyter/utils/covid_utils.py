import os
import scipy
import datetime as dt
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rc


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


def scatter_plot_per_state(df):
    fig, ax = plt.subplots(figsize=(10, 10))

    for n, g in df[df.deaths > 1].groupby('state'):
        if len(g) < 5:
            continue
        if n in ['Washington', 'New York', 'Massachusetts', 'New Jersey']:
            plt.scatter(g.cases, g.deaths, label=n, zorder=np.inf, s=100)
        else:
            plt.scatter(g.cases, g.deaths, color='black', alpha=0.3)


def plot_cases_vs_deaths(df):

    x = np.linspace(10**0, 10**6, 10)

    scatter_plot_per_state(df)
    plt.plot(x, x / 10,
             label='10\% mortality rate', color='black', ls='-')
    plt.plot(x, x / 100,
             label='1\% mortality rate', color='black', ls='--')

    plt.xlim(10**1, 10**6)
    plt.ylim(10**0, 5 * 10**4)
    plt.legend(loc=(1, .3))
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Cases')
    plt.ylabel('Deaths')


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
            plt.scatter(f(t[0]), f(t[1]), s=filt_vars.min() * 50 / filt_vars[i])
        else:
            if first:
                plt.scatter(f(t[0]), f(t[1]),
                            s=filt_vars.min() * 50 / filt_vars[i],
                            color='black', zorder=0, label='Otro')
            else:
                plt.scatter(f(t[0]), f(t[1]),
                            s=filt_vars.min() * 50 / filt_vars[i],
                            color='black', zorder=0, label='_Otro')
            first = False
