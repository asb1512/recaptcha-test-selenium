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

# main program logic
def run_recaptcha_test():

  # Chrome options
  options = Options()
  options.add_experimental_option("debuggerAddress", "localhost:8989")
  driver = webdriver.Chrome(
    executable_path="/usr/local/bin/chromedriver",
    chrome_options=options,
  )
  wait = WebDriverWait(driver, 60)

  # navigate to demo webpage
  driver.get()

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