
import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"

response = requests.get(URL)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

headlines = []

for tag in soup.find_all('h2'):
    title = tag.get_text(strip=True)
    if title:
        headlines.append(title)
with open("headlines.txt", "w", encoding="utf-8") as file:
    for i, headline in enumerate(headlines, 1):
        file.write(f"{i}. {headline}\n")

print(f"{len(headlines)} headlines saved to 'headlines.txt'")
