

from selenium import webdriver
#in replit environment, we have to import options for selenium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

#visiting Iceland, Paris, Switzerland, and Rome
PLACES_TO_VIST_URLS= ['https://www.tripadvisor.com/Attractions-g189952-Activities-a_allAttractions.true-Iceland.html','https://www.tripadvisor.com/Attractions-g187147-Activities-a_allAttractions.true-Paris_Ile_de_France.html','https://www.tripadvisor.com/Attractions-g188045-Activities-a_allAttractions.true-Switzerland.html','https://www.tripadvisor.com/Attractions-g187791-Activities-a_allAttractions.true-Rome_Lazio.html']
PLACES = ['Iceland', 'Paris', 'Switzerland', 'Rome'] #place names



def get_driver():
  #importing webdriver
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  return driver

def get_things_to_do(driver,URL):
  #having driver import the page URL
  driver.get(URL)
  #creating a list of the top 30 things to do
  thingsToDo = driver.find_elements(By.XPATH,".//section[@data-automation='WebPresentation_SingleFlexCardSection']")
  return thingsToDo


def parse_thingsToDo(thingsToDo,country):
  thumbnail_url = thingsToDo.find_element(By.XPATH,'.//div/span/div/article/div[1]/div/div/div/div[1]/a').find_element(By.TAG_NAME,'img').get_attribute('src')
  
  thing_url = thingsToDo.find_element(By.XPATH,'.//div/span/div/article/div[2]/header/div/div/a[1]').get_attribute('href')
  
  thing_name = thingsToDo.find_element(By.XPATH,'.//div/span/div/article/div[2]/header/div/div/a[1]').text
  

  average_rating = thingsToDo.find_element(By.XPATH,'.//div/span/div/article/div[2]/header/div/div/a[2]').find_element(By.TAG_NAME,'svg').get_attribute('aria-label')
  
  total_reviews = thingsToDo.find_element(By.XPATH,'.//div/span/div/article/div[2]/header/div/div/a[2]').find_element(By.TAG_NAME,'span').text
  

  thing_type = thingsToDo.find_element(By.XPATH,'.//div/span/div/article/div[2]/div[1]/div[1]/div/div/div').text
  

  link_to_user_reviews = thingsToDo.find_element(By.XPATH,'.//div/span/div/article/div[2]/div[1]/div[2]').find_element(By.TAG_NAME,'a').get_attribute('href')
  

  return {
    'Country': country,
    'Thing_to_do': thing_name,
    'Total_Reviews': total_reviews,
    'Average Rating': average_rating[:-8], #removing last few characters to remove "bubbles" word
    'Activity_type': thing_type,
    'URL': thing_url,
    'Thumbnail_URL': thumbnail_url,
    'Link_to_reviews': link_to_user_reviews
  }
  
if __name__ == "__main__":

  i=0 #counter to determine whether we are writing data for first time or appending.
  #this counter will also keep track of place name
  
  for place_URL in PLACES_TO_VIST_URLS: #for loop to loop through each location visited
    print('Creating driver')
    driver = get_driver()
  
    print('Fetching top things to do in {}.'.format(PLACES[i]))
    thingsToDo = get_things_to_do(driver,place_URL)

    print('Parsing top 30 things to do in {}.'.format(PLACES[i]))
    top30_things = [parse_thingsToDo(thing,PLACES[i]) for thing in thingsToDo[:30]]
    

    print('Save the top things to a CSV')
    things_df = pd.DataFrame(top30_things) #things Pandas table
    
    #if statement below determines whether we are writing to CSV file for first time or appending.
    if i==0:
      things_df.to_csv('topAttractions.csv',index=None)
    else:
      things_df.to_csv('topAttractions.csv', mode='a', index=None, header=False)
    i=i+1 #increment counter
  