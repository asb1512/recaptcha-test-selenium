import tkinter
from tkinter import *
from tkinter.ttk import *
import subprocess
from turtle import width
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ExpectedConditions
from selenium.webdriver.support.ui import Select

# setting up native window
root = Tk()
root.geometry('125x65')
root.title("Selenium reCAPTCHA Score Tester")

# opening Chrome instance
def open_chrome():
  subprocess.Popen(
    [
      "open",
      "-na",
      "Google Chrome",
      "--args",
      "--remote-debugging-port=8989",
      # .../Users/<your_own_username_here>/Library...
      "--user-data-dir=/Users/andrewbourgeois/Library/Application Support/Google/Chrome/Default"
    ]
  )

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# main program logic
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
def run_recaptcha_test():

  # Chrome options
  options = Options()
  options.add_experimental_option("debuggerAddress", "localhost:8989")
  driver = webdriver.Chrome(
    executable_path="/usr/local/bin/chromedriver",
    options=options,
  )
  wait = WebDriverWait(driver, 60)

  def await_presence_of_xpath(code):
    wait.until(ExpectedConditions.presence_of_element_located((By.XPATH, code)))

  # navigate to demo webpage
  driver.get(
    'https://recaptcha-demo.appspot.com/recaptcha-v3-request-scores.php'
  )

  # wait for the presence of 'go' button
  await_presence_of_xpath(
      '//*/body/main/ol/li[@class="step1"]/button[@class="go"]')
  # locate 'go' button
  go_button = driver.find_element_by_xpath(
      '//*/body/main/ol/li[@class="step1"]/button[@class="go"]')
  go_button.click()

  # wait for the presence of demo result
  await_presence_of_xpath('//*/body/main/ol/li[@class="step4"]')
  # locate demo result
  demo_result = driver.find_element_by_xpath(
      '//*/body/main/ol/li[@class="step4"]').text
  print(demo_result)
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

# open Chrome button
open_chrome_button = tkinter.Button(
  root, width=10, text="Open Chrome", command=open_chrome
)
open_chrome_button.grid(row=1, column=1)

# start button
start_app_button = tkinter.Button(
  root, width=10, text="Start", command=run_recaptcha_test
)
start_app_button.grid(row=2, column=1)

root.mainloop()