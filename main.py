"""main.py"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from locators import TestLocators
from common import Webdata
from excel_functions import Hari_Excel_Functions

excel_file = Webdata().EXCEL_FILE

sheet_number = Webdata().SHEET_NUMBER

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get(Webdata().URL)

driver.implicitly_wait(10)

rows = Hari_Excel_Functions(excel_file, sheet_number).row_count()

for row in range(2, rows+1):
    username = Hari_Excel_Functions(excel_file, sheet_number).read_data(row, column_number=6)
    password = Hari_Excel_Functions(excel_file, sheet_number).read_data(row, column_number=7)

    driver.find_element(by=By.NAME, value=TestLocators().username_locator).send_keys(username)
    driver.find_element(by=By.NAME, value=TestLocators().password_locator).send_keys(password)
    driver.find_element(by=By.XPATH, value=TestLocators().submit_locator).click()

    #wait for the page to load and check the login is success or not

    driver.implicitly_wait(10)

    if Webdata().DASHBOARD_URL in driver.current_url:
        print("Login success")
        Hari_Excel_Functions(excel_file, sheet_number).write_data(row, column_number=8, data="TEST PASS")
        action = ActionChains(driver)
        action.click(on_element=TestLocators().logout_locator).perform()
        driver.find_element(by=By.LINK_TEXT, value= "Logout").click()
    elif Webdata().URL in driver.current_url:
        print("login failed")
        Hari_Excel_Functions(excel_file, sheet_number).write_data(row, column_number=8, data="TEST FAIL")

driver.quit()