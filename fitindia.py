import csv
from PIL import Image, ImageDraw
from PIL import ImageFont

filename = "fitindia.csv"
rows = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        rows.append(row)

rows.pop(0)
for row in rows:
    name = row[0]
    print (name)
    im = Image.open("fitindia.jpg")  # template image
    draw = ImageDraw.Draw(im)
    name_font = ImageFont.truetype("FuturaPTBook.otf", 100)
    wname, hname = draw.textsize(name, font=name_font)
    # print(wname, hname)
    draw.text((995+(1640/2)-(wname/2), 1440), name, (0, 0, 0), font=name_font, stroke_width=1)
    im.save("Athletics/"+name+".png", "PNG") # save in Athletics/file_name.png