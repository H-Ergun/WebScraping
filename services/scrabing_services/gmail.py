from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from selenium.webdriver.support.ui import Select
from utils.randomSleep import randomSleeper

WAIT=2
URL = 'https://accounts.google.com/lifecycle/steps/signup/name?ddm=0&dsh=S1932408503:1718618767020266&flowEntry=SignUp&flowName=GlifWebSignIn&hl=tr-HU&TL=AC3PFD5EqE0lMdLaTct2h_vchavwW5kGq15dS4cMKRVMq8SbpPoUAC2-gio4d2Tp'

NEXT_BUTTON_TAG_NAME = [ "//span[contains(text(), 'Sonraki')]","//span[contains(text(), 'İleri')]" ]

def next_button(driver):     
     for selector in NEXT_BUTTON_TAG_NAME:
        try:
            WebDriverWait(driver, WAIT).until(EC.presence_of_element_located((By.XPATH, selector))).click()  
            randomWaiter(driver)      
        except:
            pass


def createAccount(driver,
                  first_name,
                  last_name,
                  month,
                  day,
                  year,
                  GenderEnum,
                  password
                  ):
    
    driver.get(URL)

    next_button(driver)

    name_input = WebDriverWait(driver, WAIT).until(EC.presence_of_element_located((By.NAME, 'firstName')))
    name_input.send_keys(first_name)
    lastname_input = WebDriverWait(driver, WAIT).until(EC.presence_of_element_located((By.NAME, 'lastName')))
    lastname_input.send_keys(last_name)

    next_button(driver)

    day_input = WebDriverWait(driver, WAIT).until(EC.presence_of_element_located((By.NAME, 'day')))
    day_input.send_keys(int(day))

    month_combobox = Select(WebDriverWait(driver, WAIT).until(EC.element_to_be_clickable((By.ID, 'month'))))
    month_combobox.select_by_index(int(month))

    year_input = WebDriverWait(driver, WAIT).until(EC.presence_of_element_located((By.ID, 'year')))
    year_input.send_keys(int(year))

    gender_input = Select(WebDriverWait(driver, WAIT).until(EC.presence_of_element_located((By.ID, 'gender'))))
    gender_input.select_by_value(str(GenderEnum.value))

    next_button(driver=driver)

    try:
        create_input = WebDriverWait(driver, WAIT).until(EC.element_to_be_clickable((By.ID, 'selectionc2')))
        print(create_input.text)
        create_input.click()
        next_button(driver)
    except:
        create_username(driver=driver,name=first_name,surname=last_name)  
    
    

    password_input = WebDriverWait(driver, WAIT).until(EC.element_to_be_clickable((By.NAME, 'Passwd')))
    password_input.send_keys(password)
    randomSleeper()
    password_confirm_input = WebDriverWait(driver, WAIT).until(EC.element_to_be_clickable((By.NAME, 'PasswdAgain')))
    password_confirm_input.send_keys(password)

    next_button(driver)



    randomSleeper(min=90,max=100)
  



def randomWaiter(driver,min=0,max=2):
    waitCounter= random.uniform(min,max)
    driver.implicitly_wait(waitCounter)



def create_username(driver,name,surname):
    count=random.randint(0,1000)
    xpath_expression = "//div[contains(text(), 'Bu kullanıcı adı alınmış. Başka bir tane deneyin.')]"
    is_allowed_username = "//span[contains(text(), 'Müsait:')]"
    allowed_username_button = "//button[@data-username]"
    while(True):
        count+=random.randint(1,253)
        username_input = WebDriverWait(driver, WAIT).until(EC.presence_of_element_located((By.NAME, 'Username')))
        username_input.clear()
        username_input.send_keys(name+surname+str(count)) 
        next_button(driver) 
        try:  
            my_div =  WebDriverWait(driver, WAIT).until(EC.presence_of_element_located((By.XPATH, xpath_expression)))   
            try:
                button =  WebDriverWait(driver, WAIT).until(EC.presence_of_element_located((By.XPATH, allowed_username_button))) 
                button.click()
                print(button.text)
                next_button(driver) 
            except:
                pass
            pass
        except:    
            break
    
    




