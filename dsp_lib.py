#!/usr/bin/python
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


def plot_freq_response(b, a):
    omega, H = signal.freqz(b, a)
    f = omega / (2*np.pi)
    fig, axes = plt.subplots(2, 1, sharex=True)
    axes[0].plot(f, np.abs(H))
    axes[0].set_ylabel("Magnitude response")

    axes[1].plot(f, np.angle(H))
    axes[1].set_ylabel("Phase response")
    axes[1].set_xlabel("Discrete time frequency [cycles / sample]")

def plot_signal_spectrum(sig, ax=None):
    if ax is None:
        _, ax = plt.subplots()

    X = np.fft.fft(sig)
    f = np.linspace(0, 1, len(X)+1)[:-1]
    pos_inds = f < 0.5
    ax.plot(f[pos_inds], np.abs(X)[pos_inds])
    ax.set_xlabel("Discrete time frequency [cycles / sample]")
    ax.set_ylabel("DFT magnitude [a.u.]")
