import os
from datetime import datetime

import pandas as pd
import numpy as np
from sklearn import tree

import common_export_csv
import common_logger    

class Table_Analytics_Hensu:

    # 持ち回りの変数
    MYPJ_PATH = os.path.dirname(os.path.abspath(__file__))
    DATA_SETS_PATH  = os.path.join(MYPJ_PATH, 'datasets')
    CALC_FOLDER_PATH = ''
    ANALYTICS_RESULT_FOLDER_PATH = ''
    # PJ固有の持ち回りDataFrame
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


    # 分析結果の格納（中身は未作成）
    def __aynalytics_result_put__(self)-> None:
        train_csv.to_csv(os.path.join(Table_Analytics_Hensu.ANALYTICS_RESULT_FOLDER_PATH,'result_01.csv'))

    # 読込処理
    def __read_csv__(self,file_name,path=Table_Analytics_Hensu.DATA_SETS_PATH) -> None:
        return pd.read_csv(os.path.join(path,file_name))
    

    def __analytics_kesson_table__(self,df)-> None: 
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
    def __read_csvs__(self)-> None:
        Table_Analytics_Hensu.gp_csv = TAF.__read_csv__(file_name='gender_submission.csv')
        Table_Analytics_Hensu.train_csv = TAF.__read_csv__(file_name='train.csv')
        Table_Analytics_Hensu.test_csv = TAF.__read_csv__(file_name='test.csv')    

    # 統計量のチェックと欠損値のチェック
    def __data_checks__(self)-> None:
        # 統計量抽出
        Table_Analytics_Hensu.gp_csv.describe().to_csv( \
            os.path.join(Table_Analytics_Hensu.CALC_FOLDER_PATH,'gp_csv_describe.csv'))
        Table_Analytics_Hensu.train_csv.describe().to_csv( \
            os.path.join(Table_Analytics_Hensu.CALC_FOLDER_PATH,'train_csv_describe.csv'))
        Table_Analytics_Hensu.test_csv.describe().to_csv( \
            os.path.join(Table_Analytics_Hensu.CALC_FOLDER_PATH,'test_csv_describe.csv'))
        self.logs.out_put_Log('統計量の抽出が完了しました。', common_logger.Log_Levels.INFO)
        self.logs.out_put_Log('生成ファイル : gp_csv_describe.csv', common_logger.Log_Levels.INFO)
        self.logs.out_put_Log('生成ファイル : train_csv_describe.csv', common_logger.Log_Levels.INFO)
        self.logs.out_put_Log('生成ファイル : test_csv_describe.csv', common_logger.Log_Levels.INFO)

        # 欠損値確認
        TAF.__analytics_kesson_table__(Table_Analytics_Hensu.gp_csv).to_csv( \
            os.path.join(Table_Analytics_Hensu.CALC_FOLDER_PATH,'gp_csv_kesson.csv'))
        TAF.__analytics_kesson_table__(Table_Analytics_Hensu.train_csv).to_csv( \
            os.path.join(Table_Analytics_Hensu.CALC_FOLDER_PATH,'train_csv_kesson.csv'))
        TAF.__analytics_kesson_table__(Table_Analytics_Hensu.test_csv).to_csv( \
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

    # 補正（欠損値の保管・文字列データの数値化
    def __data_complement__(self)-> None:


TAF = Table_Analytics_Func()
TAF.__read_csvs__()    
TAF.__data_checks__()




# # 使わない列のゴミ列削除
# train_csv = train_csv.drop(columns='Name')
# # test_csv = test_csv.drop(columns='Name')

# # 前処理（欠損値の補完）
# train_csv['Embarked'].fillna('S')
# train_csv['Embarked'].fillna(train_csv['Age'].median())
# test_csv['Embarked'].fillna('S')
# test_csv['Embarked'].fillna(test_csv['Age'].median())

# # 前処理（文字列→数値変換）
# train_csv[train_csv['Sex']=='female'] = 0
# train_csv[train_csv['Sex']=='male'] = 1
# train_csv[train_csv['Embarked']=='S'] = 0
# train_csv[train_csv['Embarked']=='C'] = 1
# train_csv[train_csv['Embarked']=='Q'] = 2
# test_csv[test_csv['Sex']=='female'] = 0
# test_csv[test_csv['Sex']=='male'] = 1
# test_csv[test_csv['Embarked']=='S'] = 0
# test_csv[test_csv['Embarked']=='C'] = 1
# test_csv[test_csv['Embarked']=='Q'] = 2


# # 補完後の欠損値確認
# TAF.__analytics_kesson_table__(train_csv).to_csv(os.path.join(Table_Analytics_Hensu.CALC_FOLDER_PATH,'train_csv_kesson_hokan.csv'))
# TAF.__analytics_kesson_table__(test_csv).to_csv(os.path.join(Table_Analytics_Hensu.CALC_FOLDER_PATH,'test_csv_kesson_hokan.csv'))

# # print(train_csv.head(3))
# # print(test_csv.head(3))
# # print(gp_csv.describe())
# # print(train_csv.describe())

# # print(test_csv['Ticket'].isnull().sum())
# # print(len(test_csv['Ticket'].unique()))
# # print(test_csv.columns.to_list())

# # tmp = set(list[test_csv.columns.to_list(),gp_csv.columns.to_list()])
# # print(tmp==test_csv.columns.to_list())
# # train_dataの概観
# # print(train_csv.columns.to_list())

# # # test_dataの概観
# # print(test_csv.columns.to_list())

# # common_export_csv.export_csv_datasets(gp_csv.head(1), \
# #                                       os.path.join(Table_Analytics_Hensu.CALC_FOLDER_PATH,'datasets_01.csv'))



# # gp_csv.to_csv(os.path.join(Table_Analytics_Hensu.CALC_FOLDER_PATH,'datasets_02.csv'))
# # print(train_csv.head(2))
# # print(Table_Analytics_Hensu.DATA_SETS_PATH)


# gender_submission.csvの概観
# print(gp_csv['Survived'].unique())
# print(gp_csv.count())
# print(gp_csv[gp_csv['Survived']==0].count())
# print(gp_csv[gp_csv['Survived']==1].count())
