from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generuj_pomysly(temat):
    prompt = f'Podaj 5 ciekawych tematów na bloga związanych z:{temat}'

    response = client.chat.completions.create(
        model="gpt-4o",  # Możesz użyć "gpt-3.5-turbo" lub innego dostępnego modelu
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content if response.choices else "Brak propozycji."

if __name__ == "__main__":
    temat_bloga = input("Podaj tematykę bloga: ")
    pomysly = generuj_pomysly(temat_bloga)
    print("\n Oto propozycje tematów na bloga:")
    print(pomysly)

    