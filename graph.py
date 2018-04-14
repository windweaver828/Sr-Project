import numpy as np
import scipy.stats as stats
import matplotlib.patches as mpatches
from matplotlib import pyplot as plt


def plot(values):
    fig = plt.figure()
    fig.suptitle('Range of Prep Times', fontsize=14, fontweight='bold')
    ax = fig.add_subplot(111)
    ax.set_xlabel('Prep Times')
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    blue_patch = mpatches.Patch(color='blue', label='Prep Times')
    plt.legend(handles=[blue_patch])
    mean = np.mean(values)
    std = np.std(values)
    pdf = stats.norm.pdf(values, mean, std)
    plt.plot(values, pdf)
##    plt.axvline(x = mean-std)
##    plt.axvline(x = mean+std)
    plt.show()


