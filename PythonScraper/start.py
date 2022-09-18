import urllib.request
from colorthief import ColorThief
import webcolors

image_url = "https://tr.rbxcdn.com/f709e2ec304b50f1129658a2bdcce7bb/420/420/Hat/Png"

urllib.request.urlretrieve(image_url, "gfg.png")

color_thief = ColorThief('gfg.png')
# get the dominant color
dominant_color = color_thief.get_color(quality=1)
# build a color palette
palette = color_thief.get_palette(color_count=6)

print(palette)
def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name

actual_name, closest_name = get_colour_name(dominant_color)

for color in palette:
    print(f"Actual colour name: {actual_name} \n closest colour name: {closest_name}")
