import tkinter
import subprocess

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