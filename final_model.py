import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import StratifiedKFold, cross_val_score
from lightgbm import LGBMClassifier


class ModelTrain():

    def __init__(self):
        self.df = pd.read_csv('final_weather_data.csv')

        self.x = self.df.iloc[:,0:4].values
        self.y = self.df.iloc[:,4:].values

        self.sc = StandardScaler()
        self.X = self.sc.fit_transform(self.x)

        self.Y = np.argmax(self.y, axis = 1)

        self.model = self.trainModel(self.X, self.Y)
    

    def trainModel(self, x, y):

        self.skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=23)
        self.lgbm = LGBMClassifier()

        self.scores = cross_val_score(self.lgbm, x,y, cv = self.skf)
        print('Accuracy: ', np.mean(self.scores))

        self.lgbm.fit(x,y)
        return self.lgbm