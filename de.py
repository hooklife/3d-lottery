from autogluon.tabular import TabularDataset, TabularPredictor
import pandas as pd

predictor = TabularPredictor.load("agModels-predictClass/")
test_data = pd.read_csv('test.csv')
y_test = test_data["number"]
y_pred = predictor.predict(test_data)

print(y_pred)
perf = predictor.evaluate_predictions(y_true=y_test, y_pred=y_pred, auxiliary_metrics=True)
p2 = predictor.leaderboard(test_data, silent=True)

print(p2)