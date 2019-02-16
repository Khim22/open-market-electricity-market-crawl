from crawl import *

os.environ["PATH"] += os.pathsep + r'C:\Python27\Scripts'

print("Starting crawler")

driver = start_firefox_with_url("https://compare.openelectricitymarket.sg/#/pricePlans/list")

# Terms and conditions
execute_function_else_refresh( find_by_css_selector_and_click, "button.green-btn", driver)

# Select HDB dropdown
execute_function_else_refresh(find_and_click_dropdown_by_css_selector,".md-border", driver)


# Select HDB 4 room option
find_by_css_selector_and_click("md-option[value='HDB 4-Room']", driver)

# Click Next
find_by_css_selector_and_click("a.green-btn", driver)
time.sleep(1)

# Click Next
execute_function_else_refresh(find_by_css_selector_and_click, "a.green-btn", driver)
time.sleep(10)

######### Start of Page ##############

# Sort by Retailers
execute_function_else_refresh(find_and_click_dropdown_by_css_selector, "md-select.sort-dropdown", driver)

find_by_css_selector_and_click("md-option[value='retailerNameAsc']", driver)
time.sleep(5)

# find no of plans
no_of_plans = len(driver.find_elements_by_css_selector("button.md-raised.btn-bdr.select-btn.md-button.md-ink-ripple"))

# scrape data as arr of json obj
alldata = recursive_scrape_data(driver, no_of_plans)

# export data to json file
with open('data.json', 'w') as outfile:  
    json.dump(alldata, outfile)

driver.quit()

# convert json file to excel
output_json_to_excel('output.xls', 'data.json')
