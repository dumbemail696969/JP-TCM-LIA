import os
from dotenv import load_dotenv
from datetime import datetime
from Openai import OpenAI 
dotenv_path = "OPENAI_API_KEY.env"
load_dotenv(dotenv_path) 
api_key = os.getenv("OPENAI_API_KEY")
OpenAI.api_key = api_key
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment.")
client = OpenAI(api_key=api_key)
print(f"API Key loaded (starts with): {api_key[:4]}...")
with open("content.txt","r",encoding="utf-8") as file:
    context = file.read()
SYSTEM_PROMPT = (
    "Seja especialmente atento à linguagem\n"
    "Você é um assistente que só responde a perguntas com base no seguinte contexto.\n"
    "Seja breve e conciso. Sua única fonte de informação é o banco de dados e este prompt, nada mais.\n"
    "**PRIORIDADE MÁXIMA: SEMPRE responda no mesmo idioma da pergunta.**\n"
    "Se a pergunta estiver em inglês, você DEVE responder em inglês.\n"
    "Se for solicitado um número de telefone, responda no idioma do usuário que ele deve verificar o site.\n"
    "Se uma pergunta não estiver relacionada ao contexto, responda no idioma do usuário o equivalente a que 'você não pode responder a esse tipo de pergunta.'\n"
    "Preste atenção ao tempo: Se uma data mencionada no contexto já tiver passado, refira-se a ela no pretérito.\n"
    f"A data é {datetime.now().strftime('%Y-%m-%d')}.\n" 
    "\n"
    f"Contexto:\n{context}"
)
def get_bot_response(user_query):
    print("202")
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_query}
            ],
            max_tokens=200,
            temperature=0.1
        )
        print("200")
        return response.choices[0].message.content.strip()     
    except Exception as e:
        print(f"OpenAI API Error: {e}")
        return "Sorry, I ran into an error trying to process your request."
