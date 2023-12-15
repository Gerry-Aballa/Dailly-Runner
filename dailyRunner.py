import datetime
import random
import os

readme_path = "README.md"
color_state_file = "colorState.txt"


current_date = datetime.datetime.utcnow().strftime("%Y-%m-%d")

emojis = ["😊", "🚀", "🎉", "💻", "🌟", "🐍", "🔥"]
random_emoji = random.choice(emojis)

if os.path.exists(color_state_file):
    with open(color_state_file, "r") as color_file:
        color_state = color_file.read().strip()
else:
    color_state = "blue"

if color_state == "blue":
    color_style = "blue"
    color_state = "green"
else:
    color_style = "green"
    color_state = "blue"
    
with open(color_state_file, "w") as color_file:
    color_file.write(color_state)

updated_content = f"- This README was last updated on <span style='color:{color_style};'>**{current_date}**</span> {random_emoji}\n"

with open(readme_path, "a") as readme_file:
    readme_file.write(updated_content)

print(f"Updated {readme_path} with the current date.")