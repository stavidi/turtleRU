# -*- coding: utf-8 -*-
# чтобы можно было писать русские буквы и иероглифы

from time import sleep
import threading

import turtle

RU_COLOR = {
  "черный" : "black",
  "синий" : "blue",
  "зеленый" : "green",
  "красный" : "red",
  "желтый" : "yellow",
  "белый" : "white",
  "рыжий": "orange"
}

EN_COLOR = {}
for ru in RU_COLOR:
  EN_COLOR[RU_COLOR[ru]] = ru

screen = turtle.Screen()

# animation control
def жди(sec):
    sleep(sec)

# drawing control
def стереть(**kwargs):
    screen.reset(**kwargs)
    
def всеУбрать(**kwargs):
    screen.reset(**kwargs)  
    
def цветПоля(*colors):
    q = list(RU_COLOR.get(c, c) for c in colors )
    print("EN color="+str(q))
    c = screen.bgcolor(*q)
    print("bgcolor="+str(c))
    return EN_COLOR.get(c, c)
    
class Черепаха (turtle.Turtle) :
    def __init__(self,**kwargs):
       super(Черепаха, self).__init__(**kwargs)
        
    def пиши(self, arg, **kwargs):
        self.write(arg, **kwargs)
        
    def верни(self):
        self.undo()
        
    def скорость(self, speed=None):
        return self.speed(speed)
        
    # Color control
   
    def цвет(self, *colors) :
        return self.color(*list(RU_COLOR.get(c, c) for c in colors ))
        
    def цветПера(self, *colors) :
        return self.pencolor(*list(RU_COLOR.get(c, c) for c in colors ))
        
    def цветЗакраски(self, *colors) :
        return self.fillcolor(*list(RU_COLOR.get(c, c) for c in colors ))
        
    def будемКрасить(self):
        self.begin_fill()
        
    def заКрасили(self):
        self.end_fill()
        
    def красить(self):
        return self.filling()
        
    # Visibility
    def покажись(self):
        self.showturtle()
        
    def спрячь(self):
        self.hideturtle()
        
    def видно(self):
        return self.isvisible()
        
    # Motion    
    def вперед(self, n) :
        self.forward(n)

    def назад(self, n) :
        self.back(n)
        
    def лево(self, n):
        self.left(n)
        
    def право(self, n):
        self.right(n)
    
    def встатьНа(self, *args):
        self.goto(*args)
        
    def Х(self, x):
        self.setx(x)
        
    def У(self, y):
        self.sety(y)
        
    def курс(self, angle):
        self.seth(angle)
    
    def домой(self):
        self.home()
        
    # Turtle state
    def где(self):
        return self.position();
        
    def мойХ(self):
        return self.xcor();
        
    def мойУ(self):
        return self.ycor();
        
    def мойКурс(self):
        return self.heading();
    def куда(self):
        return self.heading();
        
    def угол(self, x, y=None):
        return self.towards(x,y)
        
    def расстояние(self, x, y=None):
        return self.distance(x,y)
    
    def длина(self, x, y=None):
        return self.distance(x,y)
        
    # Settings for measurement
    def вГрадусы(self, fullcircle=360.0):
        self.degrees(fullcircle)
        
    def вРадианы(self):
        self.radians()
        
    # Pen control
    def пероВниз(self):
        self.down()
        
    def пероВверх(self):
        self.up()
        
    def опущено(self):
        return self.isdown()
        
    def размерПера(self, width=None):
        return self.width(width)

    def толщина(self, width=None):
        return self.width(width)
        
    def перо(self, pen=None, **pendict) :
        return self.pen(pen, **pendict)
        
    # Shapes
    def круг(self, radius, extent = None, steps = None):
        return self.circle(radius, extent, steps)
        
    def точка(self, size=None, *colors):
        self.dot(size, *list(RU_COLOR.get(c, c) for c in colors ))
        
    def шлеп(self):
        return self.stamp()
        
    def убрать_шлеп(self, id):
        self.clearstamp(id)
    
    def убрать_все_шлепы(self):
        self.clearstamps()
        
    def многоугольникНачало(self):
        self.begin_poly()

    def многоугольникКонец(self):
        self.end_poly()

    def многоугольник(self):
        return self.get_poly()
        
t = Черепаха()

def начало(**kwargs) :
    t.shape('turtle')
        
def конец() :
    turtle.mainloop()     # чтобы окно не закрывалось, на repl.it не нужно

пиши = t.пиши
верни = t.верни
скорость = t.скорость
    
цвет = t.цвет
цветПера = t.цветПера
цветЗакраски = t.цветЗакраски
будемКрасить = t.будемКрасить
заКрасили = t.заКрасили
красить = t.красить

покажись = t.покажись
спрячь = t.спрячь
видно = t.видно
    
вперед = t.вперед
назад = t.назад
лево = t.лево
право = t.право

встатьНа = t.встатьНа
Х = t.Х
У = t.У
курс = t.курс
домой = t.домой

где = t.где
мойХ = t.мойХ
мойУ = t.мойУ
мойКурс = t.мойКурс
куда = t.куда
угол = t.угол
расстояние = t.расстояние
длина = t.длина

вГрадусы = t.вГрадусы
вРадианы = t.вРадианы

пероВниз = t.пероВниз
пероВверх = t.пероВверх
опущено = t.опущено
размерПера = t.размерПера
толщина = t.толщина
перо = t.перо

круг = t.круг
точка = t.точка
шлеп = t.шлеп
убрать_шлеп = t.убрать_шлеп
убрать_все_шлепы = t.убрать_все_шлепы

многоугольникНачало = t.многоугольникНачало
многоугольникКонец = t.многоугольникКонец
многоугольник = t.многоугольник

if __name__ == '__main__':
    начало()
    вперед(75)
    конец()
