# Whisper (STT)
# v.1.1.0

import whisper
import os

try:
    # 모델 로드
    print("🔄 Whisper 모델 로딩 중...")
    model = whisper.load_model("base")
    print("✅ 모델 로드 성공!")
except Exception as e:
    print("❌ 모델 로드 실패:", e)
    exit(1)
    
audio_path = os.path.abspath("audio_sample.mp3")  # 자동으로 절대경로 변환
print("📁 오디오 경로:", audio_path)

# 파일 존재 확인
if not os.path.isfile(audio_path):
    print(f"❌ 파일이 존재하지 않습니다: {audio_path}")
    exit(1)

try:
    # 오디오 → 텍스트 변환
    print("🎧 음성 인식 중...")
    result = model.transcribe(audio_path)

    # 결과 출력
    print("🎤 인식된 텍스트:")
    print(result["text"])

except Exception as e:
    print("❌ 음성 인식 중 오류 발생:", e)