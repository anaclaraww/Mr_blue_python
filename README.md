## Mr. Blue - Python para Análise e Detecção de Garrafas Plásticas nos Oceanos 🌊 

Este repositório contém ferramentas e scripts Python para analisar e detectar garrafas plásticas nos oceanos. O objetivo principal é auxiliar na compreensão do impacto da poluição plástica no meio ambiente marinho e contribuir para o desenvolvimento de soluções para esse problema ambiental crítico.

**Estrutura do Repositório:**

* **data:**
    * **global-plastic-waste-emitted-to-the-ocean.csv:** Conjunto de dados contendo informações sobre a quantidade de plastico dispersada pelos países e continentes em 2019.
    * **plastic-top-20-rivers.csv:** Conjunto de dados contendo informações sobre a quantidade de plastico dispersada por alguns países e continentes em 2015.
* **notebooks:**
    * **data_analytics.ipynb:** Notebook Jupyter contendo análises exploratórias e visualizações dos dados presentes no arquivo `dados.csv`.
* **yolo_detection:**
    * **spp.py:** Script Python que utiliza o modelo YOLOv8 para detectar garrafas plásticas em imagens e gerar resultados em imagens.
 
```plaintext
.
├── runs
│   └── detect
│       └── [resultados dos predicts]
├── data
│   ├── global-plastic-waste-emitted-to-the-ocean.csv
│   └── plastic-top-20-rivers.csv
├── app.py
└── data_analytics.ipynb

```

**Requisitos:**

* Python 3.10
* Pandas
* Matplotlib
* Ultralitycs
* YOLOv8
* PIL

**Instruções de Uso:**

1. Clone o repositório:

```
git clone https://github.com/seu_usuario/repositorio_python.git
```

2. Instale as dependências:

```
pip install -r requirements.txt
```

3. Análise de dados:

   * Execute o notebook `data_analytics.ipynb` para realizar análises exploratórias e visualizações dos dados presentes no arquivo `dados.csv`.

4. Detecção de garrafas:

   * Execute o script `app.py` para detectar garrafas plásticas em imagens e gerar resultados na pasta runs/detect

**Observações:**
* O script `detectar_garrafas.py` permite a detecção de garrafas em imagens individuais. Para processar um conjunto de imagens, é necessário adaptar o script.
* Este repositório oferece uma base para o desenvolvimento de soluções para o problema da poluição plástica nos oceanos. É possível aprimorar as análises, treinar modelos mais precisos e integrar ferramentas de diferentes áreas para um trabalho mais abrangente.

## 🔗[Acesse o portfólio da ideia do projeto:](https://anaclaraww.github.io/mr_blue-client_side/)
