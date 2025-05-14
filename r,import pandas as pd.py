import random 
# Simulated seismic data (magnitude, depth, location)
 seismic_data = [ 
{"magnitude": random.uniform(2.0, 8.0), "depth": random.uniform(1, 
100), "location": "Zone A"} 
for _ in range(10) 
]
 def predict_earthquake(data): 
predictions = []
 for event in data: 
risk = "Low"
 if event["magnitude"] > 6.0 and event["depth"] < 70: 
risk = "High" 
elif event["magnitude"] > 4.0: 
risk = "Moderate" 
predictions.append({ 
"location": event["location"],
 "magnitude": round(event["magnitude"], 2),
 "depth": round(event["depth"], 1),
 "risk_level": risk 
}) 
return predictions 
def manage_disaster(predictions): 
for p in predictions: 
print(f"Location: {p['location']}")
 print(f"Magnitude: {p['magnitude']} | Depth: {p['depth']} km")
 print(f"Risk Level: {p['risk_level']}")
 if p["risk_level"] == "High": 
print("**ACTION: Evacuation alert sent to emergency 
services**") 
elif p["risk_level"] == "Moderate": 
print("**ACTION: Monitoring closely**") 
else: 
print("**ACTION: No immediate danger**") 
print("-" * 50) 
# Run the system
 predictions = predict_earthquake(seismic_data)
 manage_disaster(predictions)