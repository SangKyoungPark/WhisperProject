import whisper
import os

# Whisper 모델 로드 (기본 모델: base)
model = whisper.load_model("base")

def transcribe_audio(file_path: str) -> str:
    """
    주어진 오디오 파일을 텍스트로 변환하여 반환합니다.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"파일이 존재하지 않습니다: {file_path}")

    print(f"[INFO] Whisper 처리 중: {file_path}")
    result = model.transcribe(file_path, language='ko')  # 한국어 인식 지정
    return result['text']