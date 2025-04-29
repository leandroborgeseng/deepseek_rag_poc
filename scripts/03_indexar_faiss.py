
import pickle
import faiss
import numpy as np

with open('index/embeddings.pkl', 'rb') as f:
    conteudos, embeddings = pickle.load(f)

embeddings = np.array(embeddings)
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

faiss.write_index(index, 'index/faiss_index.bin')
