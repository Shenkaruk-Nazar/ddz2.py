import random


class Cat:
    def __init__(self, name):
        self.name = name
        self.gladness = 40
        self.hunger = 5
        self.alive = True

    def to_eat(self):
        print("Time to eat")
        self.hunger += 3
        self.gladness -= 5

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3
        self.hunger -= 1

    def to_chill(self):
        print("time go for a walk")
        self.gladness += 5
        self.hunger -= 1

    def is_alive(self):
        if self.hunger < 0:
            print("....")
            self.alive = False
        elif self.gladness <= 0:
            print("....")
            self.alive = False
        elif self.hunger > 75:
            print("....")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Hunger ={round(self.hunger, 2)}")

    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_eat()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()


cat = Cat(name="Cat")
for day in range(365):
    if cat.alive == False:
        break
    cat.live(day)