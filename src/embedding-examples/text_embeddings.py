from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings


# Load environment variables from .env file
load_dotenv()

# Initialize the Google Generative AI Embeddings model, uses GOOGLE_API_KEY from .env file
embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2"
)

# Generate embeddings for a query text. This will return a vector representation of the input text.
embedding_values = embeddings.embed_query("Who is the god of Machine Learning?")

print(embedding_values)