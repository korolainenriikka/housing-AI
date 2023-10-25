import joblib
#data = joblib.load("reverse_geocode_result.pkl")
#for i in range(len(data)):
#    print(data[i])
#    print(data[i].keys())
#
#    print("---")
data = joblib.load("geolocation_result.pkl")
data = data[0]

for key, value in data["geometry"].items():
    print(key, value)
#print(data["geometry"])
#for i in range(len(data)):
    #print(data[i])
    #print(data[i].keys())

#    print("---")