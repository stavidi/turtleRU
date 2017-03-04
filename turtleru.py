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

screen = turtle.Screen()

# animation control
def жди(sec):
    sleep(sec)

# drawing control
def стереть(**kwargs):
    screen.reset(**kwargs)
    
def всеУбрать(**kwargs):
    screen.reset(**kwargs)  
    
class Черепаха (turtle.Turtle) :
    def __init__(self,**kwargs):
       super(Черепаха, self).__init__(**kwargs)
        
    # Color control
    def цвет(self, *colors) :
        return t.color(*list(RU_COLOR.get(c, c) for c in colors ))
        
    def цветПера(self, *colors) :
        return t.pencolor(*list(RU_COLOR.get(c, c) for c in colors ))
        
    def цветЗакраски(self, *colors) :
        return t.fillcolor(*list(RU_COLOR.get(c, c) for c in colors ))
        
    def будемКрасить(self):
        t.begin_fill()
        
    def заКрасили(self):
        t.end_fill()
        
    def красить(self):
        return t.filling()
        
    # Visibility
    def покажись(self):
        t.showturtle()
        
    def спрячь(self):
        t.hideturtle()
        
    def видно(self):
        return t.isvisible()
        
        
    def вперед(self, n) :
        self.forward(n)

    def назад(self, n) :
        self.back(n)
        
    def лево(self, n):
        self.left(n)
        
    def право(self, n):
        self.right(n)
        
        
t = Черепаха()

def начало(**kwargs) :
    t.shape('turtle')
        
def конец() :
    turtle.mainloop()     # чтобы окно не закрывалось, на repl.it не нужно

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
    
if __name__ == '__main__':
    начало()
    вперед(75)
    конец()
