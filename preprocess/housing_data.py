import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("./streamlit/data/gold/dataset/test_dataset_pred.csv", index_col=0)
districts = df["District"].unique()
#print(df.head())
for district in districts:
    df_district = df[df["District"] == district]
    df_district.plot(x="Year", y="Pred_Num_Houses", kind="line", title=district)
    plt.savefig("./streamlit/data/gold/plots/" + district + ".png")
    plt.close()
    print(district)