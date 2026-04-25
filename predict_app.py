import joblib
import pandas as pd
import math

factories=pd.read_csv("Factories.csv")
projects=pd.read_csv("Projects.csv")
external=pd.read_csv("External_Factors.csv")

time_model=joblib.load("time_model.pkl")
delay_model=joblib.load("delay_model.pkl")

priority_map={
"High":10,
"Medium":5,
"Low":2
}

def get_factory(fid):
    return factories[factories["factory_id"]==fid].iloc[0]

def get_project(pid):
    return projects[projects["project_id"]==pid].iloc[0]

def get_external(date):
    return external[external["date"]==date].iloc[0]

def calculate_distance(lat1,lon1,lat2,lon2):
    return math.sqrt((lat1-lat2)**2 + (lon1-lon2)**2)*111

# ---------------- USER INPUT ----------------
factory_id=input("Factory ID: ").strip().upper()
project_id=input("Project ID: ").strip().upper()
date=input("Delivery Date (YYYY-MM-DD): ")

# ---------------- FETCH DATA ----------------
f=get_factory(factory_id)
p=get_project(project_id)
e=get_external(date)

lat1,lon1=f["latitude"],f["longitude"]
lat2,lon2=p["latitude"],p["longitude"]

distance=calculate_distance(lat1,lon1,lat2,lon2)

# ---------------- PREP INPUT ----------------
df=pd.DataFrame({
"factory_id":[factory_id],
"project_id":[project_id],
"distance_km":[distance],
"demand":[p["demand"]],
"priority_level":[p["priority_level"]],
"base_production_per_week":[f["base_production_per_week"]],
"production_variability":[f["production_variability"]],
"weather_index":[e["weather_index"]],
"traffic_index":[e["traffic_index"]],
"month":[pd.to_datetime(date).month],
"day":[pd.to_datetime(date).day],
 'calc_distance_km':[distance],
 'max_storage':6
})

# ---------------- MODEL 1 ----------------
expected_time=time_model.predict(df)[0]

df["expected_time_hours"]=expected_time

# ---------------- MODEL 2 ----------------
predicted_delay=delay_model.predict(df)[0]

# ---------------- RISK ----------------
if predicted_delay<2:
    risk="Low"
elif predicted_delay<5:
    risk="Medium"
else:
    risk="High"

# ---------------- REWARD ----------------
priority_score=priority_map[p["priority_level"]]

reward_score=(
priority_score
-(predicted_delay*2)
-(e["traffic_index"]*5)
-(e["weather_index"]*5)
)

# ---------------- OUTPUT ----------------
actual_time=expected_time+predicted_delay

print("\n--- RESULTS ---")
print("Distance:",round(distance,2),"km")
print("Estimated Expected Time:",round(expected_time,2),"hours")
print("Predicted Delay:",round(predicted_delay,2),"hours")
print("Estimated Actual Time:",round(actual_time,2),"hours")
print("Risk Level:",risk)
print("Reward Score:",round(reward_score,2))

print("\n--- INTERPRETATION ---")
print(f"This delivery from {factory_id} to {project_id} is expected to take {round(expected_time,2)} hours.")
print(f"Due to current traffic and weather conditions, it may be delayed by {round(predicted_delay,2)} hours.")
print(f"The final delivery time is estimated to be {round(actual_time,2)} hours.")
print(f"This is a {risk.lower()} risk delivery.")

if reward_score>5:
    decision="high priority"
elif reward_score>1:
    decision="moderate priority"
else:
    decision="low priority"

print(f"It is recommended as a {decision} delivery for planning.")