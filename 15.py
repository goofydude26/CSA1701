from sklearn.tree import DecisionTreeClassifier

X = [
    [25, 40000],
    [35, 60000],
    [45, 80000],
    [20, 20000],
    [50, 100000],
    [23, 30000]
]

y = ["No", "Yes", "Yes", "No", "Yes", "No"]

model = DecisionTreeClassifier()

model.fit(X, y)

age = int(input("Enter Age: "))
income = int(input("Enter Income: "))

prediction = model.predict([[age, income]])

print("Prediction:", prediction[0])