from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

# stats=driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
# all_portals=driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

fName=driver.find_element(By.NAME, value="fName")
fName.send_keys("Shreya",Keys.TAB)
lName=driver.find_element(By.NAME, value="lName")
lName.send_keys("Shastry",Keys.TAB)
email=driver.find_element(By.NAME, value="email")
email.send_keys("shsh@gmail.com",Keys.ENTER)
