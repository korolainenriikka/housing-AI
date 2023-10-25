import pandas as pd
import numpy as np 
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder

# Reproducibility
np.random.seed(42)

# Read dataset
df = pd.read_csv("./streamlit/data/gold/dataset/dataset.csv", index_col=0)

categorical_column = ['district']

# Create an instance of the OneHotEncoder
encoder = OneHotEncoder(sparse=False, drop='first')

# Fit and transform the encoder on the selected categorical column
encoded_data = encoder.fit_transform(df[categorical_column])

# Convert the one-hot encoded data into a DataFrame
encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(categorical_column))

# Concatenate the one-hot encoded DataFrame with the original DataFrame, dropping the original categorical column
result_df = pd.concat([df.drop(columns=categorical_column), encoded_df], axis=1)

X = result_df.drop("num_houses", axis = 1)
y = result_df["num_houses"]
#X = df[["population", "district"]]
#y = df["num_houses"]

#"""one hot encoding using sklearn over df.district"""
#enc = OneHotEncoder()
#X = enc.fit_transform(X["district"])
#print(X)
#df = pd.concat(df["population", "num_houses"],  pd.get_dummies(df.district))

reg = LinearRegression()
reg.fit(X, y) # Fit the model

X_test = pd.read_csv("./streamlit/data/gold/dataset/test_dataset.csv", index_col=0)
#X_test = test_dataset.drop("num_houses", axis = 1)

encoded_df = encoder.transform(X_test[categorical_column])
encoded_df = pd.DataFrame(encoded_df, columns=encoder.get_feature_names_out(categorical_column))

X_test = pd.concat([X_test, encoded_df], axis = 1)

X_test["pred_num_houses"] = X_test.drop(["year", "num_houses", "district"], axis = 1).apply(lambda x: reg.predict(x.values.reshape(1, -1))[0], axis = 1)
X_test["pred_num_houses"] = X_test["pred_num_houses"].apply(lambda z: 0 if z <= 0 else z)

columns = ["year", "population", "district", "num_houses", "pred_num_houses"]


X_test[columns].to_csv("./streamlit/data/gold/dataset/test_dataset_pred.csv")
 
#predictions = reg.predict(X)
#print(predictions)
#print(df)