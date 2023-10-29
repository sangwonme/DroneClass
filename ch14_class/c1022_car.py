class Car:
    def __init__(self, num):
        self.num = num
        self.pos = 0
        self.speed = 100
        self.color = 'red'

    def recolor(self, color):
        self.color = color
        print(self.color)

    # move
    def move(self):
        self.pos += self.speed
    
    # report
    def report(self):
        print('''
        자동차 번호 : {}
        자동차 색  : {}
        자동차 위치 : {}
        '''.format(self.num, self.color, self.pos))

# list 사용해서 자동차 100대 만들기 (~12:47)
cars = []
for i in range(100):
    cars.append(Car(i))

cars[17].recolor('blue')
cars[17].report()