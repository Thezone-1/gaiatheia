import logging
from codecarbon import EmissionsTracker
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Initialize tracker for experiment 2
tracker = EmissionsTracker(
    project_name="GIATHEA_2",
    log_level=logging.INFO,
    output_file="profiler.csv",
    save_to_file=True,
    measure_power_secs=5,
    #save_to_prometheus=True
)

# Loading and preprocessing the data
tf.random.set_seed(42)
iris = load_iris()
X = iris.data
y = iris.target

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Defining the model
model = Sequential([
    Dense(10, activation='relu', input_shape=(4,)),
    Dense(10, activation='relu'),
    Dense(3, activation='softmax')
])

optimizer = Adam(learning_rate=0.001)
model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()

# Train the model
tracker.start()
model.fit(X, to_categorical(y), epochs=100, batch_size=1, verbose=0)
tracker.stop()

print("Neural network training complete.")
