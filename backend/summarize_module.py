import openai
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_text(text: str) -> str:
    if not text.strip():
        return "요약할 내용이 없습니다."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "다음 텍스트를 간결하게 요약해줘."},
                {"role": "user", "content": text}
            ],
            max_tokens=300,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"[ERROR] GPT 요약 실패: {e}")
        return "요약 중 오류가 발생했습니다."