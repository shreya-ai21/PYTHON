import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=chrome_options)
driver.get('https://orteil.dashnet.org/experiments/cookie')
perks=[]

cookie=driver.find_element(By.ID,'cookie')
perks=driver.find_elements(By.CSS_SELECTOR,value='#store .grayed b')
perks=perks[::-1]
perks_names_list=[]
for perk in perks[1:]:
    l=perk.text.split(' - ')
    perks_names_list.append(l[0])
print(perks_names_list)

def calculate_perks(perks_name_list):
    for i in range(50):
        cookie.click()
    money=int(driver.find_element(By.ID,value='money').text.replace(',',''))
    for perk in range(len(perks_name_list),0,-1):
        for i in range(10):
            cookie.click()
        val=driver.find_element(By.XPATH,f'/html/body/div[3]/div[5]/div/div[{perk}]')
        if val.get_attribute('class')!='grayed':
            value=driver.find_element(By.XPATH,f'/html/body/div[3]/div[5]/div/div[{perk}]/b').text
            value=value.split(' - ')
            perk_val=int(value[1].replace(',',''))
            # for i in range(50):
            #     cookie.click()
            if money>=perk_val:
                return val
                # for i in range(50):
                #     cookie.click()
                
            # perks_list.append(int(val[1].replace(',','')))
    return val

timeout=time.time() + 5
while True:
    time.sleep(0.25)
    for i in range(75):
        cookie.click()
    if time.time()>=timeout:
        cookie.click()  
        to_click=calculate_perks(perks_names_list)
        to_click.click()
        timeout=time.time()+5
        
        
