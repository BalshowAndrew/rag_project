import time
import textwrap

import openai
from openai import OpenAI

from config import API_KEY

# openai.api_key = API_KEY
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY)

gptmodel = "tngtech/tng-r1t-chimera:free"
start_time = time.time()

def call_llm_with_full_text(itext):
    text_input = '\n'.join(itext)
    prompt = f"Pleese elaborate on the following content:\n{text_input}"
    try:
        response = client.chat.completions.create(
            model=gptmodel,
            messages=[
                {"role": "system", "content": "Вы являетесь экспертом в упражнениях по обработке естественного языка."},
                {"role": "assistant", "content": "1.Вы можете прочесть вводную информацию и дать подробный ответ на русском языке."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.1
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return str(e)


def print_formatted_response(response):
    wrapper = textwrap.TextWrapper(width=80)
    wrapped_text = wrapper.fill(text=response)
    print("Response:")
    print("--------------")
    print(wrapped_text)
    print("--------------\n")


print_formatted_response(call_llm_with_full_text("Как подготовить промпт для LLM?"))


# def main():
#     print("Hello from rag-studying!")

# if __name__ == "__main__":
#     main()
