# backend/app.py

import whisper
import os
from summarize_module import summarize_text

# 1. Whisper 모델 로드
print("🔄 Whisper 모델 로딩 중...")
try:
    model = whisper.load_model("base")
    print("✅ 모델 로드 성공!")
except Exception as e:
    print("❌ 모델 로드 실패:", e)
    exit(1)

# 2. 오디오 경로 확인
audio_path = os.path.abspath("backend/audio_sample.mp3")  # 경로 정확히 확인
print("📁 오디오 경로:", audio_path)

if not os.path.isfile(audio_path):
    print(f"❌ 파일이 존재하지 않습니다: {audio_path}")
    exit(1)

# 3. 음성 → 텍스트
try:
    print("🎧 음성 인식 중...")
    result = model.transcribe(audio_path)
    transcribed_text = result["text"]
    print("📝 인식된 텍스트:\n", transcribed_text)

except Exception as e:
    print("❌ 음성 인식 중 오류:", e)
    exit(1)

# 4. GPT 요약
print("✂️ GPT 요약 중...")
summary = summarize_text(transcribed_text)
print("📌 요약 결과:\n", summary)