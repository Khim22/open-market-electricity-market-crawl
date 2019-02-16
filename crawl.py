from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import os
import time
import math
import json


# os.environ["PATH"] += os.pathsep + r'C:\Python27\Scripts'

# print("Starting crawler")

def execute_function_else_refresh(fn, selector, driver):
    while not fn(selector, driver):
        driver.refresh()
        time.sleep(1)
        fn(selector, driver)
    return True


def find_by_css_selector_and_click(selector, driver):
    try:
        elem = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
        elem.click()
        return True
    except:
        return False



def find_and_click_dropdown_by_css_selector(selector, driver):
    try:
        _dropdown = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
        driver.execute_script("arguments[0].click();", _dropdown)
        return True
    except:
        return False


def start_firefox_with_url(url):
    driver = webdriver.Firefox()
    driver.get(url)
    driver.implicitly_wait(20)

    time.sleep(5)

    return driver

def recursive_scrape_data(driver, no_of_plans):
    alldata = []

    for count in range(math.ceil(no_of_plans/3)):
        start = count * 3
        end = start + 3
        if(end > no_of_plans):
            end = no_of_plans
        # click 3 'Add to Compare' buttons at a time
        for click in range(start,end):
            _button = driver.find_elements_by_css_selector("button.md-raised.btn-bdr.select-btn.md-button.md-ink-ripple")[click]
            _button.click()
        
        # click 'Compare' to open up modal
        find_by_css_selector_and_click("button.compare-button.md-ink-no.md-button.md-ink-ripple", driver)
        time.sleep(3)

        # crawl data and append to list
        alldata.extend(crawl_data_from_table(driver))
        find_by_css_selector_and_click("button.flex-order-0.flex-order-gt-sm-4.md-icon-button.md-button.md-ink-ripple", driver)
        time.sleep(1)
        find_by_css_selector_and_click( "button.compare-button.deselect.md-button.md-ink-ripple:not(.btn-disabled):not(.white-bg-btn)", driver)

    return alldata


def crawl_data_from_table(driver):
    def get_name(html):
        return html.get_text()
    
    data = []
    source = driver.page_source
    soup = BeautifulSoup(source,"lxml")

    retailers = list(map(get_name, soup.select('.flex.resp-img-container.ng-scope > h5')))
    datarows = list(soup.find_all('div' , class_= 'layout-gt-sm-row layout-xs-column layout-sm-column'))

    for i in range(len(retailers)):
        json_obj = {}
        json_obj['Retailer'] = retailers[i]
        data.append(json_obj)

    if(len(datarows) > 0):
        for row in datarows:
            onerowTitle = row.select(".flex-gt-md-25.flex-md-30.pad.grey-bg")[0].get_text()
            onerow = row.select('.flex-gt-sm-75.flex-md-30.layout-row.pad.text-center > .ng-scope:not([aria-hidden="true"])')
            for index, item in enumerate(onerow, start=0):
                (data[index])[onerowTitle] = item.get_text().strip()
    return data


def output_json_to_excel(excel_filename, json_filename):
    columns = []
    _filename = 'data.json'
    # data_json = open(_filename, 'r')
    # df = json.load(data_json)
    with open(_filename, 'r') as data_json:
        df = json.load(data_json)
    for key in df[0]: 
        columns.append(key)

    pd.DataFrame(df, columns=columns).to_excel('output.xls')


# driver = start_firefox_with_url("https://compare.openelectricitymarket.sg/#/pricePlans/list")

# # Terms and conditions
# execute_function_else_refresh( find_by_css_selector_and_click, "button.green-btn")

# # Select HDB dropdown
# execute_function_else_refresh(find_and_click_dropdown_by_css_selector,".md-border")


# # Select HDB 4 room option
# find_by_css_selector_and_click("md-option[value='HDB 4-Room']")

# # Click Next
# find_by_css_selector_and_click("a.green-btn")
# time.sleep(1)

# # Click Next
# execute_function_else_refresh(find_by_css_selector_and_click, "a.green-btn")
# time.sleep(10)

# ######### Start of Page ##############

# # Sort by Retailers
# execute_function_else_refresh(find_and_click_dropdown_by_css_selector, "md-select.sort-dropdown")
# # driver.execute_script("arguments[0].click();", _dropdown)

# find_by_css_selector_and_click("md-option[value='retailerNameAsc']")
# time.sleep(5)

######### Start of additional filter: TO BE IMPLEMENTED ##############

# find_and_click_dropdown_css_selector("md-select[name='customerType']")
# find_by_css_selector_and_click("md-option[value='COM']")

# # find_by_css_selector_and_click(".custome-select-menu-container")
# # find_by_css_selector_and_click("md-option[value='FR']")
# time.sleep(2)
# find_and_click_dropdown_css_selector("md-select[aria-label='Search Retailer(s)']")
# find_by_css_selector_and_click("md-option[value='BESTPE']")
# driver.find_element_by_tag_name('body').send_keys(Keys.TAB)
# time.sleep(2)

# inputField = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "monthlyConsumption")))
# inputField.send_keys('100')

######### End of additional filter: TO BE IMPLEMENTED ##############

# Find number of plans
# no_of_plans = len(driver.find_elements_by_css_selector("button.md-raised.btn-bdr.select-btn.md-button.md-ink-ripple"))
# alldata = recursive_scrape_data()


# with open('data.json', 'w') as outfile:  
#     json.dump(alldata, outfile)

# driver.quit()


# output_json_to_excel('output.xls', 'data.json')

