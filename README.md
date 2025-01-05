# Inventory

Projeto backend com cadastro e visuzalização (lista e gráfico) de itens em um inventário.

## Requisitos

Antes de começar, você precisará de algumas ferramentas instaladas no seu sistema:

- [Python](https://www.python.org/downloads/) 
- [Git](https://git-scm.com/)
- 
## Passo a Passo para Inicialização

### 1. Clonar o Repositório

Primeiro, clone o repositório do projeto em sua máquina local:

```bash
git clone https://github.com/seuusuario/nome-do-repositorio.git

cd nome-do-repositorio

#windows
.\venv\Scripts\activate

#mac/linux
source venv/bin/activate

#instalar dependências
pip install -r requirements.txt

#configurar variáveis de ambiente
DB_HOST=localhost
DB_USER=seuusuario
DB_PASS=suasenha

#rodar projeto
python app.py

ou

python nome_do_script.py

#testes
pip install pytest

pytest

```
Licença


Esse modelo inclui a criação de um ambiente virtual, instalação das dependências via `requirements.txt`, e as instruções para rodar o projeto em Python. Certifique-se de adicionar um arquivo `requirements.txt` contendo as bibliotecas que seu projeto utiliza.


