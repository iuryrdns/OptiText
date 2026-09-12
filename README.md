# OptiText

OCR treinado do zero para reconhecer texto em documentos escaneados/impressos — da arquitetura ao treinamento, sem depender de bibliotecas prontas como Tesseract ou EasyOCR.

* [GitHub](https://github.com/iuryrdns/OptiText/)
* Autor: [Iury Ruan do N. Santos](https://github.com/iuryrdns)
* MIT License

## Status do projeto

**Em desenvolvimento.** A etapa atual é o pipeline de pré-processamento de imagem; o modelo de reconhecimento de texto (deep learning) é o próximo passo.

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

Planejado:
- Arquitetura de deep learning para reconhecimento de texto, treinada do zero
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