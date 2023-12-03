from drawbot_skia.drawbot import rect, saveImage, fill

step = 170
y = 100
for i in range(5):
    fill(1, 0, 0.6)
    rect(800, y, 100, 100)
    y = y + step

saveImage('dz1.pdf')