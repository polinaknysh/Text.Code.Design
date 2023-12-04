from drawbot_skia.drawbot import rect, oval, newPage, saveImage, stroke, fill, strokeWidth, line 

rules = [1, 0, 1, 0, 2, 0, "динозавр"] * 20

w, h = 742.5, 1050
newPage(w, h)

margin = 80
x = margin
y = h - margin

step = (w - margin * 2) / 7

size = step

for rule in rules:
    
    if rule == 0:
        fill(0)
        stroke(0, 0, 0)
        strokeWidth(0)
        oval(x, y - step, size, size)
    
    elif rule == 1:
        fill(0)
        stroke(0, 0, 0)
        strokeWidth(0)
        rect(x, y - step, size, size)
    
    elif rule == 2:
        fill(None)
        stroke(1, 0, 0.5)
        strokeWidth(3)
        oval(x, y - step, size, size)
    
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

# выйдем из цикла (начнём писать
# без отступа) и сохраним pdf
saveImage("dz_tema_2_1.pdf")
