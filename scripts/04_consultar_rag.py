
from transformers import AutoModelForCausalLM, AutoTokenizer
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle

# Carregamento do modelo DeepSeek LLM
modelo = AutoModelForCausalLM.from_pretrained('models/deepseek-llm-7b', torch_dtype='auto')
tokenizer = AutoTokenizer.from_pretrained('models/deepseek-llm-7b')

# Carregamento dos dados vetoriais
with open('index/embeddings.pkl', 'rb') as f:
    conteudos, embeddings = pickle.load(f)
index = faiss.read_index('index/faiss_index.bin')

def gerar_resposta(pergunta):
    modelo_emb = SentenceTransformer('deepseek-ai/deepseek-embedding-1.3b')
    embedding_pergunta = modelo_emb.encode(pergunta)
    D, I = index.search(np.array([embedding_pergunta]), k=5)
    contexto = "\n\n".join([conteudos[i] for i in I[0]])
    prompt = f"Com base nas informações a seguir, responda à pergunta: {pergunta}\n\n{contexto}\n\nResposta:"
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = modelo.generate(**inputs, max_new_tokens=300)
    resposta = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return resposta

def main():
    while True:
        pergunta = input("Digite sua pergunta (ou 'sair'): ")
        if pergunta.lower() == 'sair':
            break
        resposta = gerar_resposta(pergunta)
        print("\nResposta gerada:\n", resposta)

if __name__ == "__main__":
    main()
