import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA

load_dotenv()

def get_rag_summary(query):
    # 1. 문서 로드 및 분할
    loader = TextLoader("data/memo.txt", encoding="utf-8")
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    splits = text_splitter.split_documents(docs)

    # 2. 벡터 스토어 생성 (임베딩 저장)
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(documents=splits, embedding=embeddings)

    # 3. 모델 설정 (GPT-5 출시 전이므로 4o 사용)
    llm = ChatOpenAI(model="gpt-5-mini", temperature=0)

    # 4. RetrievalQA 체인 구성 (요약용 프롬프트 포함)
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(),
        return_source_documents=True
    )

    # 5. 실행
    # 예: "이 문서의 주요 리스크 요인만 뽑아서 리포트로 만들어줘"
    result = qa_chain.invoke({"query": query})
    
    return result["result"], result["source_documents"]

# 사용 예시
if __name__ == "__main__":
    question = "문서 전체 내용을 요약해서 보여줘.내용 중에서 개인정보는 뻬줘"
    summary = get_rag_summary(question)
    
    print(f"--- [요약 결과] ---\n{summary}")




