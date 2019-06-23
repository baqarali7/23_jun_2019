class Human():
    def __init__(self, name, father_name='', favourite_dish='Biryani'):
        self.name = name
        self.favourite_dish = favourite_dish
        self.father_name = father_name
        print('I am inside Constructor')
    def eat(self):
        print(self.favourite_dish, ' Ley ao!')

humans = []
humans.append(Human('Faisal', 'M Iqbal', 'Maghaz Nihari'))
humans[0].father_name = 'Muhammad Iqbal'
humans.append(Human('Inam', 'M Jaffar'))
humans.append(Human('Danish', 'Abbu', 'Pizza'))
for human in humans:
    print(human.name)
    print(human.father_name)
    human.eat()
