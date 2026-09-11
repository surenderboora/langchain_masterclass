from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
load_dotenv()

llm = GoogleGenerativeAI(model="gemini-3.6-flash")

prompt = PromptTemplate(
    template="Explain me {topic} in easy language. List down the key points in bullet format.",
    input_variables=["topic"]
)

parser = StrOutputParser()

chain = prompt | llm | parser

result = chain.invoke({"topic": "System Design for Staff engineers"})
print(result)