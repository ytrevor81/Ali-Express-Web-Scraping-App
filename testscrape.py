
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import requests
from bs4 import BeautifulSoup
import time



product = "posters"
amazon = 'https://www.amazon.com/s?k=tapestries&ref=nb_sb_noss_1'
ali = "https://www.aliexpress.com/wholesale?catId=0&initiative_id=SB_20181225216320&SearchText=weed"

#request = requests.get(amazon)

chromepath = "C://Users/User/Desktop/chromedriver/chromedriver.exe"
driver = webdriver.Chrome(chromepath)
#driver.set_window_position(-10000,0)
driver.get(ali)

WebDriverWait(driver, 80).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"alibaba-login-box")))
WebDriverWait(driver, 30)
driver.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys("deanyoung800@gmail.com")
WebDriverWait(driver, 70)
driver.find_element_by_id("fm-login-password").send_keys("Cosmos000")
WebDriverWait(driver, 20)
driver.find_element_by_xpath('//*[@id="login-form"]/div[5]/button').click()

WebDriverWait(driver, 40)
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="search-key"]')))
y = 1000
for timer in range(0,50):
    driver.execute_script("window.scrollTo(0, "+str(y)+")")
    y += 1000
    time.sleep(1)

#WebDriverWait(driver, 100000)
html = driver.page_source
soup = BeautifulSoup(html, 'lxml')
WebDriverWait(driver, 200)



driver.close()
string1 = []
string2 = []
string3 = []
string4 = []
product_titles = soup.find_all('a', {'class':"item-title"})
product_prices = soup.find_all('span', {'class':"price-current"})
product_ratings = soup.find_all('span', {'class':"rating-value"})
products_sold = soup.find_all('a', {'class':"sale-value-link"})

titles = [x.get_text() for x in product_titles]
prices = [x.get_text() for x in product_prices]
ratings = [x.get_text() for x in product_ratings]
sold = [x.get_text() for x in products_sold]

print(titles, len(titles))
print(prices, len(prices))
print(ratings, len(ratings))
print(sold, len(sold))




#if yeah == None:
#    print("you got BLOCKED")
#else:
#    for y in yeah:
#       print(y.encode('utf-8'))
#       print(y.text)
