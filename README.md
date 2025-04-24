# sllmproject2025

CPU 기반 Gemma-3-4B-IT 모델 실행 프로젝트
개요
이 프로젝트는 GPU(그래픽 카드)를 전혀 사용하지 않고 CPU만을 활용하여 성능이 뛰어난 시스템을 구현하는 것을 목표로 합니다. 속도는 느릴 수 있으나, 자원 효율성을 극대화하여 높은 성능을 달성합니다. 특히, NVIDIA GPU 4070의 12GB를 초과하는 32GB 메모리를 갖춘 CPU를 최대한 활용합니다.
모델 정보

모델: google/gemma-3-4b-it
메모리 요구사항: FP16 또는 bfloat16 설정에서 약 20GB RAM 필요
특징: 4B 파라미터, 멀티모달(텍스트+이미지), 128k 토큰 컨텍스트, 한국어 처리 지원

목표

CPU 메모리 자원을 효율적으로 관리하여 gemma-3-4b-it 모델을 안정적으로 실행.
32GB CPU 메모리를 활용해 메모리 최적화 기법(예: bfloat16, torch.no_grad) 적용.
한국어 텍스트 생성 등 작업에서 높은 성능 달성.

환경 설정

라이브러리:
transformers (4.50.0 이상)
torch (CPU 지원 버전)


설치 명령어:pip install --upgrade transformers torch


Hugging Face 인증:
모델 접근을 위해 Hugging Face 토큰 설정 및 약관 동의 필요.
토큰 설정 예시:export HF_TOKEN="your_token_here"





실행 예시
아래는 CPU에서 gemma-3-4b-it 모델을 실행하는 샘플 코드입니다:
import torch
from transformers import AutoProcessor, Gemma3ForConditionalGeneration
import os

# Hugging Face 토큰 설정
os.environ['HF_TOKEN'] = "your_token_here"


# 입력 텍스트
input_text = "너에 대해서 설명해 줄래?"
messages = [
    {"role": "user", "content": [{"type": "text", "text": input_text}]}
]

# 채팅 템플릿 적용
inputs = processor.apply_chat_template(messages, return_tensors="pt").to("cpu")

# 출력 생성
with torch.no_grad():
    outputs = model.generate(**inputs, max_new_tokens=512)
print(processor.decode(outputs[0], skip_special_tokens=True))

메모리 최적화

bfloat16: 메모리 사용량을 줄여 32GB 내에서 모델 실행.
torch.no_grad(): 추론 시 메모리 효율성 향상.
CPU 전용 설정: device_map="cpu"로 GPU 의존성 제거.

참고

모델 문서: Hugging Face Gemma 3
Transformers 가이드: Hugging Face Transformers
메모리 요구사항: FP16/bfloat16에서 약 20GB RAM 필요, 32GB CPU 메모리로 충분.


