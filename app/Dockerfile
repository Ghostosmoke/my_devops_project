# Этап 1: Сборка (builder)
FROM python:3.11-slim as builder
WORKDIR /build
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Этап 2: Финальный образ (лёгкий!)
FROM python:3.11-alpine
WORKDIR /app

# Копируем только установленные пакеты из builder
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

# Копируем код приложения
COPY . .

EXPOSE 5000

# Запускаем через gunicorn (продакшн-сервер)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]