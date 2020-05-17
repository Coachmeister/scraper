from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pandas as pd
#import database_connection
#import elephantsql




def scrape():
    option = webdriver.ChromeOptions()
    option.add_argument("-incognito")

    browser = webdriver.Chrome(executable_path="C:\Development\scraper\chromedriver.exe", options=option)

    browser.get("https://ordnet.dk/ddo/ordbog?aselect=%C3%A5rv%C3%A5gen&query=0")

    timeout = 20

    try:
        WebDriverWait(browser, timeout).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='definitionBoxTop']")))
    except TimeoutException:
        print("timed out")
        browser.quit()

    text_elements = browser.find_elements_by_xpath("//div[@class='definitionBoxTop']")
    boejninger = browser.find_elements_by_xpath("//div[@id='id-boj']")

    clicker = browser.find_elements_by_class_name("searchResultBox")
    click = [x.text for x in clicker]
    boej = [x.text for x in boejninger]
    text = [x.text for x in text_elements]

    for clicks in click:
        print(clicks.trim())






  #  print(click, "\n")

  #  df = pd.DataFrame({"betydning": [text], "bøjninger": [boej]})
   # df.to_csv("test1")
   # print(df)

if __name__ == '__main__':
    scrape()





