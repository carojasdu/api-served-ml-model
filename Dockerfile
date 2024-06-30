FROM python:3.12.4

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY model_weights.joblib .
COPY api.py .

CMD ["fastapi", "run", "api.py", "--port", "8000"]
