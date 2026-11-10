import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

class UfpaNoRagEngine:
    def __init__(self):
        self.llm = ChatOllama(
            model=os.getenv("OLLAMA_MODEL", "qwen2.5:7b"),
            base_url=os.getenv("OLLAMA_HOST", "http://localhost:11434"),
            temperature=0.2,
        )

        # Prompt SEM RAG (só conversa)
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", "Você é um assistente útil. Responda de forma clara e objetiva."),
            ("user", "{pergunta}")
        ])

        self.chain = self.prompt | self.llm | StrOutputParser()

    def obter_resposta(self, pergunta: str) -> str:
        pergunta = (pergunta or "").strip()
        if not pergunta:
            return "Envie uma pergunta."
        return self.chain.invoke({"pergunta": pergunta})

# O app.py espera exatamente isso:
rag_instance = UfpaNoRagEngine()