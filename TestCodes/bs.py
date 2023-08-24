import requests
from bs4 import BeautifulSoup

def main():
    try:
        website = "https://www.flowrite.com/blog/thank-you-email"
        response = requests.get(website)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            
            # Find all the titles (assuming they are within <h3> tags)
            titles = soup.find_all("h3")
            
            # Find all the containers by class name
            containers = soup.find_all("div", class_="paragraph-60")
            
            if containers:
                for title, container in zip(titles, containers):
                    # Extract the text content from title and container
                    title_text = title.get_text(strip=True)
                    container_text = container.get_text(strip=True)
                    
                    print("Title:", title_text)
                    print("Text:", container_text)
                    print("-" * 40)
            else:
                print("No containers found.")

    except Exception as ex:
        print("[-] Exception:", str(ex))

if __name__ == "__main__":
    main()
