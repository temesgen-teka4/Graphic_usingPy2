from PIL import Image, ImageDraw, ImageFont
import math
import random

# Image dimensions
WIDTH, HEIGHT = 600, 600
frames = []

# Setup base background (Night sky, Moon, Stars, Grass)
def draw_background():
    img = Image.new("RGB", (WIDTH, HEIGHT), color="#0f0f1a")
    draw = ImageDraw.Draw(img)
    
    # Draw Moon
    draw.ellipse([430, 40, 510, 120], fill="#fff4d0")
    draw.arc([420, 30, 520, 130], 0, 360, fill="#fff8e7", width=2)
    
    # Draw Stars
    random.seed(10)
    for _ in range(30):
        sx = random.randint(20, WIDTH - 20)
        sy = random.randint(20, 250)
        draw.ellipse([sx, sy, sx+3, sy+3], fill="#ffffff")
        
    # Draw Grass Land
    draw.rectangle([0, HEIGHT - 140, WIDTH, HEIGHT], fill="#1b4d3e")
    for gx in range(0, WIDTH, 7):
        gh = random.randint(10, 22)
        draw.line([(gx, HEIGHT - 140), (gx + random.randint(-2, 2), HEIGHT - 140 - gh)], fill="#2ecc71", width=2)
        
    return img

# Recursive function to calculate branch lines
def get_tree_branches(x, y, length, angle, branches_list):
    if length < 12:
        return
    rad = math.radians(angle)
    nx = x + length * math.sin(rad)
    ny = y - length * math.cos(rad)
    branches_list.append(((x, y), (nx, ny), length))
    
    # Recursive splits
    get_tree_branches(nx, ny, length * 0.75, angle - 25, branches_list)
    get_tree_branches(nx, ny, length * 0.75, angle + 25, branches_list)

# Generate all branch coordinates
all_branches = []
get_tree_branches(WIDTH // 2, HEIGHT - 140, 95, 0, all_branches)

# Build frames progressively for the GIF animation
base_img = draw_background()

# Try loading a default font, fallback to default if unavailable
try:
    font_large = ImageFont.truetype("arial.ttf", 28)
    font_med = ImageFont.truetype("arial.ttf", 20)
except:
    font_large = font_med = ImageFont.load_default()

# Frame 1-3: Text messages appear
img_f1 = base_img.copy()
d1 = ImageDraw.Draw(img_f1)
# Updated greeting text here:
d1.text((WIDTH//2, 60), "✨ Hello TEMU ✨", fill="#ff3366", font=font_large, anchor="mm")
for _ in range(4): frames.append(img_f1)

img_f2 = img_f1.copy()
d2 = ImageDraw.Draw(img_f2)
d2.text((WIDTH//2, 100), "🐍 Welcome back to Python 🐍", fill="#00f2fe", font=font_med, anchor="mm")
for _ in range(4): frames.append(img_f2)

img_f3 = img_f2.copy()
d3 = ImageDraw.Draw(img_f3)
d3.text((WIDTH//2, 140), "How are you today?", fill="#ffe600", font=font_med, anchor="mm")
for _ in range(4): frames.append(img_f3)

# Frame 4-15: Branches grow progressively
current_img = img_f3.copy()
for i in range(1, len(all_branches) + 1, max(1, len(all_branches) // 8)):
    frame_img = current_img.copy()
    draw = ImageDraw.Draw(frame_img)
    for b in all_branches[:i]:
        draw.line([b[0], b[1]], fill="#4a2e1b", width=max(2, int(b[2] / 8)))
    frames.append(frame_img)
    current_img = frame_img

# Frame 16: Full tree + Leaves bloom
leaf_img = current_img.copy()
draw_leaves = ImageDraw.Draw(leaf_img)
leaf_colors = ["#ffb7b2", "#ff9aa2", "#e2f0cb", "#b5ead7", "#c7ceea"]
random.seed(50)
leaf_tips = []
for b in all_branches:
    if b[2] < 20:
        leaf_tips.append(b[1])
        lx, ly = b[1]
        color = random.choice(leaf_colors)
        draw_leaves.ellipse([lx-5, ly-5, lx+5, ly+5], fill=color)

for _ in range(6): frames.append(leaf_img)

# Frame 17-20: Colorful glowing fruits pop up
fruit_img = leaf_img.copy()
draw_fruit = ImageDraw.Draw(fruit_img)
fruit_colors = ["#ff2a2a", "#ff8c00", "#ffd700", "#ff1493", "#da70d6"]
for lt in random.sample(leaf_tips, k=min(15, len(leaf_tips))):
    fx, fy = lt
    fc = random.choice(fruit_colors)
    draw_fruit.ellipse([fx-6, fy-6, fx+6, fy+6], fill=fc)
    draw_fruit.ellipse([fx-2, fy-2, fx+1, fy+1], fill="#ffffff")

for _ in range(10): frames.append(fruit_img)

# Save as animated GIF
frames[0].save(
    "hello_temu.gif",
    save_all=True,
    append_images=frames[1:],
    optimize=False,
    duration=150,
    loop=0
)

print("Success! Animated GIF saved as 'hello_temu.gif'.")