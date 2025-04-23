from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import time

@given('the user is on the login page')
def step_given_user_on_page(context):
    service = Service(GeckoDriverManager().install())
    context.driver = webdriver.Firefox(service=service)
    context.driver.get("http://127.0.0.1:8000/login/")

@when('the user enters a valid email and password')
def step_when_user_enters_valid_credetials(context):
    context.driver.find_element(By.ID, "email").send_keys("example@test.com")
    context.driver.find_element(By.ID, "password").send_keys("test")

@when('clicks the login button')
def step_when_user_clicks_login(context):
    context.driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

@then('the user should be redirected to the dashboard')
def step_then_redirect_to_dashboard(context):
    assert "Dashboard" in context.driver.title

@then('see a welcome message')
def step_then_see_welcome_message(context):
    message = context.driver.find_element(By.TAG_NAME, "h1").text
    assert "Welcome" in message
    context.driver.quit()
