import pickle
import re
import numpy as np
from pathlib import Path

__version__ = "0.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent

with open(f"{BASE_DIR}/trained_model-{__version__}.pkl", "rb") as f:
    model = pickle.load(f)

def predict_data(arr):
    pred = model.predict([arr])
    return pred[0]


if __name__ == "__main__":
    print(predict_data(np.array([True, True, 737, True, 4, 1, 30, 67, 26.25, 0.88, True, 4503.00, 0, 3.45, -209])))