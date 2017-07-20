# -*- coding: utf-8 -*-
"""
Created on Fri May 26 09:06:07 2017

@author: Lewys.Brace
"""
"""
A bar plot with errorbars and height labels on individual bars
"""
import numpy as np
import matplotlib.pyplot as plt

N = 1
major = (21)
minor = (13)
section = (2)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, major, width, color='cornflowerblue')
rects2 = ax.bar(ind + width, minor, width, color='darkslateblue')
rects3 = ax.bar(ind + width+width, section, width, color='dodgerblue')

# add some text for labels, title and axes ticks
ax.set_ylabel('Number of Errors')
ax.set_title('Breakdown of Sampling Errors for ED16')
ax.set_xticks(ind + width / 2)
#ax.set_xticklabels(('Major Errors', 'Minor Errors', 'Historical Errors', 'Section 251 Breaches'))
ax.set_xlabel('Type of Error')

ax.legend((rects1[0], rects2[0], rects3[0]), ('Major Errors', 'Minor Errors', 'Section 251 Breaches'))


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)


plt.show()