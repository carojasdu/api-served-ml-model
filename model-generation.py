from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

def train_and_evaluate_model():
    iris = load_iris()

    X = iris.data
    y = iris.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    rf_classifier = RandomForestClassifier()
    rf_classifier.fit(X_train, y_train)

    y_pred = rf_classifier.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    print("The model's accuracy is:", accuracy)

    return rf_classifier

def save_model(model, filename):
    joblib.dump(model, filename)

def main():
    model = train_and_evaluate_model()
    save_model(model, 'model_weights.joblib')

if __name__ == "__main__":
    main()
