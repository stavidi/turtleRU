# -*- coding: utf-8 -*-
# чтобы можно было писать русские буквы и иероглифы

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

class Черепаха (turtle.Turtle) :
    def __init__(self,**kwargs):
       super(Черепаха, self).__init__(**kwargs)

    def вперед(self, n) :
        self.forward(n)

    def назад(self, n) :
        self.back(n)
        
    def лево(self, n):
        self.left(n)
        
    def право(self, n):
        self.right(n)
        
    def цветПера(self, color) :
        t.pencolor(RU_COLOR[color])
        
t = Черепаха()

def начало(**kwargs) :
    t.shape('turtle')
        
def конец() :
    turtle.mainloop()     # чтобы окно не закрывалось, на repl.it не нужно
    
вперед = t.вперед
назад = t.назад
лево = t.лево
право = t.право
цветПера = t.цветПера
    
def test_oop() :
    ч = Черепаха()   # сделали черепаху, назвали черепаху t
    # ч.вид("черепаха")     # как черепаха выглядит

    ч.вперед(75)         # вперед 75
    ч.лево(90)            # поворот налево на 90 градусов
    # ч.цветлинии('синий')    # рисовать линии синим цветом
    ч.вперед(75)         # вперед 75

    конец()

def test() :
    начало()

    вперед(75)         # вперед 75
    лево(90)            # поворот налево на 90 градусов
    цветПера('синий')    # рисовать линии синим цветом
    вперед(75)         # вперед 75  

    конец()
    
if __name__ == '__main__':
    # test_oop()
    test()
    # print("This file is not intended to be run as __main__.");
    # exit(-1);
