# ProjetoProgramacoPython – Interface de Cadastro em Python

##  Visão Geral  
Este projeto implementa uma interface de cadastro em Python, composta por uma aplicação modular que permite registrar e gerenciar entidades (clientes, produtos, etc) em uma solução simulada. O objetivo é demonstrar competências em programação orientada a objetos, modularização, tratamento de dados e preparar o terreno para práticas de qualidade de software como testes, automação e revisão de código.

##  Objetivos  
- Criar uma interface funcional em Python para cadastro e gerenciamento de dados.  
- Estruturar o código usando boas práticas: modularização, classes, organizações de arquivos.  
- Preparar a base para evoluir para automação de testes, análise estática de código e garantia de qualidade.  
- Demonstrar capacidade de adaptação a novos papéis como QA/Quality Analyst, aproveitando experiência em infra/devops.

## 🔧 Estrutura do Projeto
/ProjetoProgramacaoPython
│
├─ cadastro.py # módulo principal da interface de cadastro
├─ modules/ # pacotes para lógica de negócio (opcional)
│ ├─ init.py
│ ├─ entity.py # definição de classes de entidade
│ └─ storage.py # persistência ou manipulação de dados
├─ tests/ # pasta para futuros testes automatizados
│ └─ test_cadastro.py
├─ docs/ # (opcional) documentação, diagramas, casos de uso
└─ README.md # este arquivo

##  Tecnologias e Ferramentas  
- Linguagem: **Python 3.x**  
- Paradigma: Programação Orientada a Objetos (POO)  
- Boas práticas de código: modularização, clareza, legibilidade  
- Versionamento: **Git / GitHub**  
- Qualidade & automação (em evolução): test-framework (ex: Pytest), análise estática (ex: Flake8/Pylint), CI/CD (future)

##  Funcionalidades Implementadas  
- Interface de cadastro para entidades (ex: clientes) com entrada de dados, validação simples e armazenamento (em memória ou arquivo).  
- Uso de classes e métodos para encapsular lógica de cadastro.  
- Modularização básica (se aplicável) para separar lógica de armazenamento e de negócio.  
- Preparação para testes: pasta `tests/` criada como estrutura inicial.

##  Evolução para Qualidade de Software  
Para alinhar diretamente à função de Analista de Qualidade de Software, o plano inclui:  
1. **Implementar testes unitários** usando **Pytest** ou similar para verificar funcionalidades de cadastro, validação e storage.  
2. **Adicionar análise estática de código** (em linter, cobertura de teste, etc) para assegurar saúde do código-fonte.  
3. **Configurar pipeline de CI/CD** (ex: GitHub Actions ou Jenkins) que execute lint + testes a cada commit.  
4. **Documentar bugs / melhoria contínua** — demonstrando investigação, documentação de inconsistências e correção (uma atribuição da vaga).  
5. **Automatizar processo de publicação / versão** (mesmo que simulado) para demonstrar entendimento de “publicação de novas versões dos sistemas” da vaga.

## 🚀 Como Rodar  
```bash
# Clone este repositório  
git clone https://github.com/jvictor31/ProjetoProgram-oPython.git  
cd ProjetoProgram-oPython  

# (Recomendado) criar ambiente virtual  
python3 -m venv venv  
source venv/bin/activate  # Windows: venv\Scripts\activate  

# Instalar dependências, se houver  
pip install -r requirements.txt  

# Executar a aplicação  
python cadastro.py  
