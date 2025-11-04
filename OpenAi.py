import openai
import Scraper
import re
openai.api_key = ""
raw = re.split(r'[,\.\n]+',Scraper.scrape_site("https://www.jovemprogramador.com.br/")+Scraper.scrape_site("https://www.jovemprogramador.com.br/apoiadores.php")+Scraper.scrape_site("https://www.jovemprogramador.com.br/sobre.php")+Scraper.scrape_site("https://www.jovemprogramador.com.br/patrocinadores.php")+Scraper.scrape_site("https://www.jovemprogramador.com.br/parceiros.php")+Scraper.scrape_site("https://www.jovemprogramador.com.br/duvidas.php")+Scraper.scrape_site("https://www.jovemprogramador.com.br/queroserprofessor/"))
raw = [item.strip().lower() for item in raw if item.strip()]
context = "\n".join(raw)
user_query = input()
prompt = f"{raw}{user_query}"
while True:
  completion = openai.Completion.create(
    model="gpt-4o-mini",
    prompt=prompt,  
    max_tokens=100,  
    temperature=0.2,
    stop=(".")
  )
  print(completion.choices[0].text.strip())
  context = ""
