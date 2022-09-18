import requests
import json
import urllib.request
from colorthief import ColorThief
import webcolors

webcolors_dict = {
    "aliceblue": "White",
    "antiquewhite": "Blonde",
    "aqua": "Blue",
    "aquamarine": "Green",
    "beige":"Blonde",
    "bisque":"Blonde",
    "black":"Black",
    "azure":"White",
    "blanchedalmond":"Blonde",
    "blue":"Blue",
    "blueviolet":"Purple",
    "brown":"Brown",
    "burlywood":"Blonde",
    "cadetblue":"Blue",
    "chocolate":"Brown",
    "coral":"Brown",
    "cornflowerblue":"Blue",
    "chartreuse":"Green",
    "cornsilk":"White",
    "crimson":"Red",
    "cyan":"Blue",
    "darkblue":"Blue",
    "darkcyan":"Blue",
    "darkgoldenrod":"Brown",
    "darkgray":"White",
    "darkgreen":"Green",
    "darkgrey":"White",
    "darkkhaki":"Blonde",
    "darkmagenta":"Purple",
    "darkolivegreen":"Brown",
    "darkorange":"Orange",
    "darkorchid":"Purple",
    "darkred":"Red",
    "darksalmon":"Pink",
    "darkseagreen":"Green",
    "darkslateblue":"Blue",
    "darkslategray":"Black",
    "darkslategrey":"Black",
    "darkturquoise":"Blue",
    "darkviolet":"Purple",
    "deeppink":"Pink",
    "deepskyblue":"Blue",
    "dimgray":"Black",
    "dimgrey":"Black",
    "dodgerblue":"Blue",
    "firebrick":"Red",
    "floralwhite":"White",
    "forestgreen":"Green",
    "fuchsia":"Pink",
    "gainsboro":"White",
    "ghostwhite":"White",
    "gold":"Blonde",
    "goldenrod":"Blonde",
    "gray":"Black",
    "green":"Green",
    "greenyellow":"Green",
    "grey":"Black",
    "honeydew":"White",
    "hotpink":"Pink",
    "indianred":"Red",
    "indigo":"Purple",
    "ivory":"White",
    "khaki":"Blonde",
    "lavender":"White",
    "lavenderblush":"White",
    "lawngreen":"Green",
    "lemonchiffon":"Blonde",
    "lightblue":"Blue",
    "lightcoral":"Red",
    "lightcyan":"Blue",
    "lightgoldenrodyellow":"Blonde",
    "lightgray":"White",
    "lightgreen":"Green",
    "lightgrey":"White",
    "lightpink":"Pink",
    "lightsalmon":"Red",
    "lightseagreen":"Green",
    "lightskyblue":"Blue",
    "lightslategray":"Black",
    "lightslategrey":"Black",
    "lightsteelblue":"Blue",
    "lightyellow":"Blonde",
    "lime":"Green",
    "limegreen":"Green",
    "linen":"White",
    "magenta":"Pink",
    "maroon":"Brown",
    "mediumaquamarine":"Green",
    "mediumblue":"Blue",
    "mediumorchid":"Purple",
    "mediumpurple":"Purple",
    "mediumseagreen":"Green",
    "mediumslateblue":"Purple",
    "mediumspringgreen":"Green",
    "mediumturquoise":"Blue",
    "mediumvioletred":"Purple",
    "midnightblue":"Blue",
    "mintcream":"White",
    "mistyrose":"Pink",
    "moccasin":"Blonde",
    "navajowhite":"Blonde",
    "navy":"Blue",
    "oldlace":"Blonde",
    "olive":"Green",
    "olivedrab":"Green",
    "orange":"Red",
    "orangered":"Red",
    "orchid":"Purple",
    "palegoldenrod":"Blonde",
    "palegreen":"Green",
    "paleturquoise":"Blue",
    "palevioletred":"Purple",
    "papayawhip":"Blonde",
    "peachpuff":"Blonde",
    "peru":"Brown",
    "pink":"Pink",
    "plum":"Purple",
    "powderblue":"Blue",
    "purple":"Purple",
    "red":"Red",
    "rosybrown":"Brown",
    "royalblue":"Blue",
    "saddlebrown":"Brown",
    "salmon":"Red",
    "sandybrown":"Blonde",
    "seagreen":"Green",
    "seashell":"White",
    "sienna":"Brown",
    "silver":"White",
    "skyblue":"Blue",
    "slateblue":"Blue",
    "slategray":"Black",
    "slategrey":"Black",
    "snow":"White",
    "springgreen":"Green",
    "steelblue":"Blue",
    "tan":"Blonde",
    "teal":"Green",
    "thistle":"Purple",
    "tomato":"Red",
    "turquoise":"Blue",
    "violet":"Purple",
    "wheat":"Blonde",
    "white":"White",
    "whitesmoke":"White",
    "yellow":"Blonde",
    "yellowgreen":"Green",
}

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


colors = ["Black", "Brown", "Blonde", "Pink", "White", "Red", "Blue", "Green", "Pink", "Purple", "Rainbow"]
name = "B&B Messy Buns"
name = name.split()
color_arr = []
for name in name:
    if name.capitalize() in colors or name.lower() in colors:
        color_arr.append(name.capitalize)
    if name == "Blond":
        color_arr.append("Blonde")
    if name == "Brunette":
        color_arr.append("Brown")

if len(color_arr) != 1:
    urllib.request.urlretrieve("https://tr.rbxcdn.com/388b10425d15f4b1d51b1a7ecffe30ea/420/420/Hat/Png", "temp.png")

    color_thief = ColorThief('temp.png')
    # get the dominant color
    dominant_color = color_thief.get_color(quality=1)
    actual_name, closest_color = get_colour_name(dominant_color)
    color_guess = webcolors_dict[closest_color]
    print(closest_color)
    if color_guess in color_arr:
        print(color_guess)
    elif len(color_arr) > 0:
        print(color_arr.pop())
    else:
        print(color_guess)

else:
    print(color_arr.pop())
    