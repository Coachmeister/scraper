from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import database_connection

def scrape():
    option = webdriver.ChromeOptions()
    option.add_argument("-incognito")

    browser = webdriver.Chrome(executable_path="C:/Development/python/chromedriver.exe", options=option)

    browser.get("https://ordnet.dk/ddo/ordbog?query=data")

    timeout = 20

    try:
        WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='definitionBoxTop']")))
    except TimeoutException:
        print("timed out")
        browser.quit()

    text_elements = browser.find_elements_by_xpath("//div[@class='definitionBoxTop']")
    boejninger = browser.find_elements_by_xpath("//div[@id='id-boj']")

    boej = [x.text for x in boejninger]
    text = [x.text for x in text_elements]

    print("text")
    print(text, "\n", " ", boej)

if __name__ == '__main__':
    scrape()
    database_connection.DatabaseConnection.create_connection(r"C:\Development\python\scraper\scraperdata.db")