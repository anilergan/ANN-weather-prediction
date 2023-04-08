# %%
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# %%
import pandas as pd
database = pd.DataFrame(columns=['Time', 'Temperature','Dew Point','Humidity','Wind','Wind Speed','Wind Gust','Pressure','Precip.''Condition'])

# %%
# headless mode
chrome_options = Options()
chrome_options.add_argument('--headless')

# %%
driver = webdriver.Chrome(options=chrome_options)

# %%
import time

start_time = time.time() #calculate how much time data fetching takes

def get_table():
    time.sleep(2.5)   
    table = driver.find_element(By.XPATH, '//*[@id="inner-content"]/div[2]/div[1]/div[5]/div[1]/div/lib-city-history-observation/div/div[2]/table')
    html_table = table.get_attribute('outerHTML')

    df_list = pd.read_html(html_table)
    df = df_list[0] # ilk tabloyu seçiyoruz
    df = df.dropna()
    return df

base_url = "https://www.wunderground.com/history/daily/tr/istanbul/LTBA/date/"

for years in range(2022,2023):
    for months in range(1,13):
        for days in range (1,29):
            url = base_url+str(years)+"-"+str(months)+"-"+str(days)
            print(url) #control
            driver.get(url)
            df = get_table()
            database = pd.concat([database,df], ignore_index=True)
            print(database.tail(3)) #control
            database.to_csv('weather_data_fetched2.3.csv', index=False)
        


end_time = time.time() #calculate how much time data fetching takes

elapsed_time = end_time - start_time

minutes = int(elapsed_time / 60)
seconds = int(elapsed_time % 60)

print(f"Process has taken {minutes} minutes, {seconds} seconds.")

