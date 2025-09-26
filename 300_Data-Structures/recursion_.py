"""
    Different Recursions function in Python
    @Author: Federico Baù
    @Creation Date: 21 - Jan - 2021
    @Updated: N/a
    
"""

# ========================= < Int to Str convert Base > ========================= #
def int_to_string_converter():

    def to_str(n, base):
        """

        Args:
            n (int): the Number input
            base (int): The base to convert into

        Returns:
            str: The converted value in a given base format
        """
        convert_string = "0123456789ABCDEF"
        if n < base:
            return convert_string[n]
        else:
            return to_str(n // base, base) + convert_string[n % base]

    print(to_str(1453, 16))



# ========================= < Visualizing Recursion > ========================= #
import turtle
# If get errror ModuleNotFoundError: No module named 'tkinter' install with
# sudo apt-get install python3-tk

# ---------- Simple Recusrive Func
def simple_recursive_function():
    def draw_spiral(my_turtle, line_len):
        if line_len > 0:
            my_turtle.forward(line_len)
            my_turtle.right(120)
            draw_spiral(my_turtle, line_len - 5)

    my_turtle = turtle.Turtle()
    my_win = turtle.Screen()
    draw_spiral(my_turtle, 200)
    my_win.exitonclick()


# ---------- Bynary tree
def bynary_tree():
    def tree(branch_len, t):
        if branch_len > 1:
            t.forward(branch_len)
            t.right(20)
            tree(branch_len - 15, t)
            t.left(40)
            tree(branch_len - 15, t)
            t.right(20)
            t.backward(branch_len)

    def main():
        t = turtle.Turtle()
        my_win = turtle.Screen()
        t.left(90)
        t.up()
        t.backward(150)
        t.down()
        t.color("green")
        tree(120, t)
        my_win.exitonclick()

    main()



# ---------- Sierpinski Triangle
def sierpinski_triangle():
    def draw_triangle(points, color, my_turtle):
        my_turtle.fillcolor(color)
        my_turtle.up()
        my_turtle.goto(points[0][0], points[0][1])
        my_turtle.down()
        my_turtle.begin_fill()
        my_turtle.goto(points[1][0], points[1][1])
        my_turtle.goto(points[2][0], points[2][1])
        my_turtle.goto(points[0][0], points[0][1])
        my_turtle.end_fill()

    def get_mid(p1, p2):
        return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

    def sierpinski(points, degree, my_turtle):
        colormap = ["blue", "red", "green", "white", "yellow", "violet", "orange"]
        draw_triangle(points, colormap[degree], my_turtle)
        if degree > 0:
            sierpinski(
                [points[0], get_mid(points[0], points[1]), get_mid(points[0], points[2])],
                degree - 1,
                my_turtle,
            )
            sierpinski(
                [points[1], get_mid(points[0], points[1]), get_mid(points[1], points[2])],
                degree - 1,
                my_turtle,
            )
            sierpinski(
                [points[2], get_mid(points[2], points[1]), get_mid(points[0], points[2])],
                degree - 1,
                my_turtle,
            )

    def main():
        my_turtle = turtle.Turtle()
        my_win = turtle.Screen()
        my_points = [[-180, -150], [0, 150], [180, -150]]
        sierpinski(my_points, 5, my_turtle)
        my_win.exitonclick()

    main()



if __name__ == '__main__':
    int_to_string_converter()
