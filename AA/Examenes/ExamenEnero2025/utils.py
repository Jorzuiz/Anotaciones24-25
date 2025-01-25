import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

def clean_data(path):
    df = pd.read_csv(path)

    # User should drop columns irrelevant to the study beforehand
    # A missing or NA value in an irrelevant column shouldn't make us drop a whole row
    #df_na = df[df.isna().any(axis=1)]
    #display(df_na)
    #df = df.dropna() # Default index=0, rows with missing values

    Y = df['HeartDisease'].astype(float)
    Y = Y.values
    Y = Y.reshape(-1, 1)

    # Split the dataframes on numeric and categoric values
    df_numeric = df.select_dtypes(include=np.number)
    df_numeric = df_numeric.astype(np.float64)
    df_categoric = df.select_dtypes(exclude=np.number)

    # Imput numeric values to the mean
    numeric_imput = SimpleImputer(strategy='mean') 
    df_imputed_numeric = pd.DataFrame(numeric_imput.fit_transform(df_numeric), columns=df_numeric.columns, index=df_numeric.index)

    # Imput categirc values to the most frequent (moda)
    categoric_imput = SimpleImputer(strategy='most_frequent')
    df_imputed_categoric = pd.DataFrame(categoric_imput.fit_transform(df_categoric), columns=df_categoric.columns, index=df_categoric.index)

    normalized_numeric = normal(df_imputed_numeric)
    
    # One-hot encoding
    df_categoric = pd.get_dummies(df_imputed_categoric, dtype=float)

    # Combined the Imputed Dataframes
    df_imputed = pd.concat([normalized_numeric, df_categoric], axis=1)
    #display(df_imputed.loc[[136]],df_imputed.loc[[168]],df_imputed.loc[[186]])

    X = df_imputed.drop('HeartDisease', axis = 1).values    # This is already a matrix

    #print(X, X.shape)

    #print(df.dtypes,df_numeric.dtypes, df_categoric.dtypes)
    # display(df_numeric)
    # display(df_categoric)
    
    return X, Y

    # df_na = df.isnull() # Returns boolean values for nulls in the whole dataframe
    # df_na = df.isnull().any() # Returns boolean values for null in each row
    # df_na = df.isnull().any().any() # Returns boolean if ANY value is nan in the dataframe
    # # sum() can be used in the same way to return the number of nan

    # display(df_na)
    # print(df_na)
    # df_categoric = pd.DataFrame(data=df, columns=['Sex'])
    # df_numeric = pd.DataFrame(data=df, columns=['Age'])
    
    # display(normalized_numeric)
    # print(normalized_numeric.shape)
    # print(df)
    # print(df.dtypes)

# We can normalize each column (pd.Series), the whole dataframe or an array
# StandardScaler uses an estimartor for nan values
def normal(dataframe_to_normalize):
    
    scaler = StandardScaler()
    scaler.set_output(transform="pandas")
    # Return value is already an ndarray, not a dataframe
    normalized_columns = scaler.fit_transform(dataframe_to_normalize)

    return normalized_columns