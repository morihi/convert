# -*- coding: utf-8 -*-
import pandas as pd

'''

CSVを読み込んで、生徒データの正誤判断（列数＝行数）、DataFrameで返す

'''


def judge(student_name) :

    std_num = len(student_name)

    '''
    CSV読み込み
    '''

    df_list = []
    for a in student_name:
        df_list.append(pd.read_csv("../csv/"+a,index_col=0))

    '''
    CSVの形式を確認
    '''

    index_length = len(df_list[0])
    columns_length = len(df_list[0].columns)
    for i in df_list:
        if ( index_length != columns_length or index_length != len(i) or columns_length != len(i.columns)):
            print("生徒データに誤りがあります")
            sys.exit()

    return df_list
