# https://selenium-python.readthedocs.io/
# --------------------------------------------------------
from selenium import webdriver

# Returns a firefox browser object
browser = webdriver.Firefox()

# Getting automate the boring stuff webpage
browser.get('https://automatetheboringstuff.com')

# Selecting introduction link
elem = browser.find_element_by_css_selector('.main > div:nth-child(1) > ul:nth-child(20) > li:nth-child(1) > a:nth-child(1)')

# Clicking on it
elem.click()

# Selecting all the paragraphs from the page
elems = browser.find_elements_by_css_selector('p')
print(len(elems))

# Open github page and enter python in the search bar and click enter
browser.get('https://github.com/')
search_elem = browser.find_element_by_css_selector('input.input-sm')
search_elem.send_keys('python')
search_elem.submit()

# Back and forward in the browser
browser.back()
browser.forward()

# Refresh and quit the browser
browser.refresh()
browser.quit()

# Extract the entire text from a web page
browser = webdriver.Firefox()
browser.get('https://automatetheboringstuff.com')

elem = browser.find_element_by_css_selector('html')
print(elem.text)