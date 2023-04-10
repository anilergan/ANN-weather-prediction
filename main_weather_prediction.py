from fetching_current_weather_data import CurrentWeatherData
from final_model import ModelTrain
from sklearn.preprocessing import StandardScaler


import numpy as np


current_weather = CurrentWeatherData()

temp = current_weather.temp_value
wind = current_weather.wind_value
dewp = current_weather.dewp_value
hum = current_weather.humadity_value 

lgbm_model = ModelTrain()

new_x = np.array([temp,wind,dewp,hum])
new_X = new_x.reshape(1, -1)
new_X_sc = StandardScaler().fit_transform(new_X)

prediction = lgbm_model.model.predict(new_X_sc)
print('Prediction: ',prediction)