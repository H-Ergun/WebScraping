from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time



driver = webdriver.Edge()
driver.get("https://accounts.google.com/lifecycle/steps/signup/username?TL=AC3PFD6_n6FSFJ5FHOHLaobQM-KLx-UI8rlNjButol7zQoleDe_Zl4AwPTzwuGnd&ddm=0&dsh=S-1223980158%3A1718714056150210&flowEntry=SignUp&flowName=GlifWebSignIn&hl=tr-HU")

time.sleep(2)

radio_buttons = driver.find_elements(By.XPATH,'//div[@aria-checked="false"]')

driver.execute_script('arguments[0].setAttribute("aria-checked", "true");', radio_buttons[0])
time.sleep(1)