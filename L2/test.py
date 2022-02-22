from pycat.core import Window

window = Window()

var1 = True
elephant = window.create_sprite()
print(type(elephant.x))
print(type(3.1415))
print(type("hello world"))
print(type(var1))
print(type(elephant))
print(type(window))
print(type(type("abcde")))
print(type(elephant.color))

window.run()