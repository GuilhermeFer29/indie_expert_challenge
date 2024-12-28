# indie_expert_challenge
 
# Dashboard de Análise Comercial (CRM)

Este repositório contém o código para o desenvolvimento de um **dashboard** 
que realiza a análise descritiva e diagnóstica de dados comerciais, com o objetivo de fornecer insights claros e objetivos para gestores. O projeto utiliza ferramentas em Python como **Streamlit**, **Plotly** e **pandas** 

---

## 📊 **Objetivo do Projeto**

O objetivo é criar um dashboard intuitivo e interativo que permita:
1. **Análise de desempenho de vendas**: Acompanhamento do desempenho de vendedores e comparação com as metas estabelecidas.

2. **Facilidade na tomada de decisão**: Fornecer informações relevantes para o gestor sem a necessidade de navegações excessivas (foco no conceito "Zero Click").
3. **Interatividade**: Apresentar visualizações dinâmicas e responsivas para uma experiência de usuário fluida.

---

## 🔧 **Funcionalidades**
- **KPIs principais**: Total de vendas, média de vendas por vendedor .
- **Gráficos interativos**: Gráficos de barras e pizza que destacam o desempenho de cada vendedor.

- **Tabela com gradiente de cores**: Facilita a identificação visual de bons e maus desempenhos.


---

## 🛠️ **Tecnologias Utilizadas**

As seguintes bibliotecas em Python foram utilizadas:

### Manipulação e Modelagem de Dados
- **[pandas](https://pandas.pydata.org/)**: Para manipulação de dados tabulares.

### Visualização de Dados
- **[Plotly](https://plotly.com/python/)**: Para criar gráficos interativos e responsivos.

### Desenvolvimento de Dashboard
- **[Streamlit](https://streamlit.io/)**: Framework para criação de dashboards de forma simples e rápida.

---

## 🔬 **Dados de Exemplo**

O projeto utiliza dados em .csv para demonstração:


## 📄 **Como Executar**

### 1. Clone o repositório
```bash
git clone https://github.com/GuilhermeFer29/indie_expert_challenge.git
```

### 2. Instale as dependências
Recomenda-se o uso de um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Execute o dashboard
```bash
    streamlit run src/main.py

```
O dashboard estará disponível em seu navegador no endereço: 

https://indieexpertchallenge.streamlit.app/
---

## 🌟 **Demonstração do Dashboard**

### KPIs Principais
- Total de vendas
- Média de vendas

### Gráfico de Barras
Exibe o desempenho de vendas de cada vendedor.

### Gráfico de Pizza
Mostra a distribuição de desempenho de cada Vendedor.

## 📚 **Licença**
Este projeto está licenciado sob a [MIT License](LICENSE).

