# %%
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# %%

class CurrentWeatherData():
    def __init__(self):
    
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.url = 'https://www.wunderground.com/weather/tr/zeytinburnu'

        self.driver.get(self.url)

        self.temp = self.driver.find_element(By.XPATH,'/html/body/app-root/app-today/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[1]/div[1]/lib-city-current-conditions/div/div[2]/div/div/div[2]/lib-display-unit/span/span[1]')  

        self.temp_value = int((int(self.temp.text) - 32) * 5/9)


        self.wind = self.driver.find_element(By.XPATH, '//*[@id="inner-content"]/div[3]/div[1]/div/div[1]/div[1]/lib-city-current-conditions/div/div[3]/div/div[2]/p/strong/lib-display-unit/span/span[1]')
        
        self.wind_value = int(self.wind.text)


    # %%
        self.dewp = self.driver.find_element(By.XPATH, '//*[@id="inner-content"]/div[3]/div[2]/div/div[1]/div[1]/lib-additional-conditions/lib-item-box/div/div[2]/div/div[4]/div[2]/lib-display-unit/span/span[1]')

        self.dewp_value = int((int(self.dewp.text) - 32) * 5/9)


    # %%
        self.humadity = self.driver.find_element(By.XPATH, '//*[@id="inner-content"]/div[3]/div[2]/div/div[1]/div[1]/lib-additional-conditions/lib-item-box/div/div[2]/div/div[5]/div[2]/lib-display-unit/span/span[1]')

        self.humadity_value = int(self.humadity.text)



