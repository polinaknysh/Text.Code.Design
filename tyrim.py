from drawbot_skia.drawbot import *
 
# зададим правила для выбора
# фигуры, которые будем позже
# использовать:
rules = [1, 0, 1, 0, 2, 0, 1, "гусь", 3, 3] * 20
# список * 20
w, h = 742.5, 1050
newPage(w, h)
 
# определим поля и начальные
# координаты
margin = 80
x = margin
y = h - margin
 
# шаг = (ширина страницы - 2  поля (правое и левое)) / на 6 (6 фигур в строке)
step = (w - margin * 2) / 6
 
# создадим переменную size,
# равную выбранному шагу
size = step
 
for rule in rules:
    fill(0)
    stroke(None)
    # круг
    if rule == 0:
        oval(x, y - step, size, size)
    # квадрат
    elif rule == 1:
        rect(x, y - step, size, size)
    # окружность
    elif rule == 2:
        fill(None)
        stroke(0, 0, 0)
        strokeWidth(3)
        oval(x, y - step, size, size)
    # квадрат с красной рамкой
    elif rule == 3:
        fill(None)
        stroke(1, 0, 0)
        strokeWidth(3)
        rect(x, y - step, size, size)
    else:
        print(rule, "<— неизвестное правило")
 
    # сдвинем x на шаг
    x += step
 
    # если строка кончилась,
    # вернём x в начало, а
    # y сдвинем вниз на шаг
    if x >= w - margin:
        x = margin
        y -= step
 
    # если y дошёл до низа
    # страницы, создадим новую и
    # обнулим координаты
    if y - step < margin:
        newPage(w, h)
        x = margin
        y = h - margin
 
# сохраним pdf
saveImage("summary.pdf")