import re
import openai
import Scraper
openai.api_key = ""
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
raw = re.split(r'[,\.\n]+', all_text)
raw = [item.strip().lower() for item in raw if item.strip()]
unique_raw = list(set(raw))
context = "\n".join(unique_raw)

system_prompt = (
    "You are an assistant that only answers questions based on the following context.\n"
    "If asked for a phone number answer to look in the site.\n"
    "If a question is unrelated, say: 'Sorry, it's outside my job to answer that.'\n"
    "Be short and concise.\n"
    "Your only source of information is the database and nonthing else\n\n"

    f"Context:\n{context}"
)
while True:
    user_query = input("You: ")

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_query}
        ],
        max_tokens=200,
        temperature=0.1
    )

    print("Bot:", response['choices'][0]['message']['content'].strip())
