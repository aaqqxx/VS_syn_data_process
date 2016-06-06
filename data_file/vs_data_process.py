__author__ = 'SIOM'
# coding:utf-8
# !/usr/env/bin python
'''
���ڽ���Ļ�������ɼ������ݺ�PMAC�������ݽ��бȽϣ��õ�����������ƾ��ȡ���ͼ��
'''

import logging
import matplotlib.pyplot as plt
import numpy as np


def CCD_data_process(filename, init_dis=0, start_num=0, data_num=1000, factor=10000):
    '''
    �ù������ڽ�CCD�ɼ���������ת��Ϊcts�����ҽ��н�ȡ���βɼ��������ݡ�
    filename Ϊ�����ļ�����ʽ.txt,�����Կո����,���ݵ�λ��mm��
    pos_offset Ϊδ�˶�ʱ������Ƭ�ĳ�ʼ���롣
    start_num Ϊ��ʼ��ȡ�����ݵ���ʼ��ַ��
    data_num Ϊһ����ȡ���ٸ�����,�������ݳ�����ȫ����ȡ
    factor �ǵ�λת�����ӣ���1mmת��Ϊ0.1um,��Ҫ����10000
    '''
    buff = get_data_from_file(filename)
    buff = buff[start_num:start_num + data_num]
    data = (buff - init_dis) * factor
    return data


def get_data_from_file(filename):
    '''
    ���ڴ�CCD�õ��������ļ��еõ����ݲ�ת��Ϊnp.array�����������
    '''
    f = open(filename)
    buff = f.read()
    f.close()
    buff = buff.split()
    data = np.array(buff, dtype='float')
    print len(data)
    return data


def plot_CMD_CDD_diff(CMD_file_name, CCD_file_name, init_dis, CCD_start_num=0, CMD_start_num=0, factor=10000):
    '''
    ��ȡ����λ�ú�CCDʵ�ʲ��λ�������ļ�������CCD�ļ��е����ݽ��н�ȡ��Ȼ�����߶Աȣ��õ����
    CMD_file_name��CMD�������ļ�
    CCD_file_name��CCD�������ļ�
    init_dis��CCD�ɼ�ʱ�����ڵļ��
    CCD_start_num��CCD�ɼ���������Ч���ݵ���ʼ��ַ����һ�����ݵ��start_numΪ0
    CMD_start_num��PMAC������������Ч���ݵ���ʼ��ַ,��һ�����ݵ��start_numΪ0
    factor��CCD���ݲɼ���λ��PMAC�ĵ�λת�����ӣ���1mmת��0.1umΪ10000.
    '''
    CMD_data = get_data_from_file(CMD_file_name)[CMD_start_num:-1]
    # CMD_data = CCD_data_process(CMD_file_name, init_dis=0, start_num=CMD_start_num, factor=1)
    CCD_data = CCD_data_process(CCD_file_name, init_dis, CCD_start_num, len(CMD_data))
    CCD_line, = plt.plot(CCD_data, label='CCD')
    CMD_line, = plt.plot(CMD_data, label='CMD')
    plt.xlabel(r't/442us')
    plt.ylabel(r'y/cts')
    print CCD_data[-1] - CMD_data[-1]
    print len(CCD_data), len(CMD_data)
    logging.warning("dd")
    par2 = plt.twinx()
    fe_line, = par2.plot(CMD_data - CCD_data, label='fe')
    par2.set_ylabel('following error')
    fe_line.set_color('red')
    plt.legend([CCD_line, CMD_line, fe_line], ["CCD", "CMD", "fe"])
    plt.grid()
    plt.show()
    pass


if __name__ == "__main__":
    # get_data_from_file(r'F:\maoxinfeng\IL_VxWorks\data_files\VS\blade_test\CCD_VME6500_data.txt')
    # for each in range(27,30):
    plot_CMD_CDD_diff(r'middle\#4up300\Y1_ap.txt', r'middle\#4up300\CCD_VME6500_data.txt', 18.120089, 28, 0, 10000)
    # plot_CMD_CDD_diff(r'I:\Work\LG\Slit\Y1_ap.txt', r'I:\Work\LG\Slit\CCD_VME6500_data.txt',0,0,10000)
