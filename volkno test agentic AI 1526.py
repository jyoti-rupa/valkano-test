# -------------------- Imports --------------------
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# -------------------- Browser Setup --------------------
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)
wait = WebDriverWait(driver, 30)




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

# -------------------- OPEN MEDIA PAGE --------------------
wait.until(EC.url_contains("volkno.ai"))
driver.get("https://volkno.ai/media/1526/overview")

# -------------------- OPEN AGENTIC AI --------------------
agentic_ai_btn = wait.until(
    EC.element_to_be_clickable((
        By.XPATH, "/html/body/div[2]/header/div/div[2]/div/button[1]/span[1]"
    ))
)
agentic_ai_btn.click()

# -------------------- QUESTION 1 --------------------
chatbox = wait.until(
    EC.visibility_of_element_located((
        By.XPATH, "/html/body/div[4]/div[3]/div/form/div[1]/textarea"
    ))
)
chatbox.send_keys(
    "What does the composite score indicate about overall performance?"
)

send_btn = wait.until(
    EC.element_to_be_clickable((
        By.XPATH, "/html/body/div[4]/div[3]/div/form/div[2]/button"
    ))
)
send_btn.click()

# Wait for AI response
time.sleep(35)

# -------------------- QUESTION 2 --------------------
chatbox = wait.until(
    EC.visibility_of_element_located((
        By.XPATH, "/html/body/div[4]/div[3]/div/form/div[1]/textarea"
    ))
)
chatbox.send_keys(
    "What worked well and what didn’t in the composite score calculation?"
)

send_btn = wait.until(
    EC.element_to_be_clickable((
        By.XPATH, "/html/body/div[4]/div[3]/div/form/div[2]/button"
    ))
)
send_btn.click()

time.sleep(35)

# -------------------- CLOSE AI MODAL --------------------
# Click on empty body area to close overlays
wait.until(EC.element_to_be_clickable((By.TAG_NAME, "body"))).click()


# -------------------- OPEN Key / Art TAB --------------------
key_tab = wait.until(
    EC.element_to_be_clickable((
        By.XPATH, "/html/body/div[2]/main/div/div/div[3]/div/button[5]"
    ))
)
key_tab.click()

# -------------------- OPEN AGENTIC AI AGAIN --------------------
agentic_ai_btn = wait.until(
    EC.element_to_be_clickable((
        By.XPATH, "/html/body/div[2]/header/div/div[2]/div/button[1]/span[1]"
    ))
)
agentic_ai_btn.click()

# -------------------- QUESTION 3 --------------------
chatbox = wait.until(
    EC.visibility_of_element_located((
        By.XPATH, "/html/body/div[4]/div[3]/div/form/div[1]/textarea"
    ))
)
chatbox.send_keys(
    "Give me a generative summary for all feedback related to pacing and suspense."
)

send_btn = wait.until(
    EC.element_to_be_clickable((
        By.XPATH, "/html/body/div[4]/div[3]/div/form/div[2]/button"
    ))
)
send_btn.click()

time.sleep(35)

# -------------------- QUESTION 4 --------------------
hatbox = wait.until(
    EC.visibility_of_element_located((
        By.XPATH, "/html/body/div[4]/div[3]/div/form/div[1]/textarea"
    ))
)
chatbox.send_keys(
    "Summarize all user comments related to action scenes"
)

send_btn = wait.until(
    EC.element_to_be_clickable((
        By.XPATH, "/html/body/div[4]/div[3]/div/form/div[2]/button"
    ))
)
send_btn.click()

time.sleep(35)


# -------------------- CLOSE AI MODAL --------------------
driver.find_element(By.TAG_NAME, "body").click()

print("✅ Script executed successfully")