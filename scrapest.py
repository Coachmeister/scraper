from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



def scrape():
    option = webdriver.ChromeOptions()
    option.add_argument("-incognito")

    browser = webdriver.Chrome(executable_path="F:\Development\scraper\chromedriver.exe", options=option)

    browser.get("https://ordnet.dk/ddo/ordbog?query=data")

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

    print(text, "\n", boej, "\n", click)


if __name__ == '__main__':
    scrape()
    #database_connection.create_connection(r"C:\Development\python\scraper\scraperdata.db")
    #database_connection.main()
