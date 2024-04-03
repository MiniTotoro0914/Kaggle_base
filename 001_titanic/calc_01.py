import os

import pandas as pd
import numpy as np
from sklearn import tree

import common_export_csv
import common_logger    

# # ログの出力
# 
# logs.out_put_Log('test2', common_logger.Log_Levels.CRITICAL)

class Calc_01_HENSU:

    # 持ち回りの変数
    MYPJ_PATH = os.path.dirname(os.path.abspath(__file__))
    DATA_SETS_PATH  = os.path.join(MYPJ_PATH, 'datasets')
    CALC_FOLDER_PATH = ''
    ANALYTICS_RESULT_FOLDER_PATH = ''   

class Calc_01_FUNC:

    def __init__(self)-> None:
        # ログクラスのインスタンス化（仮）
        logs = common_logger.CommonLogger('test.log')

        # 分析ファイル格納用のフォルダを作成
        Calc_01_HENSU.CALC_FOLDER_PATH  = os.path.join(Calc_01_HENSU.MYPJ_PATH, '01_calc')
        if not os.path.exists(Calc_01_HENSU.CALC_FOLDER_PATH):
            os.makedirs(Calc_01_HENSU.CALC_FOLDER_PATH)

        # 結果ファイル格納用のフォルダを作成
        Calc_01_HENSU.ANALYTICS_RESULT_FOLDER_PATH = os.path.join(Calc_01_HENSU.MYPJ_PATH, '11_result')
        if not os.path.exists(Calc_01_HENSU.ANALYTICS_RESULT_FOLDER_PATH):
            os.makedirs(Calc_01_HENSU.ANALYTICS_RESULT_FOLDER_PATH)

    # 分析結果の格納（中身は未作成）
    def __aynalytics_result_put__(self)-> None:
        train_csv.to_csv(os.path.join(Calc_01_HENSU.ANALYTICS_RESULT_FOLDER_PATH,'result_01.csv'))


Calc_01_FUNC.__init__(Calc_01_FUNC)

gp_csv = pd.read_csv(os.path.join(Calc_01_HENSU.DATA_SETS_PATH,'gender_submission.csv'))
train_csv = pd.read_csv(os.path.join(Calc_01_HENSU.DATA_SETS_PATH,'train.csv'))
test_csv = pd.read_csv(os.path.join(Calc_01_HENSU.DATA_SETS_PATH,'test.csv'))

# testとtrainのカラム一致確認
correct = set(gp_csv.columns.to_list() + test_csv.columns.to_list()) == set(train_csv.columns.to_list()) 
print(correct)


# ゴミ列削除
train_csv = train_csv.drop(columns='Name')
# test_csv = test_csv.drop(columns='Name')

# 前処理（欠損値の補完）
train_csv['Embarked'].fillna('S')
train_csv['Embarked'].fillna(train_csv['Age'].median())

# 前処理（文字列→数値変換）
train_csv[train_csv['Sex']=='female'] = 0
train_csv[train_csv['Sex']=='male'] = 1
train_csv[train_csv['Embarked']=='S'] = 0
train_csv[train_csv['Embarked']=='C'] = 1
train_csv[train_csv['Embarked']=='Q'] = 2

# print(train_csv.head(3))
# print(test_csv.head(3))
# print(gp_csv.describe())
print(train_csv.describe())

# print(test_csv['Ticket'].isnull().sum())
# print(len(test_csv['Ticket'].unique()))
# print(test_csv.columns.to_list())

# tmp = set(list[test_csv.columns.to_list(),gp_csv.columns.to_list()])
# print(tmp==test_csv.columns.to_list())
# train_dataの概観
# print(train_csv.columns.to_list())

# # test_dataの概観
# print(test_csv.columns.to_list())

# common_export_csv.export_csv_datasets(gp_csv.head(1), \
#                                       os.path.join(Calc_01_HENSU.CALC_FOLDER_PATH,'datasets_01.csv'))



# gp_csv.to_csv(os.path.join(Calc_01_HENSU.CALC_FOLDER_PATH,'datasets_02.csv'))
# print(train_csv.head(2))
# print(Calc_01_HENSU.DATA_SETS_PATH)


# gender_submission.csvの概観
# print(gp_csv['Survived'].unique())
# print(gp_csv.count())
# print(gp_csv[gp_csv['Survived']==0].count())
# print(gp_csv[gp_csv['Survived']==1].count())
