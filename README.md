# Weather API

API Django para consultar a previsão do tempo atual usando a OpenWeatherMap API. A aplicação utiliza Docker, Redis, Celery para tarefas assíncronas e possui testes automatizados.

---

## Requisitos

- Docker
- Docker Compose

---

## Como rodar o projeto

```bash
docker-compose up --build
```

Como acessar o projeto
**http://localhost:8000**

---

## Executando os testes

### Todos os testes
```bash
docker-compose exec web python manage.py test apps.weather.tests
```

---

## Estrutura de testes

```
apps/
└── weather/
    └── tests/
        ├── unit/           ← testes unitários (ex: services)
        └── integration/    ← testes de API
```

---

## 📚 Documentação (Swagger)

Após subir o projeto, acesse o swagger em:

📄 **Swagger UI:**  
[http://localhost:8000/api/swagger/](http://localhost:8000/api/swagger/)

---

## 🔧 Variáveis de ambiente

As variáveis necessárias estão definidas no arquivo `.env`:

```env
DJANGO_SETTINGS_MODULE=weather_api.settings
DEBUG=1
OPENWEATHER_API_KEY=YOUR_API_KEY_HERE
WEATHER_URL=https://api.openweathermap.org
```

---

## Banco de Dados

A aplicação usa **PostgreSQL**. O volume do banco é persistente. Para resetar:

```bash
docker-compose down -v
```

---

## Contato e Link do Projeto

Desenvolvido por [Jonas Ferreira](https://github.com/jonasfsilva)
