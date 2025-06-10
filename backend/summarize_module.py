import openai

# 발급받은 API 키를 여기에 입력
openai.api_key = "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"

def summarize_text(text: str) -> str:
    """
    주어진 텍스트를 GPT로 요약해서 반환합니다.
    """
    if not text.strip():
        return "요약할 내용이 없습니다."

    print("[INFO] GPT 요약 요청 중...")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # 또는 gpt-4 사용 가능
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