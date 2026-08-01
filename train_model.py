import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("heart.csv")

print(df.head())

print("\nMissing Values")
print(df.isnull().sum())

X = df.drop("target", axis=1)
y = df["target"]

print("\nNumerical Features")
print(list(X.columns))

print("\nTarget Variable")
print(y.name)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

pred = model.predict(X_test)

accuracy = accuracy_score(y_test, pred)

print("Accuracy:", accuracy)

joblib.dump(model, "model.pkl")

print("Model Saved!")