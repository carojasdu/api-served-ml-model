FROM python:3.12.4

WORKDIR /api

COPY ./requirements.txt /api/requirements.txt

RUN pip install -r /api/requirements.txt

COPY ./model_weights.joblib /api/
COPY ./api.py /api/   

CMD ["fastapi", "run", "api.py", "--port", "8000"]