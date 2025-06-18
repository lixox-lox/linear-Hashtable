# Linear Hashing (Python)

A custom implementation of a hash table using **linear probing** in Python.  
This project was built from scratch to understand the core logic of hashing, collision handling, and deletion gap-filling.

## ✅ Features

- Insert elements with integer keys
- Delete elements and automatically fill gaps
- Search for keys efficiently
- Locate elements by key
- Generic key-extraction function via `data_to_key`

## 🧠 Purpose

This is an educational project to learn how hashing works behind the scenes — beyond Python's built-in `dict`.

## 🚀 Example

```python
from linear_hashing import LinearHashing

lh = LinearHashing(10)
lh.insert(42)
print(lh.search(42))    # True
lh.delete(42)
print(lh.search(42))    # False
