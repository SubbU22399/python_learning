Scores = [100, 90, 80, 70, 60, 85, 30, 20, 10, 5, 0]
def is_A_student(score):
    return score > 75
over_75 = list(filter(is_A_student, Scores))
print(over_75) 

cars = [
    {'make': 'Ford', 'model': 'Fiesta', 'mileage': 23000, 'fuel_consumed': 460},
    {'make': 'Ford', 'model': 'Focus', 'mileage': 17000, 'fuel_consumed': 350},
    {'make': 'Mazda', 'model': 'MX-5', 'mileage': 49000, 'fuel_consumed': 900},
    {'make': 'Mini', 'model': 'Cooper', 'mileage': 31000, 'fuel_consumed': 235}
]
def calculate_mpg(car):
    mpg = car['mileage'] / car['fuel_consumed']
    return mpg
def car_name(car):
    return f"{car['make']} {car['model']}"
for car in cars:
    print(car_name(car))
    print(calculate_mpg(car))
print(" ")
car_names = list(map(car_name, cars))
print(car_names)
print(" ")
mpg_values = list(map(calculate_mpg, cars))
print(mpg_values)