import os

VECTOR_STORE_BASE = r"vector_stores\Machine_Learning_Notes[1]"  # change to your real path

if not os.path.exists(VECTOR_STORE_BASE):
    print(f"❌ Path not found: {VECTOR_STORE_BASE}")
else:
    print(f"✅ Found vector store path: {VECTOR_STORE_BASE}")
