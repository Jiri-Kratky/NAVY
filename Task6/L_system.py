import turtle
import math 

def apply_rules(axiom, rules,count):  # Apply the rules to the axiom
    result = ""
    for char in axiom:  # Apply the rules to each character in the axiom
        if char in rules:   # If the character is in the rules, replace it with the rule
            result += rules[char]
        else:
            result += char
    print("\n"+str(count+1) + ". zanoření: "+result)
    return result


def draw_fractal(axiom, length, angle):
    stack = []

    # set default position and heading
    turtle.penup()
    turtle.goto(-200, 0)    
    turtle.pendown()
    turtle.speed(0)
    turtle.left(90)
    
    for char in axiom:
        if char == 'F':
            turtle.forward(length)
        elif char == '+':
            turtle.right(angle)
        elif char == '-':
            turtle.left(angle)
        elif char == '[':
            stack.append((turtle.position(), turtle.heading())) # Save the current position and heading
        elif char == ']':
            position, heading = stack.pop()                     # Restore the position and heading
            turtle.penup()
            turtle.goto(position)
            turtle.setheading(heading)
            turtle.pendown()
    
    turtle.done()
    
"""
květina:
axiom = "F"
rules = {"F": "FF+[+F-F-F]-[-F+F+F]"}
angle = 22.5    


vějíř:
axiom = "F"
rules = {"F": "F[+FF][-FF]F[-F][+F]F"}
angle =35


obrazec:
axiom = "F++F++F"
rules = {"F": "F+F--F+F"}
angle = 60

větev:
axiom = "F"
rules = {"F": "F[+F]F[-F]F"}
angle = math.pi / 7 * 180 /math.pi
"""

axiom = "F++F++F"
rules = {"F": "F+F--F+F"}
angle = 60
length = 8


for _ in range(3):  # Repeat the rule application for 2 iterations
    axiom = apply_rules(axiom, rules,_)

draw_fractal(axiom, length, angle)
