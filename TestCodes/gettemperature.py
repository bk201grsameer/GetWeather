import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def func():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-gpu")
        website = "https://www.google.com/search?q=temperature&oq=temperature&aqs=edge..69i57j0i131i433i512j0i512l7.10796j0j1&sourceid=chrome&ie=UTF-8"
        path = os.path.join(os.getcwd(), "chromedriver.exe")
        print("[+] APPLICATION STARTED ...")
        service = Service(executable_path=path)
        driver = webdriver.Chrome(options=options, service=service)
        driver.get(website)

        wait = WebDriverWait(driver, 10)
        city = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "BBwThe")))
        temperature = wait.until(EC.visibility_of_element_located((By.ID, "wob_tm")))
        if city and temperature:
            print("[+] CITY : ", city.text)
            print("[+] TEMPERATURE", temperature.text + "°C")
    except Exception as ex:
        print("[-] EXECEPTION OCCURED ", (str(ex)))

func()
