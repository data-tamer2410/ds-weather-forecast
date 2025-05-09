FROM python:3.11-slim

WORKDIR /app

COPY ./ ./

RUN pip install --no-cache-dir poetry
RUN poetry install --without dev

EXPOSE 8000
CMD ["poetry", "run","uvicorn", "weather_forecast.main:app", "--port", "8000", "--host", "0.0.0.0"]
