from sklearn import tree
import pandas as pd
import numpy as np

import common_logger

def calc_type_01(df_train:pd.DataFrame,df_test:pd.DataFrame,file_path:str,param:list[str])-> pd.DataFrame:
    # 「train」の目的変数と説明変数の値を取得
    target = df_train["Survived"].values
    #tmp = ["Pclass", "Sex", "Age", "Fare","SibSp","Parch","Embarked"]
    # features_one = df_train[["Pclass", "Age_Sex", "Fare","SibSp","Parch","Embarked"]].values

    features_one = df_train[param].values
    # features_one = df_train[["Pclass", "Sex", "Age", "Fare"]].values

    # 決定木の作成
    my_tree_one = tree.DecisionTreeClassifier()
    my_tree_one = my_tree_one.fit(features_one, target)
    
    # 「test」の説明変数の値を取得
    # test_features = df_test[["Pclass", "Age_Sex", "Fare","SibSp","Parch","Embarked"]].values
    test_features = df_test[param].values
    # test_features = df_test[["Pclass", "Sex", "Age", "Fare"]].values    

    # 「test」の説明変数を使って「my_tree_one」のモデルで予測
    my_prediction = my_tree_one.predict(test_features)
    # PassengerIdを取得
    PassengerId = np.array(df_test["PassengerId"]).astype(int)
    # my_prediction(予測データ）とPassengerIdをデータフレームへ落とし込む
    my_solution = pd.DataFrame(my_prediction, PassengerId, columns = ["Survived"])
    # print(pd.DataFrame(my_prediction, PassengerId, columns = ["Survived"]))
    # my_tree_one.csvとして書き出し
    my_solution.to_csv(file_path, index_label = ["PassengerId"])
    # return my_prediction
