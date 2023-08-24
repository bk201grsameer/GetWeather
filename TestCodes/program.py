import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def func():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-gpu")

        website = "https://www.flowrite.com/blog/thank-you-email"
        path = r"D:\PROJECTS\PythonSockets\ETH\AutoMation\WebScrapper\chromedriver.exe"

        service = Service(executable_path=path)
        driver = webdriver.Chrome(options=options, service=service)
        driver.get(website)

        container = driver.find_element(By.XPATH, value='//div[@class="paragraph-60"]')
        # Add a delay to wait before extracting the text
        time.sleep(10)
        print("container:", container)
        print("container text:", container.text)

    except Exception as ex:
        print("[-] Exception:", str(ex))
    finally:
        driver.quit()


def main():
    func()


if __name__ == "__main__":
    main()
