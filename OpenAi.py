import re
import openai
import  Scraper
openai.api_key = ""

# Assume Scraper.scrape_site is defined and works correctly

# Scrape and clean data
urls = [
    "https://www.jovemprogramador.com.br/",
    "https://www.jovemprogramador.com.br/apoiadores.php",
    "https://www.jovemprogramador.com.br/sobre.php",
    "https://www.jovemprogramador.com.br/patrocinadores.php",
    "https://www.jovemprogramador.com.br/parceiros.php",
    "https://www.jovemprogramador.com.br/duvidas.php",
    "https://www.jovemprogramador.com.br/queroserprofessor/"
]

all_text = ""
for url in urls:
    all_text += Scraper.scrape_site(url)

# Token-friendly cleaning
raw = re.split(r'[,\.\n]+', all_text)
raw = [item.strip().lower() for item in raw if item.strip()]
context = "\n".join(raw)

system_prompt = (
    "You are an assistant that only answers questions based on the following context.\n"
    "If a question is unrelated, say: 'Sorry, it's outside my operation range to answer that.'\n"
    "Be short and concise.\n"
    f"Context:\n{context}"
)

# Chat loop
while True:
    user_query = input("You: ")

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  # Or "gpt-4o-mini" if it's enabled for chat
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_query}
        ],
        max_tokens=200,
        temperature=0.1
    )

    print("Bot:", response['choices'][0]['message']['content'].strip())
