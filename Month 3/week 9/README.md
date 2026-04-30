# Week 9 — Linear Algebra Foundations

## 📌 Overview
This week focused on understanding the basics of linear algebra and implementing them in Python.

## 🧠 Concepts Learned
- What vectors are
- Vector addition
- Scalar multiplication
- Introduction to matrices

## 💻 What I Built
- `vector_operations.py`
  - Vector addition
  - Scalar multiplication
  - Basic vector operations

## 🔑 Key Takeaways
- Vectors can be represented as Python lists
- Mathematical operations can be translated into loops
- Scalar multiplication scales each element of a vector

## 🚀 Example

```python
def scalar_multiply(vector, scalar):
    return [scalar * x for x in vector]
