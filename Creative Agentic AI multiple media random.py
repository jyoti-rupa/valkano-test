# -------------------- Browser Setup --------------------
import time

from selenium import webdriver   # ✅ CORRECT
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

# from test_agentic_ai_1597 import send_btn

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

#-------------------- Multiple media Testing -------------------------------------------
#------------------------*****-----------------*****-------------------*****------------
media_ids = [1670,1526,1497,1513,1475,1533,1595]

questions_overview =["Show me all comments from lovers relating to pacing, suspense, action sequences, casting, and acting..",
                         "Give me a generative summary for all feedback related to pacing and suspense"]

for media_id in media_ids:
    print(f"🔹 Testing media ID: {media_id}")

    # Open media page
    driver.get(f"https://volkno.ai/media/{media_id}/overview")
    wait.until(EC.url_contains(str(media_id)))
    # Switch to Creative tab
    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[2]/main/div/div/div[3]/div/button[3]")
        )
    ).click()

    # Open Agentic AI
    wait.until(
        EC.element_to_be_clickable((
            By.XPATH,"/html/body/div[2]/header/div/div[2]/div/button[1]/span[1]"
        ))
    ).click()

    # ---------------- ASK QUESTION (INSIDE LOOP) ----------------
    chatbox = wait.until(
        EC.visibility_of_element_located((
            By.XPATH, "/html/body/div[4]/div[3]/div/form/div[1]/textarea"
        ))
    )
    time.sleep(12)

    for question in questions_overview:
        print(f"Asking question: {question}")
        chatbox = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[4]/div[3]/div/form/div[1]/textarea")
            )
        )
        time.sleep(20)
        chatbox.clear()
        chatbox.send_keys(question)

        send_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[4]/div[3]/div/form/div[2]/button")
            )
        )
        send_btn.click()
        time.sleep(30)
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[4]/div[3]/div/form/div[1]/textarea")
            )
        )
        time.sleep(10)

