#! /usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import pandas as pd

'''

CSVディレクトリに存在するCSVファイルを自動取得
名前は原則"生徒名.csv"

'''


#生徒のCSV読み込み
def readCSV():

    path = './csv/*.csv'
    files = []
    files = glob.glob(path)
    student_name=[]
    l = len(files)

    if l == 1:      #生徒データ一件のみは弾く
        return 1
    elif len(files) != 0 :
        for i in files :
            a = i.split("/")
            student_name.append(a[(len(a) - 1)])

        return student_name

    else :      #生徒データなし
        return 0





#指定ない場合の教師データのCSV確認
def readTeacher():
    path = './csv/teacher_data/teacher.csv'
    files = []
    files = glob.glob(path)
    return len(files)





#教師データ名を指定された場合のCSV確認
def spec_teacher(teacher) :
    a = teacher.split('.')
    if len(a) == 1:
        path = './csv/teacher_data/'+teacher+'.csv'
        files =[]
        files = glob.glob(path)
        if len(files) != 0:
            b = files[0].split("/")
            return b[len(b)-1]
        else :
            return 0
    else:
        path = './csv/teacher_data/'+teacher
        files =[]
        files = glob.glob(path)
        if len(files) != 0:
            b = files[0].split("/")
            return b[len(b)-1]
        else :
            return 0
