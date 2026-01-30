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

# Move to new mail page
driver.get("https://mail.naver.com/v2/new")
time.sleep(1)

# input
driver.find_element(By.CSS_SELECTOR, "#recipient_input_element").send_keys("User_ID@email.address")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#subject_title").send_keys("Email send by automation python program")
time.sleep(1)
iframe = driver.find_element(By.CSS_SELECTOR, "#content > div.contents_area > div > div.editor_area > div > div.editor_body > iframe") # get into iframe tag
driver.switch_to.frame(iframe)
driver.find_element(By.CSS_SELECTOR, "body > div > div.workseditor-body > div.workseditor-content").send_keys("Thanks!")
time.sleep(1)
driver.switch_to.default_content() # get out from iframe tag

# Click send button
driver.find_element(By.CSS_SELECTOR, "#content > div.mail_toolbar.type_write > div:nth-child(1) > div > button.button_write_task").click()