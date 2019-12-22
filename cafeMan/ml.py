import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from django.contrib.staticfiles.storage import staticfiles_storage

def sandpred():

    dataset = pd.read_csv("https://docs.google.com/uc?id=1aiAwOAvZMfkwQenFp3hZvXlm53RFaO6J&export=download")
    X = dataset.iloc[:, 0:1].values
    y = dataset.iloc[:, 1:2].values
    
    from sklearn.preprocessing import LabelEncoder, OneHotEncoder
    labelencoder_X = LabelEncoder()
    X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
    
    from sklearn.ensemble import RandomForestRegressor
    regressor=RandomForestRegressor(n_estimators=300,random_state=0)
    regressor.fit(X,y)
    # Predicting a new result
    y_pred = regressor.predict(np.array([5.0]).reshape(1, 1))
    y_pred =int(y_pred)
    return y_pred

def noodpred():
    dataset = pd.read_csv("https://docs.google.com/uc?id=1aiAwOAvZMfkwQenFp3hZvXlm53RFaO6J&export=download")
    X = dataset.iloc[:, 0:1].values
    y = dataset.iloc[:, 2:3].values
    
    from sklearn.preprocessing import LabelEncoder, OneHotEncoder
    labelencoder_X = LabelEncoder()
    X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
    
    from sklearn.ensemble import RandomForestRegressor
    regressor=RandomForestRegressor(n_estimators=300,random_state=0)
    regressor.fit(X,y)
    # Predicting a new result
    y_pred = regressor.predict(np.array([5.0]).reshape(1, 1))
    y_pred =int(y_pred)
    return y_pred

def dosapred():
    dataset = pd.read_csv("https://docs.google.com/uc?id=1aiAwOAvZMfkwQenFp3hZvXlm53RFaO6J&export=download")
    X = dataset.iloc[:, 0:1].values
    y = dataset.iloc[:, 3:4].values
    
    from sklearn.preprocessing import LabelEncoder, OneHotEncoder
    labelencoder_X = LabelEncoder()
    X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
    
    from sklearn.ensemble import RandomForestRegressor
    regressor=RandomForestRegressor(n_estimators=300,random_state=0)
    regressor.fit(X,y)
    # Predicting a new result
    y_pred = regressor.predict(np.array([5.0]).reshape(1, 1))
    y_pred =int(y_pred)
    return y_pred
# Importing the dataset

# recommend
def sandrec():
    df=pd.read_csv("https://docs.google.com/uc?id=1nmMvUr0Qq8NS0ZlrTmH_c_kM5FJm-Evm&export=download")
    food_titles = pd.read_csv("https://docs.google.com/uc?id=1pI2KdZnHp4M2t0k9cTmuUo2lMCom-Iz_&export=download")
    food_titles.head()
    df = pd.merge(df,food_titles,on='food_id')
    #df.head()
    df.groupby('food_item')['rating'].mean().sort_values(ascending=False).head()
    df.groupby('food_item')['rating'].count().sort_values(ascending=False).head()
    ratings = pd.DataFrame(df.groupby('food_item')['rating'].mean())
    #ratings.head()
    ratings['num of ratings'] = pd.DataFrame(df.groupby('food_item')['rating'].count())
    #ratings.head()
    foodmat = df.pivot_table(index='user_id',columns='food_item',values='rating')
    #foodmat.head()
    ratings.sort_values('num of ratings',ascending=False).head(10)
    
    sandwich_user_ratings = foodmat['sandwich']
    similar_to_sandwich = foodmat.corrwith(sandwich_user_ratings)
    corr_sandwich = pd.DataFrame(similar_to_sandwich,columns=['Correlation'])
    corr_sandwich.dropna(inplace=True)
    corr_sandwich.sort_values('Correlation',ascending=False).head(10)
    corr_sandwich = corr_sandwich.join(ratings['num of ratings'])
    corr_sandwich[corr_sandwich['num of ratings']>100].sort_values('Correlation',ascending=False).head()
    #print("for sandwich recommend ")
    data_top = corr_sandwich.head()  
    return data_top.index.values[1]

def noodrec():
    df=pd.read_csv("https://docs.google.com/uc?id=1nmMvUr0Qq8NS0ZlrTmH_c_kM5FJm-Evm&export=download")
    food_titles = pd.read_csv("https://docs.google.com/uc?id=1pI2KdZnHp4M2t0k9cTmuUo2lMCom-Iz_&export=download")
    food_titles.head()
    df = pd.merge(df,food_titles,on='food_id')
    #df.head()
    df.groupby('food_item')['rating'].mean().sort_values(ascending=False).head()
    df.groupby('food_item')['rating'].count().sort_values(ascending=False).head()
    ratings = pd.DataFrame(df.groupby('food_item')['rating'].mean())
    #ratings.head()
    ratings['num of ratings'] = pd.DataFrame(df.groupby('food_item')['rating'].count())
    #ratings.head()
    foodmat = df.pivot_table(index='user_id',columns='food_item',values='rating')
    #foodmat.head()
    ratings.sort_values('num of ratings',ascending=False).head(10)
    noodles_user_ratings = foodmat['noodles']
    similar_to_noodles = foodmat.corrwith(noodles_user_ratings)
    corr_noodles = pd.DataFrame(similar_to_noodles,columns=['Correlation'])
    corr_noodles.dropna(inplace=True)
    corr_noodles.sort_values('Correlation',ascending=False).head(10)
    corr_noodles = corr_noodles.join(ratings['num of ratings'])
    corr_noodles[corr_noodles['num of ratings']>100].sort_values('Correlation',ascending=False).head()
    #print("for noodles recommend ")
    data_top = corr_noodles.head()  
    return data_top.index.values[1]

def dosarec():
    df=pd.read_csv("https://docs.google.com/uc?id=1nmMvUr0Qq8NS0ZlrTmH_c_kM5FJm-Evm&export=download")
    food_titles = pd.read_csv("https://docs.google.com/uc?id=1pI2KdZnHp4M2t0k9cTmuUo2lMCom-Iz_&export=download")
    food_titles.head()
    df = pd.merge(df,food_titles,on='food_id')
    #df.head()
    df.groupby('food_item')['rating'].mean().sort_values(ascending=False).head()
    df.groupby('food_item')['rating'].count().sort_values(ascending=False).head()
    ratings = pd.DataFrame(df.groupby('food_item')['rating'].mean())
    #ratings.head()
    ratings['num of ratings'] = pd.DataFrame(df.groupby('food_item')['rating'].count())
    #ratings.head()
    foodmat = df.pivot_table(index='user_id',columns='food_item',values='rating')
    #foodmat.head()
    ratings.sort_values('num of ratings',ascending=False).head(10)
    dosa_user_ratings = foodmat['dosa']
    similar_to_dosa = foodmat.corrwith(dosa_user_ratings)
    
    corr_dosa = pd.DataFrame(similar_to_dosa,columns=['Correlation'])
    corr_dosa.dropna(inplace=True)
    
    corr_dosa.sort_values('Correlation',ascending=False).head(10)
    corr_dosa = corr_dosa.join(ratings['num of ratings'])
    
    corr_dosa[corr_dosa['num of ratings']>100].sort_values('Correlation',ascending=False).head()
   # print("for dosa recommend ")
    data_top = corr_dosa.head()  
    return data_top.index.values[1]




