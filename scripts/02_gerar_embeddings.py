
import os
import pickle
from sentence_transformers import SentenceTransformer

modelo = SentenceTransformer('deepseek-ai/deepseek-embedding-1.3b')
pasta_textos = 'data/textos/'
embeddings = []
conteudos = []

for arquivo in os.listdir(pasta_textos):
    if arquivo.endswith('.txt'):
        with open(os.path.join(pasta_textos, arquivo), 'r', encoding='utf-8') as f:
            conteudo = f.read()
        conteudos.append(conteudo)
        embeddings.append(modelo.encode(conteudo))

with open('index/embeddings.pkl', 'wb') as f:
    pickle.dump((conteudos, embeddings), f)
