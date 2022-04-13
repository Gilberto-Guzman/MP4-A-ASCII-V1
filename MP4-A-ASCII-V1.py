import os 
import sys

#Librerias Externas
import cv2
from PIL import Image

# Caracteres ASCII utilizados para crear la salida
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

#1
def Redimensionar_Imagen(image ,new_width=70):
	width,height = image.size
	aspect_ratio = height/width
	new_height = int(aspect_ratio * new_width)
	Redimensionar_Imagen = image.resize((new_width,new_height)).convert('L')
	return Redimensionar_Imagen

#2
def Pixeles_A_Caracteres(image):
	pixels = image.getdata()
	characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
	return characters

#3
def Generar_Imagen(image,new_width=70):
	new_image_data = Pixeles_A_Caracteres(Redimensionar_Imagen(image))
	total_pixels = len(new_image_data)
	ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, total_pixels, new_width)])
	sys.stdout.write(ascii_image)
	os.system('cls' if os.name == 'nt' else 'clear')

#Escogemos el video que queremos reproducir...
cap = cv2.VideoCapture("Video_De_Prueba.mp4")

#Ciclo principal
while True:
	ret,frame = cap.read()
	cv2.imshow("Video Original",frame)
	Generar_Imagen(Image.fromarray(frame))
	cv2.waitKey(1)