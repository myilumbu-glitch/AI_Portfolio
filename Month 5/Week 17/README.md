# Student Pass Prediction

## Overview

This beginner machine learning project uses a classification model to predict whether a student will pass or fail based on two features:

- Hours studied
- Practice tests completed

The project was created as part of my AI learning roadmap to practice the basic machine learning workflow with Python and scikit-learn.

## Machine Learning Concepts Practiced

- Features (`X`) and target labels (`y`)
- Training and test data
- Classification
- Training a model with `.fit()`
- Making predictions with `.predict()`
- Evaluating a model with `.score()`

## Model

The project uses a `DecisionTreeClassifier` from scikit-learn.

The dataset contains six student examples. The data is split into training and test sets using `train_test_split`.

The model is trained on `X_train` and `y_train`. It then predicts results for `X_test`, and those predictions are compared with `y_test`.

## Example Prediction

The model can also predict for a new student using feature values that were not included in the training data.

Example input:

```python
new_student = [[5, 4]]
```

The model predicted:

```text
Pass
```

## Evaluation

The model achieved an accuracy score of `1.0` on the two examples in the test set.

This means both test predictions were correct. However, the dataset is very small, so this result should not be interpreted as evidence that the model will always make correct predictions.

## Tools Used

- Python
- scikit-learn

## What I Learned

This project helped me understand how a machine learning model learns from labeled examples, makes predictions for unseen data, and is evaluated using a separate test set.

It was an important step in my journey toward understanding practical machine learning.
