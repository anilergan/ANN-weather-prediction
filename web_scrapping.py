from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import time

database = pd.DataFrame(columns=['Time', 'Temperature','Dew Point','Humidity','Wind','Wind Speed','Wind Gust','Pressure','Precip.''Condition'])

# headless mode
chrome_options = Options()
chrome_options.add_argument('--headless')

# run the browser through headless mode
driver = webdriver.Chrome(options=chrome_options)

def get_table():   
    time.sleep(5)   
    table = driver.find_element(By.XPATH, '//*[@id="inner-content"]/div[2]/div[1]/div[5]/div[1]/div/lib-city-history-observation/div/div[2]/table')
    html_table = table.get_attribute('outerHTML')

    df_list = pd.read_html(html_table)
    df = df_list[0] # ilk tabloyu seçiyoruz
    df = df.dropna()
    return df

base_url = "https://www.wunderground.com/history/daily/tr/istanbul/LTBA/date/"
for years in range(2020,2023):
    for months in range(1,13):
        for days in range (1,29):
            url = base_url+str(years)+"-"+str(months)+"-"+str(days)
            driver.get(url)
            df = get_table()
            database = pd.concat([database,df])
            print(database.tail(1))

