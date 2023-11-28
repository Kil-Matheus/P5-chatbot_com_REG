# P5-chatbot_com_REG

# Documentação do Código

Este script utiliza a biblioteca Gradio para criar uma interface de chat que interage com o modelo de linguagem GPT-3.5-turbo da OpenAI. O contexto do modelo é alimentado com informações provenientes de um arquivo de texto chamado "items.txt". O código está estruturado para apresentar um especialista em segurança e professor de uma oficina metalúrgica, respondendo a perguntas ou interagindo em um cenário específico.

## Dependências
- [Gradio](https://www.gradio.app/)
- [langchain](https://github.com/as-ideas/langchain): Um conjunto de ferramentas para encadear modelos de linguagem
- [SentenceTransformer](https://www.sbert.net/): Uma biblioteca para obtenção de embeddings de sentenças
- [dotenv](https://github.com/theskumar/python-dotenv): Carrega variáveis de ambiente a partir de um arquivo chamado `.env`

## Arquivo de Contexto
O conteúdo do arquivo "items.txt" serve como contexto para o modelo de linguagem. Este arquivo deve conter informações relevantes para o especialista em segurança e professor de uma oficina metalúrgica, e é carregado usando o `TextLoader`.

## Fluxo de Execução
1. **Carregar Documentos e Dividir em Chunks:**
   - O script carrega o conteúdo do arquivo "items.txt" usando `TextLoader`.
   - Em seguida, utiliza `CharacterTextSplitter` para dividir o documento em pedaços menores (chunks) de texto.

2. **Criar Função de Embedding:**
   - Utiliza `SentenceTransformerEmbeddings` para criar uma função de embedding baseada no modelo "all-MiniLM-L6-v2".
   - O resultado é carregado em um vetor de documentos usando `Chroma`.

3. **Configurar o Modelo de Recuperação (Retriever):**
   - O vetor de documentos é convertido em um objeto retriever para facilitar a recuperação de contexto.

4. **Definir o Template de Prompt:**
   - Um template de prompt é definido usando `ChatPromptTemplate`. O template inclui um espaço reservado `{context}` que será preenchido com informações do retriever.

5. **Configurar o Modelo de Linguagem:**
   - Utiliza `OpenAI` para configurar o modelo de linguagem GPT-3.5-turbo-instruct.

6. **Construir a Cadeia de Processamento (Chain):**
   - A cadeia de processamento (`chain`) é definida, conectando o retriever, o prompt e o modelo de linguagem.

7. **Função de Resposta do OpenAI:**
   - Define uma função `openai_response` que aceita uma entrada de texto e retorna uma resposta.
   - A função utiliza a cadeia de processamento para gerar a resposta.

8. **Interface de Chat com Gradio:**
   - Uma interface de chat é criada usando `gr.ChatInterface`, que utiliza a função `openai_response` para gerar respostas.

9. **Iniciar a Interface de Chat:**
   - A interface de chat é iniciada com `demo.launch()`.

## Execução
Certifique-se de ter as dependências instaladas e o arquivo "items.txt" presente no caminho especificado. Além disso, é necessário configurar a chave da API OpenAI no ambiente. Após a configuração, execute o script para iniciar a interface de chat interativa.

**Observação:** Certifique-se de revisar e entender as políticas e termos de serviço da OpenAI ao utilizar a API.

# Rodar o Código

```python
python3 app.py
```
## Desconsidere
O arquivo exemplo.py é um exemplo fornecido nas intruções de programação. O arquivo app.py é o código que foi desenvolvido para o projeto.

# Link do Vídeo

link: https://drive.google.com/file/d/1N0Dnkh8MFdTlPhZQN04nVMiPYx3MK1If/view?usp=sharing