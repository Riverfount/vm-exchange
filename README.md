# VM-Exchange a Foreign Exchange API with FastAPI

This project provides a simple API for converting currencies using FastAPI.
It fetches exchange rates from external APIs: APILayer and Etherscan.

### 🛠️ Built with
- **fastAPI** - A Python framework to build APIs.
- **Dynaconf** - A Python library to manage environments
- **aioetherscan** - Etherscan.io API async Python non-official wrapper. 
- **httpx** - HTTPX is a fully featured HTTP client for Python 3, which provides sync and async APIs, and support for both HTTP/1.1 and HTTP/2.

## 🚀 Features
- Convert between various currencies.
- Use two exchange rate providers to cover more currencies as ETH.
- Built with FastAPI for a performant and scalable solution.
- Dependency management with Poetry for a clean and reproducible environment.
- Dockerized for easy deployment and consistent environments.

### 📋 Prerequisites to Code:
- **Python**: A Python version >= 3.12
- **Docker**: Install Docker following the official guide for your operating system
- **Poetry**: Install Poetry

### 📋 Prerequisites to Execute the Project
- **APILayer API KEY**: It can get here: [https://apilayer.com/](), this value needs to put it in APILAYER_API_KEY on .secrets.toml files or in environment variable.
- **ETH API KEY**: It can get here: [https://etherscan.io/](), this value needs to put it in ETH_API_KEY on .secrets.toml files or in environment variable.

**Note**: Both have free accounts to test.

## 🔧 Installation
#### 🔩 To contribute to this project
1. Make a fork of this repository (this is made in GitHub)
1. Clone your fork 
1. Move to the project directory
1. Create a .secrets.toml or environment variables file with the API KEYs needed to run the project (as sad in Prerequisites to Execute)
1. Install dependencies with Python Poetry
1. Execute the project 
1. Open the broser and access 127.0.0.1:8000 

```bash
git clone git@github.com:[YourUser]/vm-exchange.git
cd vm-exchange
export VM_EXCHANGE_APILAYER_API_KEY='YouSuperSecretAPILayerKEY'  # Create the envvar of APILayer API Key
export VM_EXCHANGE_ETH_API_KEY='YouSuperSecretETHAPIKEY'  # Create the envvar of ETH API Key
poetry install
poetry run fastapi dev api/main.py
```

## 📦 Deploy with Docker 
To execute the project locally or on a server you can use Docker. 
How this project is experimental, and how it is used to Build the image and up the container is a simple way to point 
out how to do it.
1. Build the image
2. Up the container
3. Open the browser and access 0.0.0.0:8000

```bash
docker build -t vm-exchange:0.1.0 .
docker run --rm -p 8000:8000 -e VM_EXCHANGE_APILAYER_API_KEY='YouSuperSecretAPILayerKEY' -e VM_EXCHANGE_ETH_API_KEY='YouSuperSecretETHAPIKEY' vm-exchange:0.1.0
```

## 📄 License
- This project is licensed by **GPLv3+**.
