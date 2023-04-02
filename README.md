## Plutus

### SOBRE O PROJETO :file_folder:
Microsserviço em Python utilizando FastAPI para o desafio "MaisTodos Backend"

<hr>

### TECNOLOGIAS QUE ESTÃO SENDO USADAS :space_invader:

:small_blue_diamond: Creditcard: Validar número de cartões de crédito.

:small_blue_diamond: Cryptography: Criptografar os dados que são salvos no banco de dados.

:small_blue_diamond: Decouple: Utilizar variaveis de ambiente.

:small_blue_diamond: FastAPI: Web framework para construir a API.

:small_blue_diamond: Loglifos: Loggar avisos/erros.

:small_blue_diamond: Pip chill: Alternativa ao pip-freeze, agrupando somente top-level.

:small_blue_diamond: Pydantic: Validação dos dados de entrada.

:small_blue_diamond: Pyfiglet: Prints mais bonitinhos :P

:small_blue_diamond: Pymongo: Conexão com banco de dados MongoDB.

:small_blue_diamond: Pytest: Rodar testes unitários/mockados.

<hr>

### ROTAS DISPONIVEIS :telescope:

##### Acesse a rota abaixo para maiores detalhes.

```
{host}:{port}/docs
```

#### GET

```
{host}:{port}/api/v1/credit-card - Lista todos os cartões cadastrados.
{host}:{port}/api/v1/credit-card/{credit_card_number} - Busca detalhes de um cartão especifico. 
```

#### POST

```
{host}:{port}/api/v1/credit-card - Cadastra um novo cartão de acordo com o body enviado - {"exp_date": string, "holder": string, "number": string, "cvv": optional[string]}
```

<hr>

### PARA EXECUTAR O SERVIDOR VIA DOCKER COMPOSE :floppy_disk:
- Com o Docker e Docker Compose instalados na sua maquina rode o comando ```docker-compose up -d``` ou ```docker compose up -d``` na pasta raiz do projeto.
- Ao executar com o Docker, será criado uma imagem para o MongoDB e para o Plutus.
- Acesse ```localhost:8080/docs```

### PARA EXECUTAR O SERVIDOR SEM O DOCKER :calling:
- Crie um novo ambiente virtual com ```python3 -m virtualenv .venv``` ou ```python3 -m venv .venv```
- Ative o seu novo ambiente virtual com ```source ./venv/bin/activate``` ou ```.venv\Scripts\activate.bat```
- Instale as dependências do projeto com ```pip install -r requirements.txt``` ou ```pip install -r requirements-dev.txt``` caso for executar os testes

- Crie um arquivo ```.env``` na raiz do projeto de acordo com o ```.env_exemple```

```
-- SERVER --
SERVER_PORT= Porta em que o servidor ficará de pé.

-- MONGODB --
MONGO_HOST= Conexão com o MongoDB.
MONGO_DATABASE= Nome do database.
MONGO_COLLECTION= Nome da collection.

-- TOKEN --
VALID_TOKEN= String que será usada para fazer a autenticação de acesso aos end-points.

-- OBFUSCATE --
FERNET_KEY= Chave que será utilizada para criptografar/descriptografar os dados - Com a venv ativada execute o comando "python3 generate_fernet_key_script.py" para gerar uma nova chave.
```

- Execute o comando ```python3 plutus.py``` para startar o servidor.
- Acesse ```localhost:8080/docs```

### PARA EXECUTAR OS TESTES :bomb:
- Somente testes unitários: ```pytest```
- Testes de cobertura: ```chmod +x run_coverage_tests.sh``` e depois ```./run_coverage_tests.sh```
