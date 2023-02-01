from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv
import pandas as pd
# get link data
def extract(urlPage):

    driver = webdriver.Chrome('C:\\Users\\Tran Huu An\\Documents\\chromedriver.exe') # open chrome driver
    driver.get(urlPage) # get link job data
    time.sleep(3) # sleep 3s
    return driver


# scroll page
def scrollBar(driver):
    SCROLL_PAUSE_TIME = 0.5

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    numberHeightPage = 0
    new_height = 0
    while True:

        numberHeightPage += 50

        scrollPage = "window.scrollBy(" + str(new_height) +"," + str(numberHeightPage) + ");"
        driver.execute_script(scrollPage,"")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = numberHeightPage
        if new_height >= last_height:
            break

# extract infomation data job
def getData(driver):
    # implement get title data in page
    try:
        title = driver.find_element_by_class_name("jobsearch-JobInfoHeader-title-container").text # get title data
    except:
        title = None # if title is empty then None

    try:
        salary = driver.find_element_by_class_name("jobsearch-JobDescriptionSection-sectionItem").text # get salary
    except:
        salary = None # if salary is empty the None

    try:
        description = driver.find_element_by_id("jobDescriptionText").text # get description
    except:
        description = None # if description is empty the None
    tweet = (title, salary, description) # info job
    return tweet


# main
def main():
    Data = []
    # open File text and implement get the data to crwal info job
    # after add info job to array Data
    # the last write array info Data on the file csv
    with open('url.txt', 'r') as f:
        for link in range(1004):
            driver = extract(f.readline())
            scrollBar(driver)
            data = getData(driver)
            driver.close()
            time.sleep(3)
            Data.append(data)


    # import data in file data csv
    df = pd.DataFrame(Data, columns=['title', 'salary', 'description'])
    # save dataFrame
    df.to_csv('DataJobCsv.csv')


if __name__ == "__main__":
    main()