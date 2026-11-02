from sklearn.model_selection import train_test_split

X = [
    [1, 0],
    [2, 1],
    [3, 1],
    [4, 3],
    [5, 4],
    [6, 5]
]

# X is hours studied and practice tests completed , y is the results

y = [
    "Fail",
    "Fail",
    "Fail",
    "Pass",
    "Pass",
    "Pass"
]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.33,
    random_state=42
)

print("X_train:", X_train)
print("X_test:", X_test)
print("y_train:", y_train)
print("y_test:", y_test)

#Actual Classifier
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print("Predictions:", predictions)

print("Actual:", y_test)
print("Accuracy:", model.score(X_test, y_test))

# Mini-project: Student Pass Prediction
# Goal: Predict whether a student will Pass or Fail.
# Features: Hours studied and practice tests completed.
# Target: Pass or Fail.

new_student = [[3, 2]]
new_student2 = [[5, 4]]
new_student3 = [[1, 5]]

new_prediction = model.predict(new_student)
new_prediction2 = model.predict(new_student2)
new_prediction3 = model.predict(new_student3)

print("New student prediction:", new_prediction)
print("New student 2 prediction:", new_prediction2)
print("New student 3 prediction:", new_prediction3)
