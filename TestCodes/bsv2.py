from termcolor import cprint
from selenium import webdriver
from bs4 import BeautifulSoup
import time


def func():
    try:
        url = "https://www.google.com/search?q=temperature&oq=temperature&aqs=edge..69i57j0i131i433i512j0i512l7.10796j0j1&sourceid=chrome&ie=UTF-8"

        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
        driver = webdriver.Chrome(options=options)

        driver.get(url)

        # Wait for a moment to let JavaScript content load
        time.sleep(5)

        soup = BeautifulSoup(driver.page_source, "html.parser")
        result = soup.find("span", class_="BBwThe")

        if result:
            city = result.get_text(strip=True)
            print("[+] CITY : ", city)
        else:
            print("[-] No matching result found")

        driver.quit()

    except Exception as ex:
        print("[-] EXCEPTION AS EX ", str(ex))


def main():
    func()


if __name__ == "__main__":
    main()
