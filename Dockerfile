FROM python:3.11-slim

WORKDIR /app

COPY ./ ./

RUN pip install poetry
RUN poetry install --no-dev

EXPOSE 8000
CMD ["poetry", "run","uvicorn", "weather_forecast.main:app", "--port", "8000"]