from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyperclip
import pyautogui

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Move to target URL
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://nid.naver.com/nidlogin.login")
# driver.maximize_window() # open as biggest window

# input
driver.find_element(By.CSS_SELECTOR, "input#id").click()
pyperclip.copy("User_ID")
pyautogui.hotkey("ctrl", "v")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "input#pw").click()
pyperclip.copy("User_PW")
pyautogui.hotkey("ctrl", "v")
time.sleep(1)

# Click login button
driver.find_element(By.CSS_SELECTOR, "button#log\.login").click()