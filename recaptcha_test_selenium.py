import tkinter
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
root.geometry('300x100')
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

  # start button
  start_app_button = tkinter.Button(
    root, width=200, bg="green", fg="white", text="Start", 
  )

  root.mainLoop()