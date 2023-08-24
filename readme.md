# Weather Information Retrieval Program

This program utilizes Selenium WebDriver with ChromeDriver to fetch the current temperature and city information from a weather website. It is a simple example of web scraping for educational purposes. The program is written in Python.

## Prerequisites

- Python 3.x
- Selenium WebDriver
- ChromeDriver

## Installation

1. **Python**: If you don't have Python 3.x installed, download and install it from the official [Python website](https://www.python.org/downloads/).

2. **Selenium WebDriver**: You can install Selenium using the following pip command:

   ```bash
   pip install selenium
   ```

3. **ChromeDriver**: You need to download the appropriate version of ChromeDriver that matches your installed Chrome browser version. You can download ChromeDriver from the [official website](https://sites.google.com/chromium.org/driver/).

   After downloading ChromeDriver, make sure to place the executable in a directory that is included in your system's PATH variable.

## Usage

1. Clone or download this repository to your local machine.

2. Open the `gettemperature.py` file in a text editor.



3. Run the program using the following command:

   ```bash
   python gettemperature.py
   ```

4. The program will launch a Chrome browser window and navigate to the specified URL. It will then extract the temperature and city information from the page and display it in the console.

## Important Notes

- Web scraping might be against the terms of use of some websites. Make sure to review the website's `robots.txt` file and terms of use before scraping.

- Websites can change their structure and layout, which can break your scraping code. Regular maintenance might be required to keep the program functional.

- This example uses ChromeDriver. If you prefer using a different browser, you would need to install the corresponding WebDriver and make necessary changes in the code.

## Disclaimer

This program is intended for educational purposes only. Please be mindful of the legality and ethics of web scraping in your jurisdiction and follow best practices.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to customize and expand upon this README to fit your project's specific details and requirements.