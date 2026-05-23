import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

def train_linear_model(monthly_sales):
    X = monthly_sales[['Month_Num']]
    y = monthly_sales['Sales']
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("MAE :", mean_absolute_error(y_test, y_pred))
    print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
    print("R²  :", r2_score(y_test, y_pred))
    return model, X_test, y_test, y_pred

def forecast_future(model, last_month_num, n_months=6):
    future = pd.DataFrame({'Month_Num': range(last_month_num+1, last_month_num+1+n_months)})
    future['Predicted_Sales'] = model.predict(future)
    return future