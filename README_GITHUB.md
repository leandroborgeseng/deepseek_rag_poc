
# DeepSeek RAG PoC - Engenharia Clínica

Este projeto é uma Prova de Conceito (PoC) de um sistema de **RAG (Retrieval-Augmented Generation)** aplicado ao domínio de **Engenharia Clínica**, utilizando o modelo **DeepSeek-LLM 7B** para consultas técnicas baseadas em manuais e documentos regulatórios.

## Estrutura de Pastas

- `data/` — PDFs de manuais e textos extraídos.
- `index/` — Índice vetorizado (FAISS) para busca.
- `models/` — DeepSeek-LLM.
- `outputs/` — Respostas geradas automaticamente.
- `scripts/` — Scripts de processamento, extração, embeddings e consulta.

## Principais Scripts

| Script | Função |
|:---|:---|
| `01_extrair_texto.py` | Extrai texto de PDFs (OCR automático se necessário) |
| `02_gerar_embeddings.py` | Gera embeddings usando DeepSeek-Embedding |
| `03_indexar_faiss.py` | Indexa documentos em FAISS |
| `04_consultar_rag.py` | Perguntas manuais via DeepSeek RAG |
| `05_rodar_batch_perguntas.py` | Perguntas em lote e salvamento em CSV |

## Tecnologias Utilizadas

- **Python 3.10+**
- **PyTorch**
- **HuggingFace Transformers**
- **Sentence-Transformers**
- **FAISS (Facebook AI Similarity Search)**
- **LangChain**

## Instalação

```bash
# Crie um ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
```

## Como Executar

1. Coloque seus PDFs em `data/pdfs/`
2. Execute:
   - `scripts/01_extrair_texto.py`
   - `scripts/02_gerar_embeddings.py`
   - `scripts/03_indexar_faiss.py`
   - `scripts/04_consultar_rag.py` para testes manuais
   - `scripts/05_rodar_batch_perguntas.py` para perguntas em lote

## Licença

Projeto de caráter experimental e acadêmico.

---

🚀 Desenvolvido para PoC de especialização de IA em Engenharia Clínica utilizando DeepSeek.
