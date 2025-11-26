# RAG Engine Quick Start Guide

## Installation

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

This will install:
- `sentence-transformers` - For embeddings
- `numpy` - For vector operations
- `PyPDF2` - For PDF parsing
- `torch` - PyTorch backend

2. **Verify knowledge base exists:**
```bash
ls knowledge_base/
# Should show: hr/ it/ finance/ security/ general/
```

## Starting the Application

1. **Start the server:**
```bash
uvicorn main:app --reload
```

2. **Watch the indexing process:**
```
🚀 Starting up application...
Initializing RAG Engine with model: sentence-transformers/all-MiniLM-L6-v2
✓ Loaded embedding model: sentence-transformers/all-MiniLM-L6-v2

Indexing knowledge base from: knowledge_base
  ✓ Indexed: hr/employee_handbook.pdf (4 chunks)
  ✓ Indexed: hr/leave_policy.pdf (4 chunks)
  ...
  
Generating embeddings for 1467 chunks...
✓ Embeddings generated: shape (1467, 384)

✅ Indexing complete: 1467 chunks from 92 documents

📊 RAG Engine Stats:
   Total chunks: 1467
   Total documents: 92
   Departments: {'hr': 167, 'it': 261, 'finance': 246, 'security': 324, 'general': 469}
   Embedding dimension: 384

✅ Application ready!
```

## Testing the RAG Engine

### Option 1: Use the Web Interface

1. Open browser: `http://localhost:8000`
2. Login with any user (e.g., `sysadmin` / `demo123`)
3. Ask questions like:
   - "How many days of annual leave do I get?"
   - "What is the password policy?"
   - "How do I submit expense reports?"

### Option 2: Use the Test Script

```bash
python test_rag.py
```

This will run automated tests and show:
- RAG statistics
- Sample queries with responses
- Context retrieval information

### Option 3: Use curl

```bash
# Get RAG stats
curl http://localhost:8000/api/rag/stats

# Test a query (streaming response)
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"query": "What is the leave policy?", "model": "llama3.1"}'
```

## How It Works

### 1. Document Indexing (Startup)
```
Knowledge Base → Parse PDFs/TXT → Split into Chunks → Generate Embeddings → In-Memory Index
```

### 2. Query Processing (Runtime)
```
User Query → Generate Embedding → Find Similar Chunks → Apply Filters → Build Prompt → LLM → Stream Response
```

### 3. Example Flow

**User asks:** "How many vacation days do I get?"

**RAG Engine:**
1. Generates embedding for query
2. Finds top 5 similar chunks:
   - `hr/leave_policy.pdf` (score: 0.87)
   - `hr/benefits_guide.pdf` (score: 0.72)
   - `hr/employee_handbook.pdf` (score: 0.68)
3. Builds enhanced prompt with context
4. Sends to Ollama

**LLM Response:**
"According to the leave policy, all full-time employees receive 20 days of paid annual leave per year..."

## Monitoring

### Check RAG Statistics
```bash
curl http://localhost:8000/api/rag/stats | jq
```

### View Query Logs
The server logs show:
```
📝 Query: How many vacation days do I get?
📚 Retrieved 5 context chunks
   1. hr/leave_policy.pdf (score: 0.872)
   2. hr/benefits_guide.pdf (score: 0.721)
   3. hr/employee_handbook.pdf (score: 0.683)
   4. hr/onboarding_guide.pdf (score: 0.654)
   5. general/new_joiner_faq.pdf (score: 0.612)
```

## Reloading the Index

If you add/modify documents in `knowledge_base/`:

```bash
curl -X POST http://localhost:8000/api/rag/reload
```

Or restart the server (with `--reload` flag, it auto-reloads on file changes).

## Common Issues

### Issue: "No indexed chunks available"
**Cause:** Knowledge base not found or empty
**Solution:** 
```bash
python init_kb.py  # Regenerate knowledge base
python convert_to_pdf.py  # Convert to PDFs
```

### Issue: Slow first query
**Cause:** Model loading on first use
**Solution:** This is normal - subsequent queries are fast

### Issue: Poor quality responses
**Cause:** Not enough relevant context retrieved
**Solution:**
- Increase `top_k` parameter (default: 5)
- Check if relevant documents exist in knowledge base
- Verify document content is properly indexed

### Issue: Out of memory
**Cause:** Large knowledge base
**Solution:**
- Use smaller embedding model
- Reduce number of documents
- Implement pagination/lazy loading

## Configuration

### Change Embedding Model

In `rag_engine.py`:
```python
rag_engine = RAGEngine(
    kb_root="knowledge_base",
    model_name="sentence-transformers/all-mpnet-base-v2"  # Larger, more accurate
)
```

Available models:
- `all-MiniLM-L6-v2` (default) - Fast, 384-dim
- `all-mpnet-base-v2` - More accurate, 768-dim
- `all-MiniLM-L12-v2` - Balanced, 384-dim

### Adjust Retrieval Parameters

In `main.py`:
```python
context_chunks = rag_engine.query(
    query_text=body.query,
    user_department="hr",  # Filter by department
    user_role="Manager",   # Role-based access
    top_k=10              # Return more chunks
)
```

### Modify Scoring Weights

In `rag_engine.py`, `query()` method:
```python
# Adjust semantic vs keyword balance
combined_scores = 0.9 * similarities + 0.1 * keyword_scores  # More semantic
# or
combined_scores = 0.7 * similarities + 0.3 * keyword_scores  # More keyword
```

## Next Steps

1. **Add Authentication**: Integrate with user auth system
2. **Implement RBAC**: Add role-based access control
3. **Add More Documents**: Expand knowledge base
4. **Fine-tune Retrieval**: Adjust scoring and filtering
5. **Add Monitoring**: Track query performance and accuracy

## Resources

- [Sentence Transformers Documentation](https://www.sbert.net/)
- [RAG Implementation Guide](./RAG_IMPLEMENTATION.md)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Ollama Documentation](https://ollama.ai/docs)

## Support

For issues or questions:
1. Check server logs for errors
2. Verify knowledge base is properly indexed
3. Test with simple queries first
4. Review RAG_IMPLEMENTATION.md for architecture details
