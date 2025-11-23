
# Monthly RF inference (example)
import numpy as np, joblib
rf = joblib.load('/mnt/data/smartmeter/monthly_rf.pkl')
scaler = joblib.load('/mnt/data/smartmeter/monthly_scaler.pkl')
# features = [monthly_kWh, avg_daily_kWh, month_num, lag1_kWh, lag2_kWh, lag3_kWh, tariff]
# X = np.array(features).reshape(1,-1)
# Xs = scaler.transform(X)
# pred_bill = rf.predict(Xs)[0]
# print('Predicted monthly bill (Rs):', pred_bill)
