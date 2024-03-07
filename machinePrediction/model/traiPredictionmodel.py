import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def load_and_train_model(csv_path):
    # Read data from CSV file
    Data = pd.read_csv(csv_path)
    
    # Print the first few rows of the dataset
    # print("Original Dataset:")
    # print(Data.head())

    # Encode categorical variables
    labelEncoder = LabelEncoder()
    Data['gender'] = labelEncoder.fit_transform(Data['gender'])
    Data['smoker'] = labelEncoder.fit_transform(Data['smoker'])

    onehencoder = OneHotEncoder()
    temp = onehencoder.fit_transform(Data[['region']]).toarray()
    tempData = pd.DataFrame(temp, columns=['northeast', 'northwest', 'southeast', 'southwest'], dtype='int')
    Data = pd.concat([Data, tempData], axis=1)
    Data.drop('region', axis=1, inplace=True)

    # Print the dataset after encoding
    # print("\nEncoded Dataset:")
    # print(Data.info())

    # Prepare features and target variable
    X = Data[['age', 'bmi', 'smoker']]
    y = Data['charges']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    return model

# Example usage
bot = load_and_train_model('I:/C/Insurance prediction/dataset/insurance.csv')
# print(model)