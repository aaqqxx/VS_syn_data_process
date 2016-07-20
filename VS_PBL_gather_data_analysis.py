# coding:utf-8
# !/usr/env/bin/python

__author__ = 'aaqqxx'

"""
用来分析PBL控制VS时使用光幕传感器同步采集的数据。
"""

import numpy as np
import matplotlib.pyplot as plt


class Gather_Setting:
    def __init__(self, gath_setting_file=""):
        self.Enable = 0
        self.Addr = range(0, 128)
        self.Addr[0] = "Sys.ServoCount.a"
        self.Addr[1] = "Sys.M[8192].a"
        self.Addr[2] = "Motor[1].FeWarn.a"
        self.Addr[3] = "Motor[1].ActPos.a"
        self.Addr[4] = "Motor[1].DesPos.a"
        self.Addr[5] = "Motor[1].iqcmd.a"
        self.Addr[6] = "Motor[3].ActPos.a"
        self.Addr[7] = "Motor[3].DesPos.a"
        self.Addr[8] = "Motor[3].iqcmd.a"
        self.Items = 9
        self.Period = 10
        self.Enable = 1
        self.Enable = 0
        self.MaxSamples = 1000
        self.ServoPeriod = 0.442673749446657994

    pass


def get_vel(pos, time_dur=0.4427):
    vel = []
    for index, each in enumerate(pos):
        if index < len(pos) - 1:
            vel.append((pos[index + 1] - pos[index]) / time_dur)
    return np.array(vel)
    pass


def get_CCD_pos(CCD_volt, min_volt=-10, max_volt=10, min_pos=0, max_pos=600000):
    """

    :param CCD_volt:
    :param min_volt:
    :param max_volt:
    :param min_pos:
    :param max_pos:单位0.1um 
    :return:
    """

    CCD_pos = (CCD_volt - min_volt) / (max_volt - min_volt) * (max_pos - min_pos)
    return CCD_pos
    pass


def get_gather_data(gather_data_file):
    data_all = np.loadtxt(gather_data_file, unpack=True, skiprows=1)
    gather_setting = Gather_Setting()
    time = data_all[0]
    CCD_volt = data_all[1] * 10 / 32768
    CCD_pos = -get_CCD_pos(CCD_volt)
    CCD_pos = CCD_pos - CCD_pos[0]

    PBL_pos = data_all[2]
    PBL_pos = PBL_pos - PBL_pos[0]
    PBL_vel = get_vel(PBL_pos)
    des_pos = data_all[3] - data_all[3][0]

    ccd = CCD_pos - CCD_pos[1]
    pbl = des_pos - des_pos[0]

    CCD_fe = pbl - ccd

    # PLB_vel = data_all[2]
    # plt.plot(CCD_p    os,label="CCD_pos")
    vel = get_vel(CCD_pos)
    print pbl.max(), ccd.max()
    ax1 = plt.axes()
    ax2 = plt.twinx(ax1)
    # ax1.plot(-vel , label="CCD_vel")
    # ax1.plot(PBL_vel, label="BPL_vel")
    # ax2.plot(CCD_fe, label="CCD_fe",color="r")

    ax1.plot(PBL_pos, label="PBL_pos")
    ax1.plot(CCD_pos, label="CCD_pos")
    FE = PBL_pos - CCD_pos
    ax2.plot(FE - FE[0])

    plt.legend()
    plt.show()
    pass


def main():
    get_gather_data("gather_data/#3motor_CCD1.gat")


if __name__ == '__main__':
    main()
    print get_CCD_pos(-3.863, max_pos=60)
    pass
