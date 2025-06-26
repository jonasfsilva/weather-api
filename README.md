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


## O que faria se tivesse mais tempo

- Mais testes para casos de falha
- Outros endpoints como de achar cidades por coordenadas

## Porque das decisões técnicas

- Criacao dos apps separados para melhor organização do projeto
- BaseModel para garantir que toda tabela tenha as devidas estruturas de controle (created_at, updated_at e um id como UUID)
- A classe WeatherService foi feita para ser reutilizável e fácil de testar.
- Testes separados: Foram criados testes unitários (serviços) e testes de API (rotas).
- Logs claros: Mensagens de log ajudam a entender erros e o que está acontecendo.
- Cache com Redis: Para evitar chamadas repetidas à API externa, os dados ficam salvos por 10 minutos.