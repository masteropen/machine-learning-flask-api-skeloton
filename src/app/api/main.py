import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from joblib import dump

_data_path = '../data/salary_data.csv'
_dumps_path = '../dumps/salary_model.joblib'

data = pd.read_csv(_data_path)
features = data.iloc[:, :-1]
target = data.iloc[:, -1]

x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=1)
model = LinearRegression()
model.fit(x_train, y_train)

# dump result
dump(model, _dumps_path)
