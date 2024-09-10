brand_cars = ("Toyota", "Honda", "Benz", "BMW", "Volvo", "Ford")

# =========================================================
# 3.1 -- Show Location of "Honda", "BMW" and "Volvo"

print("Location of Honda is at " + str(brand_cars.index("Honda")))
print("Location of BMW is at " + str(brand_cars.index("BMW")))
print("Location of Volvo is at " + str(brand_cars.index("Volvo")))
print("")

# =========================================================
# 3.2 -- Show all tubles

print(brand_cars)
print("")

# =========================================================
# 3.3 -- Check "Toyota", "Benz", "Ford", "Suzuki", "Nissan"

quest = ("Toyota", "Benz", "Ford", "Suzuki", "Nissan")

for i in quest:
    for j in brand_cars:
        if i == j:
            print(i + " is in the tuble.")
            break
        elif i != j:
            if j == "Ford":
                print(i + " isn't in the tuble")
