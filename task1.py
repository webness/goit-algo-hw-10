from pulp import LpMaximize, LpProblem, LpVariable, lpSum, LpStatus

model = LpProblem(name="drink-production", sense=LpMaximize)

lemonade = LpVariable(name="Lemonade", lowBound=0, cat='Integer')  # Number of Lemonade units
fruit_juice = LpVariable(name="Fruit_Juice", lowBound=0, cat='Integer')  # Number of Fruit Juice units

model += lemonade + fruit_juice, "Total_Products"

model += (2 * lemonade + fruit_juice <= 100), "Water_Constraint"  # Total water constraint
model += (lemonade <= 50), "Sugar_Constraint"  # Total sugar constraint
model += (lemonade <= 30), "Lemon_Juice_Constraint"  # Total lemon juice constraint
model += (2 * fruit_juice <= 40), "Fruit_Puree_Constraint"  # Total fruit puree constraint

status = model.solve()

print(f"Status: {LpStatus[status]}")
print(f"Optimal Production of Lemonade: {lemonade.value()} units")
print(f"Optimal Production of Fruit Juice: {fruit_juice.value()} units")
print(f"Maximum Total Products: {model.objective.value()} units")
