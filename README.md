# Conversão de PDF para Markdown e Extração de Tabelas com Docling

Este projeto Python demonstra como usar a biblioteca `Docling` para processar arquivos PDF. Ele abrange a conversão de um PDF para o formato Markdown, preservando a estrutura do documento, e a extração programática de tabelas, transformando-as em DataFrames do Pandas para análise de dados.

## Visão Geral

A extração de informações estruturadas de PDFs pode ser um desafio, mas ferramentas como o Docling simplificam esse processo. Este script é útil para:
1.  **Conversão de Documentos:** Transformar PDFs em um formato de texto mais legível e editável como Markdown.
2.  **Extração de Dados de Tabelas:** Obter dados de tabelas dentro de PDFs, o que é crucial para análise de dados e automação.

O projeto realiza os seguintes passos:
1.  Define a URL de um arquivo PDF (neste caso, um artigo científico do arXiv).
2.  Utiliza `DocumentConverter` do Docling para processar o PDF.
3.  Exporta o conteúdo completo do documento para um arquivo Markdown.
4.  Itera pelas tabelas detectadas no documento e exporta a primeira tabela para um DataFrame do Pandas, imprimindo-o no console.

## Estrutura do Projeto

* `pdf_test.py`: O script Python principal que executa a conversão e extração.
* `pdf_test.md`: O arquivo Markdown de saída gerado pelo script.

## Tecnologias Utilizadas

* **Python 3**
* **`docling`**: A biblioteca principal para conversão e extração de documentos.
    * `Docling Document Converter`: Uma biblioteca externa que precisa ser instalada.
* **`pandas`**: Para manipular as tabelas extraídas como DataFrames.
* **`requests`**: (Indiretamente, para o Docling acessar URLs, embora não explícito no snippet fornecido, o Docling pode precisar) Para fazer requisições HTTP se a fonte for uma URL.

## Pré-requisitos

1.  **Instale a biblioteca `Docling`:** Para instalar a biblioteca `Docling`, você pode precisar de um token de acesso ou seguir as instruções de instalação específicas fornecidas pelo Docling. Geralmente, seria algo como:
    ```bash
    pip install docling-sdk
    # Ou siga as instruções no site oficial do Docling para instalação.
    ```

## Saída Esperada

Ao executar o script:
* Um arquivo `pdf_test.md` será criado no diretório do projeto, contendo o conteúdo do PDF formatado em Markdown.
* A primeira tabela encontrada no PDF será impressa no console como um DataFrame do Pandas.

## Configuração

* **`source`**: Você pode alterar a URL do PDF na variável `source` no arquivo `pdf_test.py` para qualquer outro documento PDF que deseje processar.
* **Extração de Múltiplas Tabelas**: O loop `for idx, table in enumerate(result.document.tables):` inclui um `break` após a primeira tabela. Para extrair e imprimir todas as tabelas, basta remover a linha `break`.
