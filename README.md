# DeepSeek RAG POC

## Como usar
1. Coloque seus PDFs em `data/pdfs/`
2. Execute na ordem:
   - `scripts/01_extrair_texto.py`
   - `scripts/02_gerar_embeddings.py`
   - `scripts/03_indexar_faiss.py`
   - `scripts/04_consultar_rag.py` para testar manualmente
   - `scripts/05_rodar_batch_perguntas.py` para gerar CSV com respostas em lote
