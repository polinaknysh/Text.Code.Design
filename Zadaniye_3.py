from drawbot_skia.drawbot import *

canvas_size = 100
newPage(canvas_size, canvas_size)

line_length = 10
line_thickness = 10
shape_spacing = 10

line_start_x = (canvas_size - (3 * line_length + 2 * shape_spacing)) / 2
line_start_y = canvas_size / 2

# Квадрат
rect(line_start_x, line_start_y - line_thickness / 2, line_length, line_thickness)

# Круг
circle_radius = line_thickness / 2
oval(line_start_x + line_length + shape_spacing, line_start_y - circle_radius, line_thickness, line_thickness)

# Крест
cross_size = 1.5* line_thickness
cross_start_x = line_start_x + 2 * (line_length + shape_spacing)
line(
    (cross_start_x, line_start_y),
    (cross_start_x + cross_size, line_start_y)
)
line(
    (cross_start_x + cross_size / 2, line_start_y - cross_size / 2),
    (cross_start_x + cross_size / 2, line_start_y + cross_size / 2)
)

saveImage ("dz3.pdf")