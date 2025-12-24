import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

def get_summary(file_path):
    '''전달 받은 문서 내용을 요약하여 응답해주는 함수'''
    try:
        with open(file_path, 'r', encoding = "utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        return "파일을 찾을 수 없습니다"
    except Exception as e:
        return f"에러발생 : {e}"
    # 1.API 호출
    response = client.chat.completions.create(
        model = "gpt-4o-mini-2024-07-18", 
        messages =[{"role" : "system", "content" : "대화 내용을 중점으로 자세하게, 개인정보(이름,연락처,계좌번호와 같은..)는 없이 요약해줘"},
                   {"role" : "user", "content" : content[:3000]}], 
                   temperature = 0
    )
    return response.choices[0].message.content

file = "./data/memo.txt"
result = get_summary(file)
print(result)