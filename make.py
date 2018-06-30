# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

'''

生徒ファイル名、パーセントを引数に持ち、
指定されたパーセントで正解データを作成し、teacher_dataに出力する

'''

def make(student_name,df_list,per) :

    std_num = len(student_name)
    df_num = len(df_list[0].columns)
    d = []
    f = []

    '''
    print(student_name)
    print(df_list[0].values[2])
    print(per)
    '''

    for j in range(df_num):
        for k in range(std_num):
            d.append(df_list[k].values[j])
        f.append(np.sum(d,axis = 0))
        d = []

    csv_list = []
    for a in range(0,df_num):
        csv_list.append([])

    for i in range(df_num):
        for j in range(df_num):
            if f[i][j] > std_num * (per / 100):
                csv_list[i].append(1)
            else :
                csv_list[i].append(0)

    '''
    ヘッダー用リスト作成
    '''
    list_columns=[]
    for i in range(df_num):
        list_columns.append("C"+str(i))

    '''
    作成するCSVのインデックス用リスト
    '''
    list_index = []
    for i in range(df_num):
        list_index.append("L"+str(i))

    df = pd.DataFrame(
    csv_list,
    columns = list_columns,
    index   = list_index
    )
    print(df)

    df.to_csv('./teacher_data/teacher.csv',encoding="shift-jis")
