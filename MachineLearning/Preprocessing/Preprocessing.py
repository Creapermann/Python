import numpy
import matplotlib.pyplot
import pandas
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

"""
This is Datapreprocessing. Preparing data in a way that a Machine Learning model can use it.
"""



# Read in the dataset
dataset = pandas.read_csv("Machine Learning A-Z (Codes and Datasets)/"
                          "Part 1 - Data Preprocessing/Section 2 -------------------- Part 1 - Data Preprocessing --------------------/Python/Data.csv")



# Convert it into matricies
x = dataset.iloc[:, :-1].values    # The feature matrix (The values you feed to the ML model to predict something with)
y = dataset.iloc[:, -1].values     # The Dependent matrix (The values which should get predicted)



# Calculate the missing values
imputer = SimpleImputer(missing_values=numpy.nan, strategy="mean")  # Set up the object
imputer.fit(x[:, 1:3])   # Copy x and fit the missing values in the empty spots
x[:, 1:3] = imputer.transform(x[:, 1:3])   # Calculate and reasign x to be x with the filled empty values



# Encode String Columns to binary so that the ML Model can work with it cause it can just work with numbers, not with strings
ct = ColumnTransformer(transformers=[("encoder", OneHotEncoder(), [0])], remainder="passthrough")  # Setup the object
x = numpy.array(ct.fit_transform(x))  # calculate and reasign the encoded strings

# Encode The Dependent Variable with label encoding
le = LabelEncoder()       # Setup the object
y = le.fit_transform(y)   # Fit, transform and reasign it in one step



# Split the dataset into Training and Test set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, train_size=0.8, random_state=1)



# Feature scaling
sc = StandardScaler()    # Setup the object
x_train[:, 3:] = sc.fit_transform(x_train[:, 3:])    # Scale x_train first
x_test[:, 3:] = sc.transform(x_test[:, 3:])    # Scale x_test with the same conditions of x_train (dont create a new Standardscaler!)