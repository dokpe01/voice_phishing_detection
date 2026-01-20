import json
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

def get_summary_from_json(file_path, question):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        # segments 리스트 안의 모든 text를 하나로 합침
        full_text = " ".join([seg["text"] for seg in data.get("segments", [])])
        if not full_text:
            return {"category": "데이터 없음", "summary": "텍스트 데이터가 비어있습니다."}
            
    except Exception as e:
        return {"category": "에러", "summary": f"파일 로드 실패: {e}"}
    
    # 2. 모델 설정 (gpt-4o-mini가 현재 가장 빠릅니다)
    llm = ChatOpenAI(model="gpt-4o-mini-2024-07-18", temperature=0)

    # 3. 프롬프트 및 파서 설정
    parser = JsonOutputParser()
    prompt = ChatPromptTemplate.from_messages([
        ("system", "너는 보이스피싱 분류 전문가야. 반드시 JSON 형식으로만 응답해."),
        ("user", """
        다음은 내부 시스템에서 가져온 데이터입니다:
        {context}
        
        질문: {question}
        
        응답 형식:
        {{
            "category": "분류 결과",
            "summary": "부드러운 말투의 요약 내용"
        }}
        """)
    ])

    # 4. 체인 실행
    chain = prompt | llm | parser
    return chain.invoke({"context": full_text, "question": question})

if __name__ == "__main__":
    # 데이터가 담긴 JSON 파일 경로
    json_path = "voice_phising/data/2번_3차례 신고된 여성 전화금융사기범 (음성_2).json" 
    question = "['기관사칭','투자사기','채용빙자','납치협박','가족,지인사칭'] 중에서 카테고리를 분류하고 핵심내용을 자세하게 요약해서 부드러운 말투로 알려줘"
    
    result = get_summary_from_json(json_path, question)
    
    print(f"📌 분류 결과: {result.get('category')}")
    print(f"📝 요약 결과: {result.get('summary')}")