
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def to_string(self):
        return f'{self.name}{self.age}입니다.'

oz_dog = [
    Dog("썰매",10),
    Dog("레오",4)
]

