# OptiText

OCR para reconhecer texto em documentos escaneados/impressos. Usa Tesseract nesta fase inicial, com plano de evoluir para um modelo de deep learning treinado do zero.

* [GitHub](https://github.com/iuryrdns/OptiText/)
* Autor: [Iury Ruan do N. Santos](https://github.com/iuryrdns)
* MIT License

## Status do projeto

🚧 **Em desenvolvimento.** Reconhecimento de texto via Tesseract nesta fase; um modelo de deep learning treinado do zero é o objetivo de longo prazo.

## Features

Implementado:
- Pipeline de pré-processamento de imagem para documentos escaneados:
  - Conversão para escala de cinza
  - Binarização
  - Remoção de ruído
  - Dilatação e erosão morfológica
  - Inversão de imagem
- CLI (`optitext`) para rodar o pipeline
- Notebook de experimentação (`app.ipynb`)

- Leitura de imagem via OpenCV e reconhecimento de texto via Tesseract (etapa inicial)

Planejado:
- Arquitetura de deep learning para reconhecimento de texto, treinada do zero (substituindo o Tesseract)
- Pipeline de treinamento e avaliação
- Dataset de treino/validação para documentos escaneados/impressos

## Instalação

Ainda não publicado no PyPI. Para rodar localmente:

```bash
git clone https://github.com/iuryrdns/OptiText.git
cd OptiText
uv sync
```

## Uso

```python
import optitext
```

*(interface em definição conforme o pipeline evolui)*

## Documentação

Documentação completa (em construção) disponível em [GitHub Pages](https://iuryrdns.github.io/OptiText/).

## Contribuindo

Veja [CONTRIBUTING.md](CONTRIBUTING.md) para setup de desenvolvimento, testes e instruções de documentação.

---

Construído com [Cookiecutter](https://github.com/cookiecutter/cookiecutter) e o template [audreyfeldroy/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage).