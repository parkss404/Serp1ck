from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re

my_place = input("지역을 입력하세요 : ")
food_name= input("음식을 입력하세요 : ")

driver = webdriver.Chrome()
driver.get("https://www.yogiyo.co.kr/")

driver.maximize_window()
time.sleep(1)

xpath = '''//*[@id="search"]/div/form/input'''
element = driver.find_element(By.XPATH, xpath)
element.clear()
time.sleep(1)

element.send_keys(my_place)
time.sleep(1)

search_button = '''//*[@id="button_search_address"]/button[2]'''
driver.find_element(By.XPATH, search_button).click()
time.sleep(1)

search_selector = '#search > div > form > ul > li:nth-child(3) > a'
search = driver.find_element(By.CSS_SELECTOR, search_selector)
search.click()
time.sleep(1)

input_box_xpath='''//*[@id="category"]/ul/li[1]/a'''
input_box=driver.find_element(By.XPATH, input_box_xpath)
time.sleep(1)
input_box.click()

send_food_xpath='''//*[@id="category"]/ul/li[15]/form/div/input'''
send_food=driver.find_element(By.XPATH, send_food_xpath)
time.sleep(1)
send_food.send_keys(food_name)

food_button_xpath='''//*[@id="category_search_button"]'''
food_button=driver.find_element(By.XPATH,food_button_xpath)
food_button.click()
time.sleep(1)

html = driver.page_source
html_source = BeautifulSoup(html, 'html.parser')

restaurantName = html_source.find_all("div", class_ = "restaurant-name ng-binding")
restaurantScore = html_source.find_all("span", class_ = "ico-star1 ng-binding") 
restaurantReview = html_source.find_all("span", attrs = {"class":"review_num ng-binding", "ng-show":"restaurant.review_count > 0"})
deliveryTime = html_source.find_all("li", class_ = "delivery-time ng-binding") 
