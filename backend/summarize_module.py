# summarize_module.py

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_text(text):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "당신은 친절한 요약 도우미입니다."},
                {"role": "user", "content": f"다음 내용을 요약해줘:\n{text}"}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"요약 실패: {e}"