from docling.document_converter import DocumentConverter
import pandas as pd

source="https://arxiv.org/pdf/2504.03277"

converter = DocumentConverter()
result = converter.convert(source)

with open("pdf_test.md", "w", encoding="utf-8") as f:
    f.write(result.document.export_to_markdown())

for idx, table in enumerate(result.document.tables):
    df = table.export_to_dataframe()
    print(f"Tabela {idx + 1}:")
    print(df)
    break