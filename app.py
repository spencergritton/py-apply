import time
import os
from selenium import webdriver
from utilities.automate import fillInPageDetails
from utilities.coverLetter import generateCoverLetter

def getUrls():
    filepath = os.getcwd() + '/inputs/urls.txt'

    urls = []
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            if line.strip() != '':
                urls.append(line.strip())
            line = fp.readline()
            cnt += 1
    return urls

if __name__ == '__main__':
    # Get URL list from urls.txt (greenhouse.io)
    urls = getUrls()

    # Create application for each url
    browser = webdriver.Chrome(os.getcwd() + '/utilities/chromedriver')
    for url in urls:
        generateCoverLetter(url)
        browser.get(url)
        fillInPageDetails(browser)
        # Give user time to input resume, cover letter, and additional text boxes not filled out
        # Because this was made quickly there are usually text boxes to fill out
        time.sleep(30)
    browser.close()