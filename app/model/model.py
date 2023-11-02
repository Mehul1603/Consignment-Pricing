import pickle
import re
from pathlib import Path

__version__ = "0.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent

with open(f"{BASE_DIR}/trained_model-{__version__}.pkl", "rb") as f:
    model = pickle.load(f)

def predict_data(item_value, item_quantity, weight, item_insurance):
    pred = model.predict([[item_value, item_quantity, weight, item_insurance]])
    return pred[0]


if __name__ == "__main__":
    print(predict_data(174048.00, 5439, 2097, 215.30))