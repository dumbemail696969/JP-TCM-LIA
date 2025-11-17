import requests
import re
from bs4 import BeautifulSoup
def scrape_site(urls):
    text = ""
    texts = ""
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        text = "\n".join([para.get_text() for para in paragraphs])
        texts += text
    return texts
def cleaning(text):
    raw = re.split(r'[,\.\n]+', text)
    raw = [item.strip().lower() for item in raw if item.strip()]
    return list(set(raw))
urls = [
    "https://www.jovemprogramador.com.br/",
    "https://www.jovemprogramador.com.br/apoiadores.php",
    "https://www.jovemprogramador.com.br/sobre.php",
    "https://www.jovemprogramador.com.br/patrocinadores.php",
    "https://www.jovemprogramador.com.br/parceiros.php",
    "https://www.jovemprogramador.com.br/duvidas.php",
    "https://www.jovemprogramador.com.br/queroserprofessor/"
]
content = scrape_site(urls)
content = cleaning(content)
content = "\n".join(content)
with open(r"C:\Users\gustavo.lopes1\OneDrive - SENAC-SC\Code\TCM-1.8.2\content.txt", "w", encoding="utf-8") as file:
    file.write(content)