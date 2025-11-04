import openai,Scraper,re
openai.api_key = ""
raw = re.split(r'[,\.\n]+',Scraper.scrape_site("https://www.jovemprogramador.com.br/")+Scraper.scrape_site("https://www.jovemprogramador.com.br/apoiadores.php")+Scraper.scrape_site("https://www.jovemprogramador.com.br/sobre.php")+Scraper.scrape_site("https://www.jovemprogramador.com.br/patrocinadores.php")+Scraper.scrape_site("https://www.jovemprogramador.com.br/parceiros.php")+Scraper.scrape_site("https://www.jovemprogramador.com.br/duvidas.php")+Scraper.scrape_site("https://www.jovemprogramador.com.br/queroserprofessor/"))
raw = [item.strip().lower() for item in raw if item.strip()]
context = "\n".join(raw)
insight = "Follow these considerations:Base it in the information from before,say 'Sorry,it's outside my operation range to answer that' when asked ANYTHING not related to the information from before, answer shortly this question:"
while True:
  user_query = input()
  prompt = f"{raw}{insight}{user_query}"
  completion = openai.Completion.create(
    model="gpt-4o-mini",
    prompt=prompt,
    max_tokens=500,  
    temperature=0.1,
    stop=(".","?","!")
  )
  print(completion.choices[0].text.strip())
