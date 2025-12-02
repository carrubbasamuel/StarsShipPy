from PIL import Image, ImageDraw

# Crea un'immagine della navicella
size = 50
img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Corpo principale della navicella (rettangolo arrotondato)
draw.ellipse([(5, 15), (45, 40)], fill=(0, 200, 255), outline=(0, 100, 200), width=2)

# Cabina (cerchio)
draw.ellipse([(18, 8), (32, 22)], fill=(100, 150, 255), outline=(0, 100, 200), width=2)

# Finestra della cabina
draw.ellipse([(20, 10), (30, 20)], fill=(150, 200, 255))

# Punta della navicella (triangolo)
points = [(25, 0), (15, 12), (35, 12)]
draw.polygon(points, fill=(0, 200, 255), outline=(0, 100, 200))

# Motori (due rettangoli ai lati)
draw.rectangle([(8, 30), (15, 42)], fill=(255, 100, 0), outline=(200, 50, 0), width=2)
draw.rectangle([(35, 30), (42, 42)], fill=(255, 100, 0), outline=(200, 50, 0), width=2)

# Fiamme dei motori
draw.polygon([(8, 42), (15, 42), (11, 48)], fill=(255, 200, 0))
draw.polygon([(35, 42), (42, 42), (38, 48)], fill=(255, 200, 0))

# Salva l'immagine
img.save('spaceship.png')
print("Navicella creata: spaceship.png")
