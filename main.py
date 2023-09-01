import time
from selenium import webdriver
from selenium.webdriver.common.by import By  # Import the By class
from selenium.webdriver.common.keys import Keys
import tkinter
import tkinter.messagebox
from selenium.webdriver.chrome.service import Service
import tkinter.simpledialog


service = Service()
driver = webdriver.Chrome(service=service)

# Create a function to pop up a message box to prompt the user to choose a course
def popup():
    tkinter.messagebox.showinfo('Tip', 'Please choose your favorite course within 15 seconds')


# Create a tkinter window but do not display it
root = tkinter.Tk()
root.withdraw()

# Pop up a small window to enter the username and password, and store them in variables
username = tkinter.simpledialog.askstring("username", "Please enter your username：")
password = tkinter.simpledialog.askstring("password", "please enter your password：", show="*")

# open the Web page
driver.get("https://www48.polyu.edu.hk/myhkcc_new/subject-registration/add-drop")

# Use the By.NAME strategy to find the username and password input boxes and fill in the previously entered values.
username_input = driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$UsernameTextBox")
username_input.send_keys(username)
password_input = driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$PasswordTextBox")
password_input.send_keys(password)

# Press the Enter key to submit the form
password_input.send_keys(Keys.RETURN)

# Wait 5 seconds for the page to load, you can adjust the time as needed
time.sleep(5)

# Click the "Next" button
Next = driver.find_element(By.XPATH, "//*[@id='sidebarPushable']/div[2]/div/div[2]/div[2]/div/div[2]/button")
Next.click()
Next2=driver.find_element (By.XPATH, "//*[@id='sidebarPushable']/div[2]/div/div[2]/div[2]/div/div[2]/button")
Next2.click()

# While waiting for 30 seconds, a small window pops up to prompt the user to select a course.
popup()
time.sleep(20)

# Start looping to detect course vacancies
openrefreshui=driver.find_element (By.XPATH, "//*[@id='sidebarPushable']/div[2]/div/div[2]/div[2]/div/div[2]/span/span/button")
openrefreshui.click()
while True:
    try:
        # Get remaining position
        vacancy = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/div/div[2]").text

        if int(vacancy) > 0:
            # Close the refresh page
            close=driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/button[2]")
            close.click()
            # Click the "Next" button
            Next1 = driver.find_element(By.XPATH, "//*[@id='sidebarPushable']/div[2]/div/div[2]/div[2]/div/div[2]/span/button[2]")
            Next1.click()
            time.sleep(1)
            confirm = driver.find_element(By.XPATH, "//*[@id='sidebarPushable']/div[2]/div/div[2]/div[2]/div/div[2]/button[2]")
            confirm.click()
            break
        else:
            # refresh page
            refresh = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/button[1]")
            refresh.click()
            time.sleep(2)
    except Exception as e:
        # Reload page or other operations
        driver.get("https://www48.polyu.edu.hk/myhkcc_new/subject-registration/add-drop")

# close the browser
driver.quit()
