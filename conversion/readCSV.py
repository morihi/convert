#! /usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import pandas as pd

"""

CSVディレクトリに存在するCSVファイルを自動取得
名前は原則"生徒名.csv"
引数として、csvまでの絶対パスを渡す

"""


def get_std_name(path):

    """
    CSVにあるファイルから、*.csvを全て取得する

    Parameters
    ----------
    path : str
        取得するCSVファイルがあるディレクトリまでの絶対パス

    Returns
    -------
    student_name : list of string
        全*.csvのリスト
    """

    path += '/*.csv'
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

        #print(student_name)
        return student_name

    else :      #生徒データなし
        return 0


#指定ない場合の教師データのCSV確認
def readTeacher(path):

    """
    teacher_dataの中にteacher.csvというファイルが存在するか判断する

    Parameters
    ----------
    path : str
        取得するCSVファイルがあるディレクトリまでの絶対パス

    Returns
    -------
    len(files) : int
        ファイルが存在すれば1,なければ0
    """

    path += '/teacher_data/teacher.csv'

    files = []
    files = glob.glob(path)

    return len(files)

#教師データ名を指定された場合のCSV確認
def spec_teacher(path,teacher) :

    """
    teacher_dataの中に引数の名前のファイルが存在するか判断する
    返り値は、存在すればファイル名、なければ0

    Parameters
    ----------
    path : str
        teacher_dataディレクトリまでの絶対パス
    teacher : str
        teacher_dataにある読み込みたいcsvファイル名

    Returns
    -------
    b[len(b)-1] : str
        指定したファイルがあれば、そのファイル名を*.csvという名前で返す
    0 : int
        なければ0を返す
    """

    a = teacher.split('.')
    if len(a) == 1:
        path += '/teacher_data/'+teacher+'.csv'
        files =[]
        files = glob.glob(path)
        if len(files) != 0:
            b = files[0].split("/")
            return b[len(b)-1]
        else :
            return 0
    else:
        path += '/teacher_data/'+teacher
        files =[]
        files = glob.glob(path)
        if len(files) != 0:
            b = files[0].split("/")
            return b[len(b)-1]
        else :
            return 0

def read_std_csv(path,student_name):

    """
    引数で渡されたcsvファイル名のリストをDataFrame型に変換して返す

    Parameters
    ----------
    path : str
        変換したいcsvファイルのあるディレクトリまでの絶対パス
    student_name : list of string
        読み込みたいcsvファイル名

    Returns
    -------
    df_list : list of DaraFrame
        指定されたファイル名のcsvを変換したDaraFrameが格納されたリスト
    """

    df_list = []
    for a in student_name:
        df_list.append(pd.read_csv(path+"/"+a,index_col=0))

    return df_list

def read_tec_csv(path,file_name):

    """
    引数で渡されたcsvファイルをDataFrame型に変換して返す

    Parameters
    ----------
    path : str
        変換したいcsvファイルのあるディレクトリまでの絶対パス
    file_name : str
        teacher_dataにある読み込みたいcsvファイル名

    Returns
    -------
    dft : DataFrame
        指定されたファイル名のcsvを変換したDaraFrame
    """

    dft = pd.read_csv(path+"/teacher_data/"+file_name,index_col=0)

    return dft
