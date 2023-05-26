Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle as t
>>> def rectangle(horizontal,vertical,color):
...     t.pendown()
...     t.pensize(1)
...     t.color(color)
...     t.begin_fill()
...     for counter in range(1,3):
...         t.forward(horizontal)
...         t.right(90)
...         t.forward(vertical)
...         t.right(90)
...     t.end_fill()
