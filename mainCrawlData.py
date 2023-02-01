from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

 # visit the website
def getWebSite(urlWeb):
    # get chromedriver
    driver = webdriver.Chrome('path chromeDriver')
    # get webSite
    driver.get(urlWeb)
    return driver

def scrollPageAndLoadPage(driver):
    # search name job
    searchJob = driver.find_element_by_id('text-input-what')
    searchJob.send_keys("Name job")

    # implement get page by number page
    # assignment numberPage = 1. The first load page from page 1 to last page
    numberPage = 1
    while True:
        # time sleep 5s
        SCROLL_PAUSE_TIME = 5

        # Get scroll height
        # load page from 0 to last height
        last_height = driver.execute_script("return document.body.scrollHeight") # last height page

        numberHeightPage = last_height - 1000 # the length we want to aim for
        scrollPage = "window.scrollBy(0," + str(numberHeightPage) + ")" # start scroll from 0 to numberHeightPage
        driver.execute_script(scrollPage, "") # execute action scrollPage

        # get url all jobs in all page
        jobs = driver.find_elements_by_xpath("//a[@class='jcs-JobTitle css-jspxzf eu4oa1w0']")

        # open File text and write url
        with open('url.txt', 'a') as f:
            for job in range(len(jobs)):
                lines = jobs[job].get_attribute("href")
                f.write(lines)

        time.sleep(SCROLL_PAUSE_TIME)
        numberPage += 1
        adressPage = "//div[@class='css-tvvxwd ecydgvn1']/a[@data-testid='pagination-page-" + str(numberPage) + "']"
        adressPage = adressPage.format(numberPage)
        changePage = driver.find_element_by_xpath(adressPage)
        if str(changePage) == None:
            break
        changePage.click()
        try:
            buttonClose = driver.find_element_by_xpath("//button[@aria-label='close']")
            buttonClose.click()
        except:
            pass



def main():
    url = 'name website'
    driver = getWebSite(url)
    scrollPageAndLoadPage(driver)
if __name__ == "__main__":
    main()