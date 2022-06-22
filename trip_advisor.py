

from selenium import webdriver
#in replit environment, we have to import options for selenium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

TRIP_ADVISOR_URL = 'https://www.tripadvisor.com/Attractions-g189952-Activities-a_allAttractions.true-Iceland.html'



def get_driver():
  #importing webdriver
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  return driver

def get_things_to_do(driver):
  #having driver import the page URL
  driver.get(TRIP_ADVISOR_URL)
  #creating a list of the top 15 things to do
  thingsToDo = driver.find_elements(By.XPATH,".//section[@data-automation='WebPresentation_SingleFlexCardSection']")
  return thingsToDo

def get_top_hotels(driver):
  pass

def parse_thingsToDo(thingsToDo):
  thumbnail_url = thingsToDo.find_element(By.XPATH,'.//div/span/div/article/div[1]/div/div/div/div[1]/a').find_element(By.TAG_NAME,'img').get_attribute('src')
  #print(thumbnail_url) #remove later

  thing_url = thingsToDo.find_element(By.XPATH,'.//div/span/div/article/div[2]/header/div/div/a[1]').get_attribute('href')
  #print(thing_url) #remove later
  thing_name = thingsToDo.find_element(By.XPATH,'.//div/span/div/article/div[2]/header/div/div/a[1]').text
  #print(thing_name) #remove later

  average_rating = thingsToDo.find_element(By.XPATH,'.//div/span/div/article/div[2]/header/div/div/a[2]').find_element(By.TAG_NAME,'svg').get_attribute('aria-label')
  #print(average_rating) #remove later
  total_reviews = thingsToDo.find_element(By.XPATH,'.//div/span/div/article/div[2]/header/div/div/a[2]').find_element(By.TAG_NAME,'span').text
  #print(total_reviews) #delete later

  thing_type = thingsToDo.find_element(By.XPATH,'.//div/span/div/article/div[2]/div[1]/div[1]/div/div/div').text
  #print(thing_type) #delete later

  link_to_user_reviews = thingsToDo.find_element(By.XPATH,'.//div/span/div/article/div[2]/div[1]/div[2]').find_element(By.TAG_NAME,'a').get_attribute('href')
  #print(link_to_user_reviews) #delete later

  return {
    'Thing_to_do': thing_name,
    'Total_Reviews': total_reviews,
    'Average Rating': average_rating[:-8], #removing last few characters to remove "bubbles" word
    'Activity_type': thing_type,
    'URL': thing_url,
    'Thumbnail_URL': thumbnail_url,
    'Link_to_reviews': link_to_user_reviews
  }
  
if __name__ == "__main__":
  print('Creating driver')
  driver = get_driver()

  print('Fetching top things to do')
  thingsToDo = get_things_to_do(driver)

  print('Parsing top 20 things to do')
  top20_things = [parse_thingsToDo(thing) for thing in thingsToDo[:20]]

  print('Save the top things to a CSV')
  things_df = pd.DataFrame(top20_things) #things Pandas table
  print(things_df)

  things_df.to_csv('topAttractions.csv',index=None)