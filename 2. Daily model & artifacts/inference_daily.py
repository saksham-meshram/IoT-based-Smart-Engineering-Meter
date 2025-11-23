
# Daily RF inference (example)
import numpy as np, joblib
rf = joblib.load('/mnt/data/smartmeter/daily_rf.pkl')
scaler = joblib.load('/mnt/data/smartmeter/daily_scaler.pkl')
# last48 = np.array([...]) # replace with last 48 hourly power_kW values
# X = last48.reshape(1,-1)
# Xs = scaler.transform(X)
# pred_next24h_kWh = rf.predict(Xs)[0]
# print('Predicted next-24h energy (kWh):', pred_next24h_kWh)
