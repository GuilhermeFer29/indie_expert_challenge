# indie_expert_challenge
 
# Dashboard de Análise Comercial (CRM)

Este repositório contém o código para o desenvolvimento de um **dashboard interativo** que realiza a análise descritiva e diagnóstica de dados comerciais, com o objetivo de fornecer insights claros e objetivos para gestores. O projeto utiliza ferramentas em Python como **Streamlit**, **Plotly**, **pandas** e **seaborn**.

---

## 📊 **Objetivo do Projeto**

O objetivo é criar um dashboard intuitivo e interativo que permita:
1. **Análise de desempenho de vendas**: Acompanhamento do desempenho de vendedores e comparação com as metas estabelecidas.
2. **Facilidade na tomada de decisão**: Fornecer informações relevantes para o gestor sem a necessidade de navegações excessivas (foco no conceito "Zero Click").
3. **Interatividade**: Apresentar visualizações dinâmicas e responsivas para uma experiência de usuário fluida.

---

## 🔧 **Funcionalidades**
- **KPIs principais**: Total de vendas, média de vendas por vendedor e outros indicadores relevantes.
- **Gráficos interativos**: Gráficos de barras e pizza que destacam o desempenho de cada vendedor.
- **Tabela com gradiente de cores**: Facilita a identificação visual de bons e maus desempenhos.
- **Destaque de metas**: Indica se os vendedores estão acima ou abaixo das metas estabelecidas.

---

## 🛠️ **Tecnologias Utilizadas**

As seguintes bibliotecas em Python foram utilizadas:

### Manipulação e Modelagem de Dados
- **[pandas](https://pandas.pydata.org/)**: Para manipulação de dados tabulares.

### Visualização de Dados
- **[Plotly](https://plotly.com/python/)**: Para criar gráficos interativos e responsivos.
- **[Seaborn](https://seaborn.pydata.org/)**: Para aplicação de esquemas de cores e estilização de tabelas.

### Desenvolvimento de Dashboard
- **[Streamlit](https://streamlit.io/)**: Framework para criação de dashboards de forma simples e rápida.

---

## 🔬 **Dados de Exemplo**

O projeto utiliza dados em .xlsx para demonstração:
```plaintext
Vendedor  | Vendas  | Meta  | Status
Ana       | 30000   | 25000 | Acima da Meta
Bruno     | 20000   | 25000 | Abaixo da Meta
Carla     | 40000   | 25000 | Acima da Meta
Daniel    | 15000   | 25000 | Abaixo da Meta
Eduarda   | 35000   | 25000 | Acima da Meta
```

---

## 📄 **Como Executar**

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/dashboard-crm.git
cd dashboard-crm
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
streamlit run dashboard.py
```
O dashboard estará disponível em seu navegador no endereço: `http://localhost:8501`

---

## 🌟 **Demonstração do Dashboard**

### KPIs Principais
- Total de vendas
- Média de vendas

### Gráfico de Barras
Exibe o desempenho de vendas de cada vendedor com destaque de metas atingidas.

### Gráfico de Pizza
Mostra a distribuição de desempenho em "Acima da Meta" e "Abaixo da Meta".

### Tabela de Detalhes
Lista os dados de cada vendedor com um gradiente visual indicando o desempenho.

---

## 🔧 **Customização**
Caso você queira adaptar o dashboard:
- **Adicionar novos KPIs**: Edite o código no arquivo `dashboard.py`.
- **Alterar as metas**: Atualize os valores no DataFrame principal.
- **Adicionar novas visualizações**: Use bibliotecas como `matplotlib`, `plotly`, ou outras suportadas pelo Streamlit.

---

## 🚀 **Próximos Passos**
- Implementar integração com bases de dados reais (e.g., SQL ou APIs).
- Adicionar novos filtros para análise segmentada (e.g., por região ou produto).
- Implementar alertas automáticos para desempenho abaixo da meta.

---

## 📚 **Licença**
Este projeto está licenciado sob a [MIT License](LICENSE).

