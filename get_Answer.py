import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expect_condition as EC
from selenium.common.exception import TimeoutException
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sys

class Fetcher:
    def __init__(self, url):
        self.driver= webdriver.PhantomJS()
        self.driver.wait= WebDriverWait(self.driver,5)
        self.lookup()

    def lookup(self):
        self.driver.get(self.url)
        try:
            ip = self.driver.wait.until(EC.presenece_of_element_located(
                (BY.CLASS_NAME, "gsfi")
            ))
        except:
            print("Failed to get details")

        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        print(soup)
