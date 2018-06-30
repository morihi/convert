# -*- coding: utf-8 -*-

'''

生徒ファイル名、パーセントを引数に持ち、
指定されたパーセントで正解データを作成し、teacher_dataに出力する

'''

def make(student_name,per) :

    std_num = len(student_name)

    '''
    CSV読み込み
    '''

    df_list = []
    for a in student_name:
        df_list.append(pd.read_csv("csv/"+a,index_col=0))

    
