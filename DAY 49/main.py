from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

events_list=driver.find_element(By.XPATH,value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul').text.split('\n')
print(events_list)
dict={}
for i in range(0,len(events_list),2):
    dict[events_list[i]]=events_list[i+1]
print(dict)

# price_dollar=driver.find_element(By.CLASS_NAME, value='a-price-whole')
# price_cents=driver.find_element(By.CLASS_NAME, value='a-price-fraction')

# print(f"The price is ${price_dollar.text}.{price_cents.text}")


# close one tab
# driver.close()


#close whole window all tabs
driver.quit()