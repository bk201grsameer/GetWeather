from termcolor import cprint
import requests
from bs4 import BeautifulSoup


def func():
    try:
        website = "https://www.flowrite.com/blog/thank-you-email"
        response = requests.get(website)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")

            # Find all the titles (assuming they are within <h3> tags)
            titles = soup.find_all("h3")
            # Find all the containers using CSS selector
            containers = soup.select("div.paragraph-60")

            if containers:
                for title, container in zip(titles, containers):
                    title_text = ((title.get_text(strip=True)).split("."))[1].strip()
                    cprint(f"[+] TITLE :{title_text}", "green")
                    for string in container.stripped_strings:
                        print(string)
                    print()
            else:
                print("Container not found.")

    except Exception as ex:
        print("[-] Exception:", str(ex))


if __name__ == "__main__":
    func()
