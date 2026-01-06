import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
#Browser setup
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

#------------------------Open website-------------------
driver.get("https://volkno.ai/")
time.sleep(5)
driver.maximize_window()
#--------------------log in to the page---------------
#Click on portal login button
driver.find_element(By.XPATH, "/html/body/main/div/div[1]/div/div/div/div/div/nav/ul/li[7]/a").click()
time.sleep(5)

#---------------------------Fill the login form---------------------
Email = driver.find_element(By.XPATH,"/html/body/div/main/section/div/div/div/form/div[1]/div/div[1]/div[1]/input")
Email.send_keys("anthony@pineapples.dev")
password = driver.find_element(By.XPATH,"/html/body/div/main/section/div/div/div/form/div[1]/div/div[2]/div[1]/input")
password.send_keys("Pineapples69$")
driver.find_element(By.XPATH, "/html/body/div/main/section/div/div/div/form/div[2]/button").click()
time.sleep(5)

#---------------------media item selection 1497----------------------------------
driver.get("https://volkno.ai/media/1497/overview")
#driver.find_element(By.XPATH,"/html/body/div[2]/nav/div/div/a[1]").click()
time.sleep(10)
#go to the media details
#driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[2]/div/div[2]/a[1]/div/div[1]/div[2]/h3").click()
#time.sleep(10)
#Open agentic ai
driver.find_element(By.XPATH,"/html/body/div[2]/header/div/div[2]/div/button[1]").click()
time.sleep(2)
chatbox=driver.find_element(By.XPATH,"/html/body/div[4]/div[3]/div/form/div[1]/textarea")
chatbox.send_keys("What are the weakest contributing components of the composite score?")
time.sleep(10)
driver.find_element(By.XPATH,"/html/body/div[4]/div[3]/div/form/div[2]/button").click()
time.sleep(10)
chatbox=driver.find_element(By.XPATH,"/html/body/div[4]/div[3]/div/form/div[1]/textarea")
chatbox.send_keys("Explain what the composite score means for this title in simple terms.")
time.sleep(20)
driver.find_element(By.XPATH,"/html/body/div[4]/div[3]/div/form/div[2]/button").click()
time.sleep(15)
chatbox.send_keys("Break down what factors contributed most to the composite score.")
time.sleep(20)
driver.find_element(By.XPATH,"/html/body/div[4]/div[3]/div/form/div[2]/button").click()
time.sleep(15)
#-------- Close the agentic Ai pop up-----------

driver.find_element(By.TAG_NAME, "body").click()
#----------open Audiance______
driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div[3]/div/button[2]").click()
time.sleep(5)
# ________________ ASK QUES___________
driver.find_element(By.XPATH,"/html/body/div[2]/header/div/div[2]/div/button[1]").click()
time.sleep(2)
chatbox=driver.find_element(By.XPATH,"/html/body/div[4]/div[3]/div/form/div[1]/textarea")
chatbox.send_keys("Identify my target audience and describe their demographic and psychographic traits.")
driver.find_element(By.XPATH,"/html/body/div[4]/div[3]/div/form/div[2]/button").click()
time.sleep(10)
chatbox=driver.find_element(By.XPATH,"/html/body/div[4]/div[3]/div/form/div[1]/textarea")
chatbox.send_keys("What platforms does my target audience prefer for this title?")
driver.find_element(By.XPATH,"/html/body/div[4]/div[3]/div/form/div[2]/button").click()
time.sleep(10)