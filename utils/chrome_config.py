from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import streamlit as st
import tempfile
import json
import os

from utils.config import is_local

def chrome():
   
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_experimental_option('detach', True)
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')

    if is_local():
        service = Service('chromedriver.exe')
        driver = webdriver.Chrome(service=service, options=chrome_options)
    else:
        driver = webdriver.Chrome(options=chrome_options)

    return driver

