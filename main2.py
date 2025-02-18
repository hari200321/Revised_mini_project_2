"""main2.py"""

#importing necessary modules to do automation
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.keys import Keys

# importing expected conditions modules
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

#importing exception handling modules
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException

from locators import TestLocators
from common import Webdata

#its the main parent class which inherit Testlocators and Webdata classes
class WebAutomation(TestLocators, Webdata):

    def __init__(self):# Constructor
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 15)
        self.actions = ActionChains(self.driver)

    def start(self): #here im get the URL and maximizing the window

        try:
            self.driver.maximize_window()
            self.driver.get(self.URL)
            return f"{self.URL} is working"

        except NoSuchElementException as error:
            print(error)

    def visibility_of_username(self):# To check the visibility of the username locator
        try:
            username_locator = self.wait.until(EC.visibility_of_element_located((By.NAME, self.username_locator)))
            return 'username locator is visible'

        except (NoSuchElementException, ElementNotVisibleException) as error:
            print(error)

    def visibility_of_password(self): # to check the visibility of the password locator
        try:
            password_locator = self.wait.until(EC.visibility_of_element_located((By.NAME, self.password_locator)))
            return 'password locator is visible'

        except (NoSuchElementException, ElementNotVisibleException) as error:
            print(error)

    # to check the several fields are visible or not after login
    def login_and_fields_visibility_and_clickability_checking(self):
        try:
            self.driver.find_element(by=By.NAME, value = self.username_locator).send_keys(self.USERNAME)
            self.driver.find_element(by=By.NAME, value = self.password_locator).send_keys(self.PASSWORD)
            self.driver.find_element(by=By.XPATH, value = self.submit_locator).click()
            self.driver.implicitly_wait(5)

            #steps to check whether all the fields is visible or not!
            admin_locator = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.admin_locator)))
            pim_locator = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.pim_locator)))
            leave_locator = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.leave_locator)))
            time_locator = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.time_locator)))
            recruit_locator = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.recruitment_locator)))
            my_info_locator = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.my_info_locator)))
            performance_locator = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.dashboard_locator)))
            dashboard_locator = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.dashboard_locator)))

           #steps to check whether all the fields is clickable or not
            admin_locator = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.admin_locator)))
            pim_locator = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.pim_locator)))
            leave_locator = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.leave_locator)))
            time_locator = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.time_locator)))
            recruit_locator = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.recruitment_locator)))
            my_info_locator = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.my_info_locator)))
            performance_locator = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.dashboard_locator)))
            dashboard_locator = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.dashboard_locator)))

            return 'admin, pim, leave, time, recruitment, myinfo, performance, dashboard is visible and clickable'


        except NoSuchElementException as error:
            print(error)

    #this method is for to add a new user in OrangeHRM
    def add_new_user(self):
        self.driver.find_element(by=By.XPATH, value = self.select_admin_locator).click()
        self.actions.click(self.driver.find_element(by=By.XPATH, value = self.add_locator)).perform()
        self.actions.click(self.driver.find_element(by=By.XPATH, value = self.user_role)).perform()
        self.actions.click(self.driver.find_element(by=By.XPATH, value = self.ess_locator)).perform()
        self.actions.click(self.driver.find_element(by=By.XPATH, value = self.status_locator)).perform()
        self.actions.click(self.driver.find_element(by=By.XPATH, value = self.enable_locator)).perform()
        password = self.driver.find_element(by=By.XPATH, value = self.enter_password_locator)
        password.click()
        password.send_keys(self.PASSWORD2)
        self.driver.find_element(by=By.XPATH, value = self.employee_name_locator).send_keys(self.EMPLOYEE_NAME)
        sleep(3)
        perform = self.actions.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN)
        perform.perform()
        perform = self.actions.key_down(Keys.ENTER).key_up(Keys.ENTER)
        perform.perform()
        u_name2 = self.driver.find_element(by=By.XPATH, value = self.username2_locator)
        u_name2.click()
        sleep(3)
        u_name2.send_keys(self.USERNAME2)
        c_password = self.driver.find_element(by=By.XPATH, value=self.enter_confirm_password_locator)
        c_password.click()
        sleep(3)
        c_password.send_keys(self.PASSWORD2)
        self.driver.implicitly_wait(10)
        self.actions.click(self.driver.find_element(by=By.XPATH, value = self.save_locator)).perform()
        sleep(3)
        self.actions.click(self.driver.find_element(by=By.XPATH, value = self.logout_locator)).perform()
        log_out = self.driver.find_element(by=By.XPATH, value = self.logout_locator2)
        log_out.click()
        sleep(3)
        return 'New user created successfully'


    # This method contains login using new user
    def login_with_new_user(self):
        self.driver.find_element(by=By.NAME, value = self.username_locator).send_keys(self.USERNAME2)
        self.driver.find_element(by=By.NAME, value = self.password_locator).send_keys(self.PASSWORD2)
        self.driver.find_element(by=By.XPATH, value = self.submit_locator).click()
        sleep(3)
        return 'login successful with new user credentials! '


    #once program ends it will quit successfully to avoid RAM issues!
    def shutdown(self):
        self.driver.quit()



#here hari is the object !
hari = WebAutomation()
print(hari.start())
print(hari.visibility_of_username())
print(hari.visibility_of_password())
print(hari.login_and_fields_visibility_and_clickability_checking())
print(hari.add_new_user())
print(hari.login_with_new_user())
hari.shutdown()

