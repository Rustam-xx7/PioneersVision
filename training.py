import argparse
import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


def main():
    # -------- Argument parsing --------
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str, required=True, help="Path to CSV file")
    args = parser.parse_args()

    csv_path = args.data
    print("Loading data from:", csv_path)

    # -------- Load dataset --------
    df = pd.read_csv(csv_path)

    X = df.drop("label", axis=1)
    y = df["label"]

    print(f"Samples: {len(df)}")
    print(f"Classes: {y.unique()}")

    # -------- Train / Test split --------
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # -------- Train model --------
    print("Training model...")
    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42,
        n_jobs=-1
    )
    model.fit(X_train, y_train)

    # -------- Evaluate --------
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print("✅ Accuracy:", acc)

    # -------- Save model (AML compatible) --------
    output_dir = "outputs"                 # ← DO NOT CHANGE
    os.makedirs(output_dir, exist_ok=True)

    model_path = os.path.join(output_dir, "asl_model.pkl")
    joblib.dump(model, model_path)

    print("✅ Model saved at:", model_path)


if __name__ == "__main__":
    main()


