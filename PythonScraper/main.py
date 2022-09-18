from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import random
import time
import requests
import json
import urllib.request
from colorthief import ColorThief
import webcolors

colors = ["Black", "Brown", "Blonde", "White", "Red", "Blue", "Green", "Pink", "Purple", "Rainbow"]

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

def getColor(name, image_url):
    name = name.split()
    color_arr = []
    for name in name:
        if name.capitalize() in colors or name.lower() in colors:
            color_arr.append(name.capitalize())
        if name == "Blond" or name == "Yellow":
            color_arr.append("Blonde")
        if name == "Brunette" or name == "Caramel" or name == "Ginger":
            color_arr.append("Brown")

    if len(color_arr) != 1:
        urllib.request.urlretrieve(image_url, "temp.png")

        color_thief = ColorThief('temp.png')
        # get the dominant color
        dominant_color = color_thief.get_color(quality=1)
        actual_name, closest_color = get_colour_name(dominant_color)
        color_guess = webcolors_dict[closest_color]

        if color_guess in color_arr:
            return color_guess
        elif len(color_arr) > 0:
            color = color_arr[0]
            return color
        else:
            return color_guess
    else:
        color = color_arr[0]
        return color

driver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://www.roblox.com/catalog?Category=14&Subcategory=20"
driver.maximize_window()
driver.get(url)
time.sleep(5)

content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content, 'lxml')

with open(f'data/items.txt', 'w') as f:
    f.write("[")

newPage = None
while newPage == None:
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content, 'lxml')
    catalog_items = soup.find_all('li', class_ = 'list-item item-card ng-scope')
    for item in catalog_items:
        name = item.find('a', class_='item-card-container')['title']
        thumbnail_container = item.find('span', class_='thumbnail-2d-container')
        item_id = thumbnail_container['thumbnail-target-id']
        image_url = thumbnail_container.find('img', src=True)['src']
        color = getColor(name, image_url)
        with open(f'data/items.txt', 'a') as f:
            f.write("\n    {\n")
            f.write(f"    \"item_id\": \"{item_id}\",\n")
            f.write(f"    \"image_url\": \"{image_url}\",\n")
            f.write(f"    \"color\": \"{color}\"")
            f.write("\n    },")
        time.sleep(random.uniform(0,0.2))

    newPage = soup.find('li', class_="pager-next disabled")    
    driver.find_element_by_css_selector("a[ng-click=\"cursorPaging.loadNextPage()\"]").click()
    time.sleep(random.uniform(1, 2))

with open(f'data/items.txt', 'a') as f:
    f.write("\n]")

driver.quit()
