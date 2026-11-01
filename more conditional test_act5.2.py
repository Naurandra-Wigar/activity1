car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

city = 'jakarta'
print("\nIs city == 'jakarta'? I predict True.")
print(city == 'jakarta')

print("\nIs city == 'bali'? I predict False.")
print(city == 'bali')

fruit = 'apple'
print("\nIs fruit == 'apple'? I predict True.")
print(fruit == 'apple')

print("\nIs fruit == 'banana'? I predict False.")
print(fruit == 'banana')

color = 'blue'
print("\nIs color == 'blue'? I predict True.")
print(color == 'blue')

print("\nIs color == 'red'? I predict False.")
print(color == 'red')

pet = 'cat'
print("\nIs pet == 'cat'? I predict True.")
print(pet == 'cat')

print("\nIs pet == 'dog'? I predict False.")
print(pet == 'dog')

print("\n--- 5-2: More Conditional Tests ---")

# String: sama dan tidak sama
print(car != 'audi')          # True
print(car != 'subaru')        # False

# Method lower()
car = 'Subaru'
print(car.lower() == 'subaru')   # True
print(car.lower() == 'audi')     # False

# Angka
age = 19
print(age == 19)    # True
print(age == 20)    # False
print(age != 20)    # True
print(age != 19)    # False
print(age > 18)     # True
print(age > 25)     # False
print(age < 25)     # True
print(age < 10)     # False
print(age >= 19)    # True
print(age >= 20)    # False
print(age <= 19)    # True
print(age <= 18)    # False

# Kata kunci and dan or
age_1 = 22
age_2 = 18
print(age_1 >= 21 and age_2 >= 18)   # True
print(age_1 >= 21 and age_2 >= 21)   # False
print(age_1 >= 21 or age_2 >= 21)    # True
print(age_1 < 18 or age_2 < 18)      # False

# Item ada / tidak ada di list
cars = ['subaru', 'toyota', 'honda']
print('toyota' in cars)         # True
print('audi' in cars)           # False
print('audi' not in cars)       # True
print('honda' not in cars)      # False