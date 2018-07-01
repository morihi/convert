#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

"""

CSVを読み込んで、生徒データの正誤判断（列数＝行数）、DataFrameで返す

"""


def judge(df_list) :

    """
    生徒のデータの形式が揃っており、かつn*n型になっているか判断

    Parameters
    ----------
    df_list : list of DataFrame
        生徒の結線データを格納したリスト

    Returns
    -------
    True or False : boolean
        生徒データ形式の正誤
    """

    index_length = len(df_list[0])
    columns_length = len(df_list[0].columns)
    for i in df_list:
        if ( index_length != columns_length or index_length != len(i) or columns_length != len(i.columns)):
            print("生徒データに誤りがあります")
            return False
        else:
            return True

def judge_tec(dft,df_list) :

    """
    教師データがn*n型になっており、生徒データと列数、行数があっているか判断

    Parameters
    ----------
    dft : DaraFrame
        教師データのDataFrame
    df_list : list of DataFrame
        生徒の結線データを格納したリスト

    Returns
    -------
    True or False : boolean
        教師データ形式の正誤
    """

    if ( len(dft) != len(dft.columns) and (len(df_list[0]) == len(dft))):
        print("教師データに誤りがあります")
        return False
    else :
        return True
