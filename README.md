# 📦sllmproject2025
🚀 CPU 기반 Gemma-3-4B-IT 모델 실행 프로젝트


<div align="center">
  <br>
</div>
<div align=center>
  <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi">
  <br>
  <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
  <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white">
  <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">
  <br>
  <img src="https://img.shields.io/badge/pytorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white">
  <img src="https://img.shields.io/badge/transformers-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black">
  <br><br>
</div>

---
## 1. 프로젝트 개요
본 프로젝트는 GPU 없이 CPU만 활용하여,
고성능 자연어 처리 모델인 Gemma-3-4B-IT를 구동하는 것을 목표로 합니다.

속도는 상대적으로 느릴 수 있으나,
32GB CPU 메모리를 최적 활용하여 자원 효율성과 안정성을 극대화합니다.

참고

비교용: NVIDIA 4070 GPU (12GB 메모리)

본 프로젝트: 32GB 시스템 메모리 활용

---
## 2. 모델 정보

항목	설명
모델명	google/gemma-3-4b-it
모델 특징	- 4B 파라미터
- 멀티모달 (텍스트 + 이미지)
- 최대 128k 토큰 컨텍스트 지원
- 한국어 자연어 처리 가능
메모리 요구사항	약 20GB RAM 필요 (FP16 또는 bfloat16 설정 시)

---

## 3. 프로젝트 목표
CPU 환경에서 Gemma-3-4B-IT 모델을 안정적으로 실행합니다.

32GB 시스템 메모리를 활용하여 메모리 최적화 기술을 적용합니다:

bfloat16 데이터 타입 사용

torch.no_grad()로 추론 시 메모리 절약

한국어 텍스트 생성 등 자연어 작업에서 실질적 높은 품질을 목표로 합니다.

---

## 4. 실행 결과 예시
아래는 CPU에서 Gemma-3-4B-IT 모델을 구동하여
"이순신 장군이 누구야"를 질문한 결과 화면입니다:

<p align="center"> <a href="https://ifh.cc/v-FdJaQC" target="_blank"> <img src="https://ifh.cc/g/FdJaQC.jpg" alt="Gemma 채팅 결과" border="0"> </a> </p>
모델은 이순신 장군의 생애, 업적, 리더십을 체계적으로 설명해 주었습니다.

한국어로 자연스럽고 구체적인 답변을 생성하는 것을 확인할 수 있습니다.

복잡한 긴 답변도 CPU 기반 메모리 최적화 설정으로 충분히 처리되었습니다.

---

## 5. 주의사항
속도는 GPU 대비 느릴 수 있으며,
실시간 응답이 필요한 서비스용에는 적합하지 않을 수 있습니다.

메모리 요구사항을 초과하지 않도록,
입력 토큰 길이와 출력 토큰 수를 적절히 조정해야 합니다.

🚀 최종 정리
✅ GPU 없이 CPU로 4B 모델 실행
✅ 32GB RAM으로 안정적 구동 가능
✅ 한국어 생성 및 텍스트 작업 지원
✅ 답변은 느릴 수 있으나, 최상의 답변 품질 보장

