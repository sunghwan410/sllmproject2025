import os
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import uvicorn

# Hugging Face 토큰 설정
os.environ['HF_TOKEN'] = ""

# FastAPI 앱 초기화
app = FastAPI()

# 정적 파일 디렉토리와 템플릿 디렉토리 확인 및 생성
os.makedirs("templates", exist_ok=True)

# 정적 파일 마운트
templates = Jinja2Templates(directory="templates")

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 개발 중에는 모든 origin 허용
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 모델을 Hugging Face에서 직접 로드
tokenizer = AutoTokenizer.from_pretrained("google/gemma-3-4b-it")
model = AutoModelForCausalLM.from_pretrained("google/gemma-3-4b-it")

# 요청 모델 정의
class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate")
async def generate_text(request: PromptRequest):
    try:
        input_text = request.prompt
        input_ids = tokenizer(input_text, return_tensors="pt")
        outputs = model.generate(**input_ids, max_length=512)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return {"response": response}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)