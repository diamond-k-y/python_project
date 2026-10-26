# 类与对象
from dataclasses import dataclass, field

class Animal:
    kingdom = "动物界"  # 类属性
    def __init__(self, name, sound="..."):
        self.name = name  # 实例属性
        self.sound = sound  # 实例属性

    def speak(self):
        return f"{self.name} 说 {self.sound}"  # 实例方法

    def __repr__(self):
        return f"Animal(name={self.name!r})"  # 自定义对象的字符串表示

    def __eq__(self, other):
        return isinstance(other, Animal) and self.name == other.name  # 自定义对象的相等比较

    @classmethod
    def from_string(cls, s):
        name, _, sound = s.partition(":")
        return cls(name, sound)  # 类方法，用于从字符串创建对象

    @staticmethod
    def is_loud(sound):
        return sound.isupper()  # 静态方法，用于判断声音是否大写

    @property
    def shout(self):
        return self.sound.upper()  # 属性方法，用于获取大写的声音

class Dog(Animal):  # 继承自Animal类
    def __init__(self, name, sound="汪"):
        super().__init__(name, sound)  # 调用父类的构造方法

    def speak(self):
        return super().speak() + "!"  # 重写父类的方法

a = Animal.from_string("猫:喵")  # 使用类方法创建对象
print(a)  # Animal(name='猫')
print(repr(a))  # Animal(name='猫')
print(a.speak())  # 猫 说 喵
print(a.shout)  # 喵

d = Dog("旺财")  # 创建Dog对象
print(d.speak())  # 旺财 说 汪!
print(isinstance(d, Animal))  # True
print(Animal.kingdom)  # 动物界
print(Animal("猫") == a)  # True 自定义 __eq__ 只比较 name
print(Animal.is_loud("WOOF"))  # True

@dataclass
class Point:
    x: int = 0
    y: int = 0
    tags: list[str] = field(default_factory=list)
print(Point(1, 2) == Point(1, 2))  # True dataclass 自动生成 __eq__