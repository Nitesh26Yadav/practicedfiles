# # weekDays = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']


# # def convertToString(weekDays):
# #     string_a = "-".join(weekDays)
# #     return (string_a)


# # print(convertToString(weekDays))
# from collections import Counter

# days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sun', 'mon', 'mon']
# length_of_days = len(days)
# # def findMaxOccuringString(days):
# # print(max(days, key=days.count))
# num = 0
# total = 0
# final_data = []
# for i in days:
#     for _ in range(length_of_days):
#         if i == days[num]:
#             total = total + 1

#         object1 = {days[num]: total}
#     final_data += object1
#     num += 1
#     total = 0
# print(object1)

# name = ['jfbj', 'abc', 'def']
# print(name)
# reversed_name = reversed(name)
# print(list(reversed_name))

class Car:
    def __init__(self, color, max_speed, acceleration, tyre_friction):
        self.color = color
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.tyre_friction = tyre_friction
        self.is_engine_started = False
        self.current_speed = 0

    def start_engine(self):
        self.is_engine_started = True

    def stop_engine(self):
        self.is_engine_started = False

    def accelerate(self):
        if not self.is_engine_started:
            print("Car has not started yet")
            self.current_speed = 0
        else:
            self.current_speed += self.acceleration
            if self.current_speed > self.max_speed:
                self.current_speed = self.max_speed

    def apply_brakes(self):
        self.current_speed -= self.tyre_friction
        if self.current_speed < 0:
            self.current_speed = 0

    def sound_horn(self):
        if not self.is_engine_started:
            print("Car has not started yet")
        else:
            print("Beep Beep")


def default_test():
    car = Car(color="Red", max_speed=250, acceleration=10, tyre_friction=3)

#     car.accelerate()
#     print(car.current_speed)
#     car.start_engine()
#     car.accelerate()
#     print(car.current_speed)
#     car.accelerate()
#     print(car.current_speed)
#     car.accelerate()
#     car.accelerate()
#     # car.stop_engine()
#     car.accelerate()
#     print(car.current_speed)
#     print(car.current_speed)

# ------------ Checking sound horn ----------
    # car.sound_horn()
    # car.start_engine()
    # car.sound_horn()
    # car.stop_engine()
    # car.sound_horn()

# ---------- checking brakes -----------

    # car.start_engine()
    # car.accelerate()
    # print(car.current_speed)
    # car.apply_brakes()
    # print(car.current_speed)
    # car.apply_brakes()
    # print(car.current_speed)
    # car.apply_brakes()
    # print(car.current_speed)
    # car.apply_brakes()
    # print(car.current_speed)


default_test()
