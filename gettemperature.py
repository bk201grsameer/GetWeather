from colorama import Fore, Style, init
from prettytable import PrettyTable
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def Table():
    try:
        """table config"""
        init()
        table = PrettyTable()
        table.field_names = [
            Fore.BLUE + "CITY" + Style.RESET_ALL,
            Fore.BLUE + "TEMPERATURE" + Style.RESET_ALL,
        ]
        return table

    except Exception as ex:
        print("[+] SOMETHING WENT WRONG WHILE CREATING TABLE ..")


def func():
    try:
        table = Table()
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-gpu")
        country = input("[+] Please Enter Country: ")
        searchCity = input("[+]Please Enter City: ")
        if country == "" or searchCity == "":
            return
        website = f"https://www.google.com/search?q={country}+{searchCity}"

        path = os.path.join(os.getcwd(), "chromedriver.exe")
        print("[+] APPLICATION STARTED ...")
        service = Service(executable_path=path)
        driver = webdriver.Chrome(options=options, service=service)
        driver.get(website)

        wait = WebDriverWait(driver, 10)
        city = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "yKMVIe")))
        # temperature = wait.until(EC.visibility_of_element_located((By.ID, "wob_tm")))
        temperature = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//span[@jsname="wcyxJ"]'))
        )
        if city and temperature:
            # print("[+] CITY : ", city.text)
            # print("[+] TEMPERATURE", temperature.text + "°C")
            table.add_row(
                [
                    Fore.GREEN + city.text + Style.RESET_ALL,
                    Fore.CYAN + temperature.text + "°C" + Style.RESET_ALL,
                ]
            )
            print(table)
    except Exception as ex:
        print("[-] EXECEPTION OCCURED ", (str(ex)))


func()
