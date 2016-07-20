# coding:utf-8
# !/usr/env/bin/python

__author__ = 'aaqqxx'

"""
用来分析PBL控制VS时使用光幕传感器同步采集的数据。
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib


def main():
    data_all = np.loadtxt("raw_data", unpack=True)
    data0=data_all[0]
    data1=data_all[1]
    ax=plt.axes()
    print dir(ax)
    ax2=ax.twinx()
    # l=[]
    # l1=ax.plot(data0/data0.max(),"r-*",label="CCD")
    # l2=ax2.plot(data1/data1.max(),"b-*",label="PBL")
    zhfont1 = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')
    l1=ax.plot(data0-data0.min(),"r-*",label="#1")
    l2=ax2.plot(data1-data1.min(),"b-*",label="#2")
    ax2.set_ylim(0,40)
    lns = l1+l2
    labs = [l.get_label() for l in lns]
    ax.legend(lns, labs, loc=0)
    plt.title(ur"归一化",fontproperties=zhfont1)
    plt.show()

    pass

if __name__ == '__main__':
    main()
    pass