brand_cars = ("Toyota", "Honda", "BMW", "Volvo", "Ford")

# =========================================================
# 2.1 -- Show location of "Toyota", "Volvo", "Ford"

print("Location of Toyota is at " + str(brand_cars.index("Toyota")))
print("Location of Volvo is at " + str(brand_cars.index("Volvo")))
print("Location of Ford is at " + str(brand_cars.index("Ford")))
print("")

# =========================================================
# 2.2 -- Show all data in Tuble

print(brand_cars)
print("")

# =========================================================
# 2.3 -- Check that "Suzuki", "Toyota", "Ford" in the tuble var

quest = ("Suzuki", "Toyota", "Ford")

for i in quest:
    for j in brand_cars:
        if i == j:
            print(i + " is in the tuble.")
            break
        elif i != j:
            if j == "Ford":
                print(i + " isn't in the tuble")
