import time
finish_time=time.time()+300

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")




def check_store():
    items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
    for item in items[::-1]:
        try:
            item.click()
        except:
            pass

button=driver.find_element(By.ID,"cookie")

while time.time()<finish_time:
    timeout = time.time() + 10
    while time.time()<timeout:
        button.click()

    check_store()

score=driver.find_element(By.ID,value="cps")
print(score.text)

driver.quit()