import math

# function to calculate price per square meter
def pizza_value(diameter, price):
    radius = diameter / 2
    area_cm = math.pi * radius * radius   # area in cm²
    area_m = area_cm / 10000              # change cm² to m²
    value = price / area_m                # price per m²
    return value

# main program
d1 = float(input("Give diameter of first pizza (cm): "))  # d1 = diameter of first pizza
p1 = float(input("Give price of first pizza (€): "))      # p1 = price of first pizza

d2 = float(input("Give diameter of second pizza (cm): ")) # d2 = diameter of second pizza
p2 = float(input("Give price of second pizza (€): "))     # p2 = price of second pizza

v1 = pizza_value(d1, p1)   # v1 = value (€/m²) of first pizza
v2 = pizza_value(d2, p2)   # v2 = value (€/m²) of second pizza

print("First pizza:", v1, "€/m2")
print("Second pizza:", v2, "€/m2")

if v1 < v2:
    print("First pizza is better value.")
elif v2 < v1:
    print("Second pizza is better value.")
else:
    print("Both pizzas are the same value.")
