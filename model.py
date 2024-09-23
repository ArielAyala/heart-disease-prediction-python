import pandas as pd

data = pd.read_csv('heart-data.csv')

from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()

# Convertir la columna 'Family' en valores numericos utilizando el LabelEncoder
data['Family'] = encoder.fit_transform(data['Family'])

# Separamos las caracteristicas (X) y la variable objetivo (y)
X = data.drop('chd', axis=1)
y = data['chd']

from sklearn.model_selection import train_test_split

# Dividimos el cojunto de datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier()

# Entrenamos el modelo de clasificacion RandonForest
clf.fit(X_train, y_train)

# Importamos la biblioteca pickle para guardar y cargar modelos entrenados
import pickle

# Guardamos el modelo entrenado en un archivo
pickle.dump(clf, open('heart.pkl', 'wb'))


