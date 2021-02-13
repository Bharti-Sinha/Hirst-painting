import colorgram

colors = colorgram.extract('photo.jpeg', 30)
rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    colours = (r, g, b)
    rgb_colors.append(colours)

print(rgb_colors)
