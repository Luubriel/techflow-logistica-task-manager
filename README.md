# TechFlow Tasks

TechFlow Tasks é uma aplicação web de gerenciamento de tarefas simples e eficiente, desenvolvida com Django. O projeto foca na organização pessoal, permitindo que usuários se cadastrem e gerenciem suas próprias listas de afazeres com segurança e privacidade.

## 🎯 Objetivo

O objetivo principal deste projeto foi desenvolver um sistema robusto de *To-Do List* utilizando o framework Django, aplicando boas práticas de desenvolvimento web, como arquitetura MTV (Model-Template-View), autenticação segura e uma interface de usuário responsiva e intuitiva.

## 📋 Escopo do Projeto

### Escopo Inicial
O projeto foi inicialmente concebido para atender aos seguintes requisitos funcionais básicos:
* **Autenticação de Usuários:** Sistema de Login, Logout e proteção de rotas.
* **Gerenciamento de Tarefas (CRUD):** Criar, Ler (listar), Atualizar e Deletar tarefas.
* **Isolamento de Dados:** Cada usuário deve visualizar e manipular apenas as tarefas que ele mesmo criou.
* **Atributos da Tarefa:** Título, Descrição e Status (Pendente/Concluída).

### 🔄 Mudança de Escopo: Priorização de Tarefas
Durante o ciclo de desenvolvimento, foi identificada a necessidade de melhorar a organização visual das tarefas.

* **Alteração:** Inclusão de um sistema de **Prioridades** (Alta, Média, Baixa).
* **Justificativa:** Apenas listar as tarefas por ordem de criação ou status não era suficiente para usuários com alto volume de atividades. A adição da prioridade permite que o usuário foque primeiro no que é mais urgente, aumentando a eficácia da ferramenta como um utilitário de produtividade diária.
* **Impacto na Implementação:**
    * Alteração do Modelo de dados (`Task`) para incluir o campo `priority`.
    * Atualização das Views para ordenar a lista não apenas por status, mas também por prioridade (Alta > Média > Baixa).
    * Adaptação da interface para exibir "badges" visuais indicando o nível de urgência.

## 🛠️ Metodologia e Tecnologias

O projeto seguiu uma metodologia ágil iterativa, onde as funcionalidades foram implementadas e refinadas em ciclos.

* **Backend:** Python 3 & Django 5.
* **Gerenciador de Dependências:** Poetry.
* **Frontend:** HTML5, CSS3 e Bootstrap 5 para estilização responsiva e componentes de interface (Cards, Modais, Badges).
* **Banco de Dados:** SQLite (para ambiente de desenvolvimento e testes).
* **Arquitetura:** Django MTV (Model-Template-View), com uso extensivo de *Class-Based Views*.

## 🚀 Instruções de Execução

Siga os passos abaixo para rodar o projeto localmente em sua máquina.

### Pré-requisitos
* Python 3.10 ou superior.
* Git.
* **Poetry** instalado (veja como instalar na [documentação oficial](https://python-poetry.org/docs/#installation)).

### Passo a Passo

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/Luubriel/techflow-logistica-task-manager.git
    cd techflow-logistica-task-manager
    ```

2.  **Instale as dependências com Poetry:**
    O Poetry criará automaticamente o ambiente virtual e instalará todas as bibliotecas necessárias.
    ```bash
    poetry install
    ```

3.  **Ative o ambiente virtual:**
    ```bash
    poetry shell
    ```

4.  **Aplique as migrações ao banco de dados:**
    ```bash
    python manage.py migrate
    ```

5.  **Crie um superusuário (opcional, para acessar o /admin):**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Execute o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

7.  **Acesse a aplicação:**
    Abra seu navegador e vá para `http://127.0.0.1:8000/`.

---
*Desenvolvido como parte de um projeto prático de Django.*