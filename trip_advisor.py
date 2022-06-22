

from selenium import webdriver
#in replit environment, we have to import options for selenium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

TRIP_ADVISOR_URL = 'https://www.tripadvisor.com/Attractions-g189952-Activities-a_allAttractions.true-Iceland.html'




#importing webdriver
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)

#having driver import the page URL
driver.get(TRIP_ADVISOR_URL)




#creating a list of the top 30 things to do
thingsToDo_cards = driver.find_elements(By.XPATH,".//section[@data-automation='WebPresentation_SingleFlexCardSection']")


for i in range(5):
  thumbnail_url = thingsToDo_cards[i].find_element(By.XPATH,'.//div/span/div/article/div[1]/div/div/div/div[1]/a').find_element(By.TAG_NAME,'img').get_attribute('src')
  print(thumbnail_url) #remove later

  thing_url = thingsToDo_cards[i].find_element(By.XPATH,'.//div/span/div/article/div[2]/header/div/div/a[1]').get_attribute('href')
  print(thing_url) #remove later
  thing_name = thingsToDo_cards[i].find_element(By.XPATH,'.//div/span/div/article/div[2]/header/div/div/a[1]').text
  print(thing_name) #remove later

  average_rating = thingsToDo_cards[i].find_element(By.XPATH,'.//div/span/div/article/div[2]/header/div/div/a[2]').find_element(By.TAG_NAME,'svg').get_attribute('aria-label')
  print(average_rating) #remove later
  total_reviews = thingsToDo_cards[i].find_element(By.XPATH,'.//div/span/div/article/div[2]/header/div/div/a[2]').find_element(By.TAG_NAME,'span').text
  print(total_reviews) #delete later

  thing_type = thingsToDo_cards[i].find_element(By.XPATH,'.//div/span/div/article/div[2]/div[1]/div[1]/div/div/div').text
  print(thing_type) #delete later

  link_to_user_reviews = thingsToDo_cards[i].find_element(By.XPATH,'.//div/span/div/article/div[2]/div[1]/div[2]').find_element(By.TAG_NAME,'a').get_attribute('href')
  print(link_to_user_reviews)
  
  





