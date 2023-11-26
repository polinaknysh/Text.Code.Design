from drawbot_skia.drawbot import oval, saveImage, fill
x = 10
y = 10
step = 10
side = 100
for a in range(10):
     for b in range(10):
        fill(0.5, 0.5, 1)
        oval(x, y, 100, 100)
        y = step + a * (side + step)
        x = step + b * (side + step)
       
    

saveImage("dz2.pdf")