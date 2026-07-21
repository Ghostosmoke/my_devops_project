from flask import Flask, render_template
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
# Эта строка автоматически создаст endpoint /metrics
metrics = PrometheusMetrics(app)

# Простой счетчик через глобальную переменную
visit_counter = 0

@app.route('/')
def index():
    global visit_counter
    visit_counter += 1
    return render_template('index.html', visits=visit_counter)

@app.route('/health')
def health():
    """Эндпоинт для проверки, что приложение живо"""
    return {"status": "ok", "visits": visit_counter}

# НЕ создаём /metrics вручную — библиотека делает это сама!

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)