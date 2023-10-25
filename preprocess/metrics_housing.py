import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("./streamlit/data/gold/dataset/test_dataset_pred.csv", index_col=0)
houses_build_in_2019 = df[df.Year <= 2019]["Pred_Num_Houses"].sum()
predictions_data = df[df.Year > 2019]

total_sum_houses = int(predictions_data["Pred_Num_Houses"].sum())
total_sum_per_district = predictions_data.groupby("District")["Pred_Num_Houses"].sum().to_frame()


districts_names = total_sum_per_district.index
print("houses built from 2016 to 2019: ", houses_build_in_2019)

print("From 2020 to 2036")
print("Total sum houses: ", total_sum_houses)
#print("Total sum per district: ", total_sum_per_district)
print("Area with the greatest number of new apartments: ", 
        districts_names[total_sum_per_district["Pred_Num_Houses"].argmax()], 
        int(total_sum_per_district["Pred_Num_Houses"].max())
)
print("Area with the greatest number of new apartments: ", 
        districts_names[total_sum_per_district["Pred_Num_Houses"].argmin()], 
        int(total_sum_per_district["Pred_Num_Houses"].min())
        
)
#print("Area with the lowest number of new apartments: ")
#print("Average number of apartments: ")