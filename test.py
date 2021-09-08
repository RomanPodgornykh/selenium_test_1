from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get("http://tutorialsninja.com/demo/")
driver.close()

search_field = driver.find_element_by_name("search")

pass