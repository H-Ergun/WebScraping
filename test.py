from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome()

# driver = webdriver.Edge()
driver.get("https://accounts.google.com/lifecycle/steps/signup/name?ddm=0&dsh=S1932408503:1718618767020266&flowEntry=SignUp&flowName=GlifWebSignIn&hl=tr-HU&TL=AC3PFD5EqE0lMdLaTct2h_vchavwW5kGq15dS4cMKRVMq8SbpPoUAC2-gio4d2Tp")


time.sleep(2)

buttons = driver.find_elements(By.TAG_NAME, 'button')


try:
    for button in buttons:
        button_text = button.text
        if button_text=="Sonraki":
            button.click()    
            firstNameInput=driver.find_element(By.NAME, 'firstName')
            lastNameInput=driver.find_element(By.NAME, 'lastName')
            firstNameInput.send_keys("Hüseyin")
            lastNameInput.send_keys("Ergün")
            submitButtons=driver.find_elements(By.TAG_NAME, 'button')
            
            for submitButton in submitButtons:
                button_text = submitButton.text
                if button_text=="Sonraki":
                    submitButton.click()  
                    time.sleep(2)
                    dayInput=driver.find_element(By.NAME, 'day')
                    monthSelect=Select(driver.find_element(By.ID, 'month'))
                    yearInput=driver.find_element(By.NAME, 'year')
                    genderSelect=Select(driver.find_element(By.ID, 'gender'))

                    dayInput.send_keys(2)
                    monthSelect.select_by_value("3")
                    yearInput.send_keys(1998)                  
                    #2 kadın, 1 erkek, 3 belirtmek istemiyorum, 4 özel
                    genderSelect.select_by_value("1")
                    submitButtons=driver.find_elements(By.TAG_NAME, 'button')
                    
                    for submitButton in submitButtons:
                        button_text = submitButton.text
                        if button_text=="Sonraki":
                            submitButton.click()  
                            time.sleep(1)                           

                            radio_buttons = driver.find_elements(By.XPATH,'//div[@aria-checked="false"]')

                            if len(radio_buttons)== 0:
                                userNameInput=driver.find_elements(By.NAME, 'Username')
                                userNameInput[0].send_keys("ergHuseyn34")
                            else:           
                               clickableDiv = driver.find_element(By.XPATH,'//div[@jsname="CeL6Qc"]')
                               clickableDiv.click()
                            
                            time.sleep(1)

                            submitButtons=driver.find_elements(By.TAG_NAME, 'button') 
                                            
                            for submitButton in submitButtons:
                                button_text = submitButton.text
                                if button_text=="Sonraki":
                                    submitButton.click()                                  
                                    time.sleep(1)
                                    passwordInput=driver.find_element(By.NAME, 'Passwd')
                                    passwordAgainInput=driver.find_element(By.NAME, 'PasswdAgain')
                                    passwordInput.send_keys("Huseynergun1.")
                                    time.sleep(2.5)
                                    passwordAgainInput.send_keys("Huseynergun1.") 
                                    submitButtons=driver.find_elements(By.TAG_NAME, 'button')                  
                                    for submitButton in submitButtons:
                                        button_text = submitButton.text
                                        if button_text=="İleri":
                                            submitButton.click()        

except Exception as ex:
    print(ex)








# button.click()

time.sleep(5000)

# driver.quit()
# ChromeDriver'ın yolu
# driver_path = r"C:\Users\huseyin.ergun\Desktop\python\chromedriver\chromedriver-win64\chromedriver.exe"

# # WebDriver'ı başlat
# driver = webdriver.Chrome(driver_path)

# # Bir web sitesine git
# driver.get('https://accounts.google.com/lifecycle/steps/signup/name?ddm=0&dsh=S1561209489:1718615401887685&flowEntry=SignUp&flowName=GlifWebSignIn&TL=AC3PFD6FDrtfnd9C99yFpswd4eiMFgZH7jYVE0PyrV7LlJxVbLr61A1a_NOP3sr6')