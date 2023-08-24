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
        
        website = "https://www.flowrite.com/blog/thank-you-email"
        path = r"D:\PROJECTS\PythonSockets\ETH\AutoMation\WebScrapper\chromedriver.exe"
        
        service = Service(executable_path=path)
        driver = webdriver.Chrome(options=options, service=service)
        driver.get(website)

        # Wait for the container to be visible before extracting text
        wait = WebDriverWait(driver, 10)
        container = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="paragraph-60"]')))
        
        text = container.text
        print(text)
        
    except Exception as ex:
        print("[-] Exception:", str(ex))
    finally:
        driver.quit()

def main():
    func()

if __name__ == "__main__":
    main()
