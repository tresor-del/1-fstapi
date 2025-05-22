# Analytics API

A FastAPI project containerized with Docker, created for learning purposes.

## Features

- Fast and efficient RESTful API
- Interactive documentation (Swagger UI)
- Easy deployment with Docker

## Prerequisites

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Quick Start

```bash
git clone https://github.com/tresor-del/1-fstapi.git
cd analitics_api
docker-compose up --build
```

The API will be available at [http://localhost:8000](http://localhost:8000).

## Documentation

Access the interactive documentation at [http://localhost:8000/docs](http://localhost:8000/docs).

## Project Structure

```
analitics_api/
├── app/
│   ├── main.py
│   └── ...
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## License

This project is licensed under the MIT License.
