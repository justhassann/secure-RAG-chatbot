"""
Test script to demonstrate RAG engine functionality
"""

import requests
import json

API_BASE = "http://localhost:8000"

def test_rag_stats():
    """Test RAG stats endpoint"""
    print("=" * 60)
    print("Testing RAG Stats Endpoint")
    print("=" * 60)
    
    response = requests.get(f"{API_BASE}/api/rag/stats")
    stats = response.json()
    
    print(f"\n✓ Total chunks indexed: {stats['total_chunks']}")
    print(f"✓ Total documents: {stats['total_documents']}")
    print(f"✓ Embedding dimension: {stats['embedding_dimension']}")
    print(f"\n✓ Chunks by department:")
    for dept, count in stats['departments'].items():
        print(f"   - {dept}: {count} chunks")

def test_query(query_text):
    """Test a query through the chat endpoint"""
    print("\n" + "=" * 60)
    print(f"Testing Query: {query_text}")
    print("=" * 60)
    
    # Make request
    response = requests.post(
        f"{API_BASE}/api/chat",
        json={"query": query_text, "model": "llama3.1"},
        stream=True
    )
    
    print("\n📝 Response:")
    print("-" * 60)
    
    # Stream response
    full_response = ""
    for line in response.iter_lines():
        if line:
            line_str = line.decode('utf-8')
            if line_str.startswith('data: '):
                data = json.loads(line_str[6:])
                if 'content' in data:
                    content = data['content']
                    print(content, end='', flush=True)
                    full_response += content
                elif 'error' in data:
                    print(f"\n❌ Error: {data['error']}")
    
    print("\n" + "-" * 60)
    return full_response

if __name__ == "__main__":
    # Test RAG stats
    test_rag_stats()
    
    # Test queries
    print("\n\n")
    
    # Query 1: HR policy
    test_query("How many days of annual leave do employees get?")
    
    print("\n\n")
    
    # Query 2: IT security
    test_query("What is the password policy?")
    
    print("\n\n")
    
    # Query 3: Finance
    test_query("What are the expense reimbursement guidelines?")
    
    print("\n\n")
    
    # Query 4: Out of scope (should say no information)
    test_query("What is the weather like today?")
