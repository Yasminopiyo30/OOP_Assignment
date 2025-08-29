# Object-Oriented Programming in Python

This repository contains two Python assignments that demonstrate core **OOP concepts** such as classes, constructors, inheritance, encapsulation, and polymorphism.

---

## 📂 Files Included

- `student_class.py` – Assignment 1: Design Your Own Class
- `polymorphism_challenge.py` – Activity 2: Polymorphism Challenge
- `README.md` – Project documentation

---

## 🏗️ Assignment 1: Design Your Own Class

### Description

In this assignment, we design a **Student class** with attributes and methods.
The class demonstrates:

- **Constructors** (`__init__`) to initialize objects.
- **Inheritance** – `Student` inherits from `Person`, and `GraduateStudent` inherits from `Student`.
- **Encapsulation** – using private attributes with getters and setters.
- **Polymorphism** – method overriding in the `GraduateStudent` class.

### Run the Program

```bash
python student_class.py
```

### Example Output

```
Hi, my name is Yasmin and I am 20 years old.
Student: Yasmin, ID: S123, Course: Computer Science
Grade: A
Hi, my name is Opiyo and I am 25 years old.
Graduate Student: Opiyo, Thesis: AI in Healthcare
```

---

## 🎭 Activity 2: Polymorphism Challenge

### Description

This activity demonstrates **polymorphism** by creating a base class `Vehicle` and subclasses with their own implementation of the `move()` method.

- `Car.move()` → prints "Driving 🚗"
- `Plane.move()` → prints "Flying ✈️"
- `Boat.move()` → prints "Sailing 🚤"

### Run the Program

```bash
python polymorphism_challenge.py
```

### Example Output

```
Car: Driving 🚗
Plane: Flying ✈️
Boat: Sailing 🚤
```

---

s
