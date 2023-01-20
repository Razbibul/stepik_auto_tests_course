from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
    """формула для решения данного уровнения"""
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    price = WebDriverWait(browser, 13).until(
            EC.text_to_be_present_in_element((By.ID, "price"),'100')
            )

    button = browser.find_element(By.ID, "book")
    button.click()

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    polevvoda = browser.find_element(By.ID, "answer")
    polevvoda.send_keys(y)

    button2 = browser.find_element(By.ID, "solve")
    button2.click()

    print(browser.switch_to.alert.text.split(': ')[-1])

finally:
    browser.quit()