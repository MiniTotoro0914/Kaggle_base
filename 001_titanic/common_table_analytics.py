import os
from datetime import datetime

import pandas as pd
import numpy as np
from sklearn import tree

import common_export_csv
import common_logger
import decision_tree    

class Table_Analytics_Hensu:

    # 持ち回りの変数
    MYPJ_PATH = os.path.dirname(os.path.abspath(__file__))
    DATA_SETS_PATH  = os.path.join(MYPJ_PATH, 'datasets')
    CALC_FOLDER_PATH = ''
    ANALYTICS_RESULT_FOLDER_PATH = ''
    # PJ固有の持ち回りDataFrame 個別部分
    gp_csv = pd.DataFrame()
    train_csv = pd.DataFrame()
    test_csv = pd.DataFrame()

class Table_Analytics_Func:

    def __init__(self)-> None:
        # ログクラスのインスタンス化（仮）
        self.logs = common_logger.CommonLogger(Table_Analytics_Hensu.MYPJ_PATH,\
                                          str(datetime.now().strftime('%Y-%m-%d')) +'_Table_Analytics.log')

        # 分析ファイル格納用のフォルダを作成
        Table_Analytics_Hensu.CALC_FOLDER_PATH  = os.path.join(Table_Analytics_Hensu.MYPJ_PATH, '02_data_set_analytics')
        if not os.path.exists(Table_Analytics_Hensu.CALC_FOLDER_PATH):
            os.makedirs(Table_Analytics_Hensu.CALC_FOLDER_PATH)
            self.logs.out_put_Log('02_data_set_analyticsフォルダを作成しました。', common_logger.Log_Levels.INFO)
        else:
            self.logs.out_put_Log('ログ格納フォルダは存在したのでスキップします。', common_logger.Log_Levels.INFO)

        Table_Analytics_Hensu.ANALYTICS_RESULT_FOLDER_PATH = os.path.join(Table_Analytics_Hensu.MYPJ_PATH, '11_result')
        if not os.path.exists(Table_Analytics_Hensu.ANALYTICS_RESULT_FOLDER_PATH):
            os.makedirs(Table_Analytics_Hensu.ANALYTICS_RESULT_FOLDER_PATH)
            self.logs.out_put_Log('11_resultフォルダを作成しました。', common_logger.Log_Levels.INFO)
        else:
            self.logs.out_put_Log('分析結果フォルダは存在したのでスキップします。', common_logger.Log_Levels.INFO)


    # 分析結果の格納（中身は未作成）
    def __aynalytics_result_put__(self)-> None:
        train_csv.to_csv(os.path.join(Table_Analytics_Hensu.ANALYTICS_RESULT_FOLDER_PATH,'result_01.csv'))

    # 読込処理
    def __read_csv__(self,file_name,path=Table_Analytics_Hensu.DATA_SETS_PATH) -> None:
        print(os.path.join(path,file_name))
        return pd.read_csv(os.path.join(path,file_name), index_col=None)
    
    def __common_analytics_kesson_table__(self,df)-> None: 
            null_val = df.isnull().sum()
            percent = 100 * df.isnull().sum()/len(df)
            kesson_table = pd.concat([null_val, percent], axis=1)
            kesson_table_ren_columns = kesson_table.rename( \
            columns = {0 : '欠損数', 1 : '%'})
            return kesson_table_ren_columns

    # def __aynalytics_describe__(self,file_path)-> None:
    #     train_csv.to_csv(os.path.join(Table_Analytics_Hensu.ANALYTICS_RESULT_FOLDER_PATH,'result_01.csv'))

    def __chh__tmp__(self,df_tmp:pd.DataFrame)-> None:
        print(len(df_tmp.columns.to_list())) 
        # テーブルデータの検証
        for i in df_tmp.columns.to_list():
            print(i)
        return 'test'

    # 読込処理
    def __call_read_csvs__(self)-> None:
        Table_Analytics_Hensu.gp_csv = TAF.__read_csv__(file_name='gender_submission.csv')
        Table_Analytics_Hensu.train_csv = TAF.__read_csv__(file_name='train.csv')
        Table_Analytics_Hensu.test_csv = TAF.__read_csv__(file_name='test.csv')    

    # 統計量のチェックと欠損値のチェック（一応 個別部分）
    def __call_data_checks__(self,sufix:str='')-> None:
        # 統計量抽出
        Table_Analytics_Hensu.gp_csv.describe().to_csv( \
            os.path.join(Table_Analytics_Hensu.CALC_FOLDER_PATH,f'gp_csv_describe{sufix}.csv'))
        Table_Analytics_Hensu.train_csv.describe().to_csv( \
            os.path.join(Table_Analytics_Hensu.CALC_FOLDER_PATH,f'train_csv_describe{sufix}.csv'))
        Table_Analytics_Hensu.test_csv.describe().to_csv( \
            os.path.join(Table_Analytics_Hensu.CALC_FOLDER_PATH,f'test_csv_describe{sufix}.csv'))
        self.logs.out_put_Log('統計量の抽出が完了しました。', common_logger.Log_Levels.INFO)
        self.logs.out_put_Log('生成ファイル : gp_csv_describe.csv', common_logger.Log_Levels.INFO)
        self.logs.out_put_Log('生成ファイル : train_csv_describe.csv', common_logger.Log_Levels.INFO)
        self.logs.out_put_Log('生成ファイル : test_csv_describe.csv', common_logger.Log_Levels.INFO)

        # 欠損値確認
        TAF.__common_analytics_kesson_table__(Table_Analytics_Hensu.gp_csv).to_csv( \
            os.path.join(Table_Analytics_Hensu.CALC_FOLDER_PATH,'gp_csv_kesson.csv'))
        TAF.__common_analytics_kesson_table__(Table_Analytics_Hensu.train_csv).to_csv( \
            os.path.join(Table_Analytics_Hensu.CALC_FOLDER_PATH,'train_csv_kesson.csv'))
        TAF.__common_analytics_kesson_table__(Table_Analytics_Hensu.test_csv).to_csv( \
            os.path.join(Table_Analytics_Hensu.CALC_FOLDER_PATH,'test_csv_kesson.csv'))
        self.logs.out_put_Log('欠損値の確認が完了しました。', common_logger.Log_Levels.INFO)
        self.logs.out_put_Log('生成ファイル : gp_csv_describe.csv', common_logger.Log_Levels.INFO)
        self.logs.out_put_Log('生成ファイル : train_csv_describe.csv', common_logger.Log_Levels.INFO)
        self.logs.out_put_Log('生成ファイル : test_csv_describe.csv', common_logger.Log_Levels.INFO)

        # testとtrainのカラム一致確認
        correct = set(Table_Analytics_Hensu.gp_csv.columns.to_list() + \
                      Table_Analytics_Hensu.test_csv.columns.to_list()) == \
                          set(Table_Analytics_Hensu.train_csv.columns.to_list()) 
        self.logs.out_put_Log(f'訓練用とテスト用の項目数チェック【{correct}】', common_logger.Log_Levels.INFO)

    # 補正（欠損値の保管・文字列データの数値化）
    def __custom_data_complements__(self)-> None:
        # ゴミデータ削除 - 1
        # 使わない列のゴミ列削除
        Table_Analytics_Hensu.train_csv = Table_Analytics_Hensu.train_csv.drop(columns='Name')
        Table_Analytics_Hensu.test_csv = Table_Analytics_Hensu.test_csv.drop(columns='Name')

        # 前処理 - 1
        # 欠損値の補完
        # Embarked・・・出港地の欠損値をSで補完
        # Age・・・年齢の欠損値を中央値で補完
        Table_Analytics_Hensu.train_csv['Embarked'].fillna('S')
        Table_Analytics_Hensu.train_csv['Embarked'].fillna(\
            Table_Analytics_Hensu.train_csv['Age'].median())
        Table_Analytics_Hensu.test_csv['Embarked'].fillna('S')
        Table_Analytics_Hensu.test_csv['Embarked'].fillna(\
            Table_Analytics_Hensu.test_csv['Age'].median())

        # 前処理 - 2
        # 文字リテラル → 数値 の変換
        # Sex・・・female：1、male：2
        # Embarked・・・S：1、C：2、Q：3
        Table_Analytics_Hensu.train_csv['Sex'][Table_Analytics_Hensu.train_csv['Sex']=='female'] = 1
        Table_Analytics_Hensu.train_csv['Sex'][Table_Analytics_Hensu.train_csv['Sex']=='male'] = 2
        Table_Analytics_Hensu.train_csv['Embarked'][Table_Analytics_Hensu.train_csv['Embarked']=='S'] = 1
        Table_Analytics_Hensu.train_csv['Embarked'][Table_Analytics_Hensu.train_csv['Embarked']=='C'] = 2
        Table_Analytics_Hensu.train_csv['Embarked'][Table_Analytics_Hensu.train_csv['Embarked']=='Q'] = 3
        Table_Analytics_Hensu.test_csv['Sex'][Table_Analytics_Hensu.test_csv['Sex']=='female'] = 1
        Table_Analytics_Hensu.test_csv['Sex'][Table_Analytics_Hensu.test_csv['Sex']=='male'] = 2
        Table_Analytics_Hensu.test_csv['Embarked'][Table_Analytics_Hensu.test_csv['Embarked']=='S'] = 1
        Table_Analytics_Hensu.test_csv['Embarked'][Table_Analytics_Hensu.test_csv['Embarked']=='C'] = 2
        Table_Analytics_Hensu.test_csv['Embarked'][Table_Analytics_Hensu.test_csv['Embarked']=='Q'] = 3
        # Table_Analytics_Hensu.train_csv['Age_Sex']= Table_Analytics_Hensu.train_csv['Age'] * Table_Analytics_Hensu.train_csv['Sex']
        # Table_Analytics_Hensu.test_csv['Age_Sex']= Table_Analytics_Hensu.test_csv['Age'] * Table_Analytics_Hensu.test_csv['Sex']

    # 補正（カスタム項目の生成）
    def __custom_data_complements_column__(self)-> None:
        # 前処理 - 2
        Table_Analytics_Hensu.train_csv['Age_Sex']= Table_Analytics_Hensu.train_csv['Age'] * Table_Analytics_Hensu.train_csv['Sex']
        Table_Analytics_Hensu.test_csv['Age_Sex']= Table_Analytics_Hensu.test_csv['Age'] * Table_Analytics_Hensu.test_csv['Sex']


TAF = Table_Analytics_Func()
TAF.__call_read_csvs__()
TAF.__call_data_checks__()
# 前処理（欠損値の補完）ロジック
TAF.__custom_data_complements__()
# TAF.__custom_data_complements_column__()
TAF.__call_data_checks__(sufix='_After_Complement')

calc_param = ["Pclass", "Sex", "Age", "Fare","SibSp","Parch","Embarked"]
file_name = '01_decision_tree_04.csv'
decision_tree.calc_type_01(Table_Analytics_Hensu.train_csv,Table_Analytics_Hensu.test_csv,\
                   os.path.join(Table_Analytics_Hensu.ANALYTICS_RESULT_FOLDER_PATH,\
                                file_name),calc_param)
