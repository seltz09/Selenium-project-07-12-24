# first project 07/12/2024 starting at 9:48 PM est

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get('https://www.amazon.com')
driver.maximize_window()

time.sleep(2)

#searching up go pro, my dad likes it
srch_btn = driver.find_element("id", 'twotabsearchtextbox')
srch_btn.click()
time.sleep(1)
srch_btn.send_keys('Go Pro 12 hero black')
srch_btn.send_keys(Keys.RETURN)

#adding it to cart
add_crt = driver.find_element("id", 'a-autoid-3-announce')
add_crt.click()
time.sleep(3)

#going to cart
cart = driver.find_element("id", 'nav-cart')
cart.click()
time.sleep(2)

#checking out product
checkout = driver.find_element("id", 'sc-buy-box-ptc-button')
checkout.click()
time.sleep(2)

#putting in email
email = driver.find_element("id", 'ap_email')
email.send_keys('leo is gay af')
email.send_keys(Keys.RETURN)


print('did it work?')
time.sleep(4)
