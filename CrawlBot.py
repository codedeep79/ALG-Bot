from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import numpy as np
from console_logging.console import Console
import json
import os

console = Console()
curated_lists = []
browser = webdriver.Chrome()
console.info("Initialized Chrome Webdriver.")

def get_repos(pages=9):
    console.log("Now entering signup process.")

    # Page 1 of Signup
    browser.get('https://github.com/')
    # input('Log in, then press ENTER.')
    # browser.get(
    #    'https://github.com/search?o=desc&p=1&q=curated+list&s=stars&type=Repositories&utf8=%E2%9C%93')
    browser.get(
        'https://github.com/search?o=desc&p=100&q=curated+list')
    sleep(1)

    # Get repos
    console.info("Loaded search results.")
    for page in range(pages):
        search_results = browser.find_elements_by_class_name('repo-list-item')
        console.info("Found %d results..." % len(search_results))
        # ChangeProxy.proxyChange();
        sleep(2)
        for search_result in search_results:
            try:
                # Get text content in repo-list-item class by innerText JS attribute
                resultText = search_result.get_attribute('innerText').split('\n')
                curated_lists.append({
                    'repo': resultText[0],
                    'description': resultText[1]
                })
                console.success("Added " + resultText[0])
            except Exception as e:
                console.error(str(e))
        #browser.find_element_by_class_name('next_page').click()
        #console.log("Moving on...")
        sleep(1)

    #search_results = browser.find_elements_by_class_name('repo-list-item')
    #console.info("Found %d results..." % len(search_results))
    #for search_result in search_results:
    #    resultText = search_result.get_attribute('innerText').split('\n')
    #    curated_lists.append({
    #        'repo': resultText[0],
    #        'description': resultText[1]
    #    })
    #    console.success("Added " + resultText[0])
    browser.quit()

try:
    get_repos(pages=9)
except:
    pass

with open('./Curated list/curated_lists24.json', 'w') as curated_list_json_file:
    json.dump(curated_lists, curated_list_json_file, indent=4)
