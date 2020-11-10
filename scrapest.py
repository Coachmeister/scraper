from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
import pandas as pd
import os
from time import sleep
#import database_connection
#import elephantsql


def wheel_element(element, browser, deltaY = 120, offsetX = 0, offsetY = 0):
  error = browser.execute_script("""
    var element = document.querySelector('#search-result');
    var deltaY = arguments[0];
    var box = element.getBoundingClientRect();
    var clientX = box.left + (arguments[1] || box.width / 2);
    var clientY = box.top + (arguments[2] || box.height / 2);

    element.dispatchEvent(new MouseEvent('mouseover', {view: window, bubbles: true, cancelable: true, clientX: clientX, clientY: clientY}));
    element.dispatchEvent(new MouseEvent('mousemove', {view: window, bubbles: true, cancelable: true, clientX: clientX, clientY: clientY}));
    element.dispatchEvent(new WheelEvent('wheel',     {view: window, bubbles: true, cancelable: true, clientX: clientX, clientY: clientY, deltaY: deltaY}));
    return;
    """, deltaY, offsetX, offsetY)
  if error:
    raise WebDriverException(error)

def scrape():
    option = webdriver.ChromeOptions()
    #option.add_argument("-incognito")

    path = os.path.dirname(os.path.abspath(__file__))
    os.chmod(f"{path}/chromedriver", 755)
    browser = webdriver.Chrome(executable_path=f"{path}/chromedriver", options=option)

    browser.get("https://danbolig.dk/")

    timeout = 20

    try:
        WebDriverWait(browser, timeout).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@id='CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection']"))).click()
    except TimeoutException:
        print("timed out")
        browser.quit()

    search_button = browser.find_elements_by_xpath("//button[@id='frontpage-search-button']")
    search_button[0].click()

    browser.implicitly_wait(timeout)
    sleep(20)

    elm = browser.find_elements_by_xpath("//ul[@id='search-result']")
    wheel_element(elm, browser, 120, 0, 0)

    elements = browser.find_elements_by_class_name("bolig.show.action")
    print(len(elements))
    f = open('description.txt', 'a+')
    for element in elements:
        try:
            wrapper = element.find_element_by_xpath(".//div[@class='bolig-wrapper']")
            link = wrapper.find_elements_by_xpath(".//a[@href]")
            print(link)
            browser.execute_script("arguments[0].click();", link[0])
            #browser.get(link[0].get_attribute("href"))
            sleep(timeout)
            description = browser.find_element_by_class_name("db-description-block")
            print(description.text)
            f.write(f'{description.text}\n')
            browser.back()
        except NoSuchElementException:
            continue

    f.close()

  #  df = pd.DataFrame({"betydning": [text], "bøjninger": [boej]})
   # df.to_csv("test1")
   # print(df)

if __name__ == '__main__':
    scrape()





