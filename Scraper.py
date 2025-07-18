import requests
from bs4 import BeautifulSoup
def scrape_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('article')
        scraped_data = []
        for article in articles:
            title = article.find('h2').text.strip()
            link = article.find('a')['href']
            scraped_data.append({'title': title, 'link': link})
        return scraped_data
    else:
        print("Failed to retrieve data from the website.")
        return None