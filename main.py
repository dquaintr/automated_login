from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



#set options to make browsing easier

def get_driver():
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")


  driver = webdriver.Chrome(options=options)
  driver.get("https://automated.pythonanywhere.com/login/")
  return driver

"""def clean_text(text):
  output = float(text.split(": ")[1])
  return output"""

def main():
  driver = get_driver()
  driver.find_element(by="id", value="id_username").send_keys("automated")
  time.sleep(2)
  driver.find_element(by="id", value= "id_password").send_keys("automatedautomated" + Keys.RETURN)
  time.sleep(2)
  driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
  text = driver.find_element(by="xpath", value = "/html/body/div[1]/div/h1[2]").text

  return text


print(main())
