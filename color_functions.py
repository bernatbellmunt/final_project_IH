import math
import PIL
import extcolors
import numpy as np
import urllib.request
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
from matplotlib import gridspec
import pandas as pd

# group of functions -> it will return my image + the color palette that's been used 
def study_image(img):
  im = Image.open(img)
  colors = extract_colors(img)
  color_palette = render_color_platte(colors)
  return overlay_palette(img, color_palette)

# function that extracts the color codes of the image - palette in codes
#tolerance = group colors (0 does not group colors)
# i want to get 10 colors max per painting
def extract_colors(img):
  im = Image.open(img)
  tolerance = 32
  limit = 10
  colors = extcolors.extract_from_image(im, tolerance, limit)
  #I remove white, as it is the margin of the picture
  for e in colors:
    if e == (255, 255, 255):
      colors.remove(e)
  return colors


# this transforms color code into the color palette
def render_color_platte(colors):
  size = 100
  columns = 6
  width = int(min(len(colors), columns) * size)
  height = int((math.floor(len(colors) / columns) + 1) * size)
  result = Image.new("RGBA", (width, height), (0, 0, 0, 0))
  canvas = ImageDraw.Draw(result)
  for idx, color in enumerate(colors):
      x = int((idx % columns) * size)
      y = int(math.floor(idx / columns) * size)
      canvas.rectangle([(x, y), (x + size - 1, y + size - 1)], fill=color[0])
  return result


# groups image and color palette rectangle
def overlay_palette(img, color_palette):
  img = Image.open(img)
  nrow = 2
  ncol = 1
  f = plt.figure(figsize=(10,10), facecolor='None', edgecolor='k', dpi=55, num=None)
  gs = gridspec.GridSpec(nrow, ncol, wspace=0.0, hspace=0.0) 
  f.add_subplot(2, 1, 1)
  plt.imshow(img, interpolation='nearest')
  plt.axis('off')
  f.add_subplot(1, 2, 2)
  plt.imshow(color_palette, interpolation='nearest')
  plt.axis('off')
  plt.subplots_adjust(wspace=0, hspace=0, bottom=0)
  plt.show(block=True)


# given the column of img_names, it returns the palette list of all images
def get_palette_list (col_images):
    palettelist=[]
    for cuadro in col_images:
        try:
            path = f"images/prado_paintings/{cuadro}"

            #study_image(path)
            palettelist.append(extract_colors(path))
        except:
            palettelist.append([])
            pass
    return palettelist

#given the a list of palettes (from different pics)-> returns the top 3 colors used in the images
def get_top3_colors(palettelist):
    all_color=[]
    for palette in palettelist:
        for color in palette:
            all_color.append(color)
    count1=0
    count2=0
    count3=0
    
    col1=()
    col2=()
    col3=()
    
    for c in all_color:
        curr_frequency = all_color.count(c)
        if curr_frequency> count1:
            count1 = curr_frequency
            col1 = c

        elif curr_frequency> count2:
            count2= curr_frequency
            col2=c

        elif curr_frequency> count3:
            count3= curr_frequency
            col3=c

    return [col1,col2,col3]


# given a column with images names -> gives me TOP 3 colors or TOP 3 color codes

def color3_from_dataframe (column):
    lista_paleta = get_palette_list(column)
    main_colors = get_top3_colors(lista_paleta)
    return render_color_platte(main_colors)

def color3_codes (column):
    lista_paleta = get_palette_list(column)
    return get_top3_colors(lista_paleta)

# given the column of the img_names it returns me a list with all the colors codes that are in an image
def get_all_color_codes (column):
    all_col = []
    for pic in column:
        try:
            path = f"images/prado_paintings/{pic}"
            col_list = extract_colors(path)
            all_col.append(col_list)
        except:
            all_col.append([])
            print(f"the {pic} is damaged")
            pass
    return all_col
        

    