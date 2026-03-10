# API-Served ML Model

A scikit-learn classification model served as a containerized REST API using FastAPI and Docker. Uses the classic Iris dataset to keep the focus on the infrastructure and serving pattern rather than the modeling problem itself.

## Tech stack

- **Model:** scikit-learn (RandomForestClassifier)
- **API:** FastAPI
- **Containerization:** Docker
- **Model serialization:** joblib

## Project structure

```
├── api/
│   ├── api.py               # FastAPI application
│   └── run_test_request.py  # Sample request script
├── model/
│   └── model_generation.py  # Model training script
├── model_weights.joblib     # Serialized trained model
├── Dockerfile
└── requirements.txt
```

## Running the API

Build the Docker image:

```bash
docker build -t model-api .
```

Start the container:

```bash
docker run --name model-api-container -p 8000:8000 model-api
```

The API is available at `http://localhost:8000`. Visit `http://localhost:8000/docs` for the interactive Swagger UI.

## Endpoints

**`GET /`** — Returns a description of the API.

**`POST /predict`** — Classifies an Iris sample into one of three species.

Request body:

```json
{
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
}
```

Response:

```json
{
    "prediction": 0
}
```

The response returns the numeric class index (0 = Setosa, 1 = Versicolour, 2 = Virginica). Returning the index rather than the label keeps the API flexible for downstream consumers.

## Sample inputs per class

| Class | Species | Sample |
|---|---|---|
| 0 | Setosa | `{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}` |
| 1 | Versicolour | `{"sepal_length": 6.6, "sepal_width": 3.0, "petal_length": 4.4, "petal_width": 1.4}` |
| 2 | Virginica | `{"sepal_length": 5.9, "sepal_width": 3.0, "petal_length": 5.1, "petal_width": 1.8}` |

## Model notes

- **Algorithm:** RandomForestClassifier (default hyperparameters)
- **Train/test split:** 80/20, `random_state=42`
- **Serialization:** joblib — optimized file size, bundled directly into the Docker image
- Only the dependencies strictly required for serving are included in `requirements.txt`, keeping the container image lean
