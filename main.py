from canvas import Canvas
from shapes import Rectangle, Square
    

canvas_height = int(input("Enter the canvas height: "))
canvas_width = int(input("Enter the canvas width: "))

colors = {"white":(255, 255, 255), "black":(0, 0, 0)}
canvas_color = input("Enter canvas color (white or black): ")

canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])

while True:
    shape_type = input("What would you like to draw? Enter quit to quit: ")
    
    if shape_type.lower() == 'rectangle':
        rect_x = int(input("Enter x of the rectangle: "))
        rect_y = int(input("Enter y of the rectangle: "))
        rect_height = int(input("Enter the height of the rectangle: "))
        rect_width = int(input("Enter the width of the rectangle: "))
        red = int(input("How much red should be rectangle have: "))
        green = int(input("How much green: "))
        blue = int(input("How much blue: "))
        
        rect = Rectangle(x=rect_x, y=rect_y, height=rect_height, width=rect_width, color=(red, green, blue))
        rect.draw(canvas)
        
    if shape_type.lower() == 'square':
        sqr_x = int(input("Enter x of the sqaure: "))
        sqr_y = int(input("Enter y of the sqaure: "))
        sqr_side = int(input("Enter the side lenght of the sqaure: "))
        red = int(input("How much red should be rectangle have: "))
        green = int(input("How much green: "))
        blue = int(input("How much blue: "))

        sqr = Square(x=sqr_x, y=sqr_y, side=sqr_side, color=(red, green, blue))
        sqr.draw(canvas)
        
    if shape_type == "quit":
        break


canvas.make('canvas.png')