
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

opt = Options()
opt.add_argument("--disable-notifications")

driver = webdriver.Chrome(r"C:\Users\iamab\Downloads\chromedriver_win32\chromedriver.exe",chrome_options=opt)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
username = driver.find_element_by_id("user-name")
username.clear()
username.send_keys("standard_user")

password = driver.find_element_by_id("password")
password.clear()
time.sleep(1)
password.send_keys("secret_sauce")
driver.find_element_by_id("login-button").click()
time.sleep(3)

driver.find_element_by_id("add-to-cart-sauce-labs-fleece-jacket").click()
time.sleep(2)
driver.find_element_by_id("shopping_cart_container").click()
time.sleep(2)
driver.find_element_by_id("checkout").click()
time.sleep(1)
driver.find_element_by_id("first-name").send_keys("Abhay")
driver.find_element_by_id("last-name").send_keys("Tiwari")
driver.find_element_by_id("postal-code").send_keys("231216")
driver.find_element_by_id("continue").click()
time.sleep(1)
driver.find_element_by_name("finish").click()
time.sleep(3)
driver.find_element_by_id("react-burger-menu-btn").click()
time.sleep(2)
driver.find_element_by_id("logout_sidebar_link").click()