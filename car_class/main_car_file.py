from car_class import Car

my_own_car = Car(2026,  "Bugatti Bolide")

print("Accelerate")
for i in range(5):
    my_own_car.accelerate()
    print("Speed:", my_own_car.get_speed())

print()
print()

print("Braking")
for i in range(5):
    my_own_car.brake()
    print("Speed:", my_own_car.get_speed())

