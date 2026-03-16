
import pandas as pd
from sklearn.ensemble import IsolationForest

class IntrusionDetector:

    def __init__(self):
        self.model = IsolationForest(contamination=0.05)

    def train(self, data):
        self.model.fit(data)

    def detect(self, sample):
        prediction = self.model.predict(sample)
        return prediction

def load_logs():
    import random
    data = []
    for i in range(200):
        data.append([random.random(), random.random(), random.random()])
    return pd.DataFrame(data)

if __name__ == "__main__":
    detector = IntrusionDetector()
    logs = load_logs()
    detector.train(logs)
    print("Model trained.")
