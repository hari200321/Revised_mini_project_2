"""test_main2.py"""

from PageObjects.main2 import WebAutomation


URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

#positive test case for whether home url is working or not
def test_positive_home_url():
    test_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    assert test_url == URL
    print(f"Success{URL} is the valid url")

#Negative test case for whether home url is working or not
def test_negative_home_url():
    test_url = "Google.in"
    assert test_url == URL

#Verifying whether the username locator ans password locator are visible or not!
def test_u_name_and_pwd_visible_or_not():
    assert WebAutomation.visibility_of_username == WebAutomation.visibility_of_username
    assert WebAutomation.visibility_of_password == WebAutomation.visibility_of_password
    print(f"Passed!{WebAutomation.visibility_of_username} and {WebAutomation.visibility_of_password} both are visible")

#Verifying after successful whether all the fields are visible or not
def test_fields_are_visible_or_not():
    assert WebAutomation.login_and_fields_visibility_and_clickability_checking == WebAutomation.login_and_fields_visibility_and_clickability_checking
    print(f"{WebAutomation.login_and_fields_visibility_and_clickability_checking} is visible ")

#verifying new user is able to login or not
def test_new_user_login():
    assert WebAutomation.login_with_new_user == WebAutomation.login_with_new_user
    print(f"{WebAutomation.login_with_new_user} is able to login to the webpage")





