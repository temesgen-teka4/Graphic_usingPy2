import turtle
import random
import time

# Screen setup
screen = turtle.Screen()
screen.bgcolor("#0f0f1a")
screen.title("Hello Luna - Welcome Back to Python")
screen.tracer(2, 0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

leaf_tips = []
LEAF_COLORS = ["#ffb7b2", "#ff9aa2", "#e2f0cb", "#b5ead7", "#c7ceea"]
FRUIT_COLORS = ["#ff2a2a", "#ff8c00", "#ffd700", "#ff1493", "#da70d6"]

def draw_moon_and_stars():
    # Glowing Moon
    t.penup()
    t.goto(160, 160)
    t.pendown()
    t.color("#fff4d0")
    t.begin_fill()
    t.circle(45)
    t.end_fill()
    
    t.penup()
    t.goto(160, 145)
    t.pendown()
    t.pensize(2)
    t.color("#fff8e7")
    t.circle(60)

    # Twinkling Stars
    for _ in range(35):
        sx = random.randint(-280, 280)
        sy = random.randint(50, 280)
        t.penup()
        t.goto(sx, sy)
        t.pendown()
        t.color(random.choice(["#ffffff", "#e0e6ff", "#ffd1dc"]))
        t.dot(random.randint(2, 4))

def draw_grass():
    # Base ground mound
    t.penup()
    t.goto(-350, -225)
    t.setheading(0)
    t.pendown()
    t.color("#1b4d3e")
    t.begin_fill()
    t.goto(350, -225)
    t.goto(350, -320)
    t.goto(-350, -320)
    t.end_fill()

    # Individual grass blades
    grass_colors = ["#2ecc71", "#27ae60", "#a8e063", "#55efc4"]
    for gx in range(-330, 340, 6):
        t.penup()
        t.goto(gx + random.randint(-2, 2), -225)
        t.setheading(random.randint(70, 110))
        t.pendown()
        t.pensize(2)
        t.color(random.choice(grass_colors))
        blade_height = random.randint(10, 25)
        t.forward(blade_height)

def write_greeting():
    t.penup()
    t.goto(0, 195)
    t.color("#ff3366")
    t.write("✨ Hello Luna ✨", align="center", font=("Arial", 28, "bold"))

def write_welcome_back():
    t.penup()
    t.goto(0, 155)
    t.color("#00f2fe")  # Vibrant cyan
    t.write("🐍 Welcome back to Python 🐍", align="center", font=("Arial", 20, "bold"))

def write_followup():
    t.penup()
    t.goto(0, 115)
    t.color("#ffe600")  # Bright golden yellow
    t.write("How are you today?", align="center", font=("Arial", 20, "bold"))

def grow_branches(branch_len, thickness):
    t.pensize(max(thickness, 1))
    
    if branch_len < 15:
        leaf_tips.append(t.position())
        return

    t.color("#4a2e1b")
    t.forward(branch_len)

    angle1 = random.randint(15, 30)
    angle2 = random.randint(15, 30)
    reduction = random.randint(10, 16)

    t.right(angle1)
    grow_branches(branch_len - reduction, thickness * 0.7)

    t.left(angle1 + angle2)
    grow_branches(branch_len - reduction, thickness * 0.7)

    t.right(angle2)
    t.color("#4a2e1b")
    t.backward(branch_len)

def bloom_leaves():
    for pos in leaf_tips:
        t.penup()
        t.goto(pos)
        t.pendown()
        t.color(random.choice(LEAF_COLORS))
        t.begin_fill()
        t.circle(random.randint(4, 7))
        t.end_fill()

def grow_colorful_fruit():
    fruit_spots = random.sample(leaf_tips, k=min(20, len(leaf_tips)))
    
    for pos in fruit_spots:
        t.penup()
        t.goto(pos[0], pos[1] - 4)
        t.pendown()
        
        chosen_color = random.choice(FRUIT_COLORS)
        t.color(chosen_color)
        t.begin_fill()
        t.circle(random.randint(6, 9))
        t.end_fill()
        
        # Glossy highlight
        t.penup()
        t.goto(pos[0] + 1, pos[1])
        t.pendown()
        t.color("#ffffff")
        t.dot(3)

# --- Run Timed Progressive Sequence ---
draw_moon_and_stars()
draw_grass()

# Sequence of text messages appearing with pauses
write_greeting()
screen.update()

time.sleep(1.2)
write_welcome_back()
screen.update()

time.sleep(1.2)
write_followup()
screen.update()

# Position and Draw Tree
t.penup()
t.goto(0, -225)
t.setheading(90)
t.pendown()

grow_branches(95, 10)
screen.update()

bloom_leaves()
screen.update()

grow_colorful_fruit()
screen.update()

# --- Save Canvas as an EPS file ---
screen.getcanvas().postscript(file="hello_luna.eps")
print("Successfully saved canvas as hello_luna.eps!")

turtle.done()