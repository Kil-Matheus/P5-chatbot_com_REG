import gradio as gr
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableLambda, RunnablePassthrough
from langchain.document_loaders import TextLoader
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from dotenv import load_dotenv

load_dotenv()

# load the document and split it into chunks
loader = TextLoader("./data/items.txt")  # Verifique o caminho do arquivo
documents = loader.load()

# split it into chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

# create the open-source embedding function
embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# load it into Chroma
vectorstore = Chroma.from_documents(docs, embedding_function)

retriever = vectorstore.as_retriever()

template = """
Se apresente como um especialista na área de segurança e professor de uma oficina metalurgica.
{context}
"""
prompt = ChatPromptTemplate.from_template(template)

# Certifique-se de configurar a chave da API OpenAI no ambiente
llm = OpenAI(model="gpt-3.5-turbo-instruct", max_tokens=512)

chain = (
    {"context": retriever}
    | prompt
    | llm
)

# Crie uma função que aceite uma entrada de texto e retorne uma resposta
def openai_response(prompt, history):
    response = ""
    for chunk in chain.stream(prompt):
        response += chunk
    return response

demo = gr.ChatInterface(openai_response)

demo.launch()

