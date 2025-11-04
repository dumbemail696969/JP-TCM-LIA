import requests
from bs4 import BeautifulSoup
def scrape_site(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract visible text from paragraphs
    paragraphs = soup.find_all('p')
    text = "\n".join([para.get_text() for para in paragraphs])
    return text
#print(scrape_site("https://www.jovemprogramador.com.br/")+scrape_site("https://www.jovemprogramador.com.br/apoiadores.php")+scrape_site("https://www.jovemprogramador.com.br/sobre.php")+scrape_site("https://www.jovemprogramador.com.br/patrocinadores.php")+scrape_site("https://www.jovemprogramador.com.br/parceiros.php")+scrape_site("https://www.jovemprogramador.com.br/duvidas.php")+scrape_site("https://www.jovemprogramador.com.br/queroserprofessor/"))