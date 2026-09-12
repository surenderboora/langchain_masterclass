from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path="data/NIFTY 50-12-09-2025-to-12-09-2026.csv", encoding="utf-8")

data = loader.load()

print(f"Loaded {len(data)} rows(documents) from the CSV file.")
print("Sample row(document) content:")
for doc in data[:3]:  # Print content of first 3 documents
    print(doc.page_content)

