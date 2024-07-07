class Bird:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def to_string(self):
        return f'{self.name}{self.age}입니다.'

oz_bird = [
    Bird("앵무새",10),
    Bird("독수리",4)
]
