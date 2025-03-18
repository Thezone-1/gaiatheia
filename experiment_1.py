import logging
from codecarbon import OfflineEmissionsTracker
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# Initialize the tracker for experiment 1
tracker = OfflineEmissionsTracker(
    project_name="GIATHEIA_1",
    log_level=logging.INFO,
    # output_file="profiler.csv",
    # save_to_file=True,
    measure_power_secs=5,
    save_to_prometheus=True
)

# Loading and preprocessing the data
iris = load_iris()
X = iris.data
y = iris.target

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training the SVM classifier
tracker.start()
clf = SVC(kernel='linear')
clf.fit(X_train, y_train)
tracker.stop()

print("SVM model training complete.")