import matplotlib.pyplot as plt

def plot_predictions(monthly_sales, X_test, y_test, y_pred, future):
    fig, ax = plt.subplots(figsize=(13, 5))
    ax.plot(monthly_sales['YearMonth'], monthly_sales['Sales'],
            label='Actual Sales', color='steelblue')
    test_dates = monthly_sales['YearMonth'].iloc[X_test.index]
    ax.plot(test_dates, y_pred, label='Predicted (Test)',
            color='orange', linestyle='--')
    ax.set_title('Sales Prediction — Linear Regression')
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales ($)')
    ax.legend()
    plt.tight_layout()
    plt.savefig(r'C:\projects\predictive-analytics\outputs\plots\predictions.png')
    plt.show()