import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def time_rolling_regression(df, time_window, x_label, y_label, freq ='ME'):
    coeffs = []
    intercepts = []
    r2score = []

    for i in pd.date_range(df.first_valid_index()+time_window, df.index[-1],freq = freq):
        
        x_window = df[x_label].loc[i-time_window:i].to_frame()
        y_window = df[y_label].loc[i-time_window:i].to_frame()

        model = LinearRegression()
        model.fit(x_window, y_window)

        r2 = r2_score(y_window, model.predict(x_window))
        coeff = model.coef_
        intercept = model.intercept_
        
        coeffs.append(coeff[0][0])
        r2score.append(r2)
        intercepts.append(intercept[0])
        
    return coeffs, intercepts, r2score