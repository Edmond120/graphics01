import random

def header(file, file_type, width, height, max_color_value):
	file.write(file_type + '\n' + str(width) + ' ' + str(height) + '\n' + str(max_color_value) + '\n')

def write_pixel(file,r,g,b):
	file.write(str(r) + ' ' + str(g) + ' ' + str(b))

def main():
	random.seed()
	file = open('images/image.ppm','w')
	header(file,"P3",1000,1000,255)
	R = range(0,1000)
	for y in R:
		for x in R:
			r = int((x / 1000.0) * 255)
			g = int(random.random() * r)
			b = int(random.random() * (int((y / 1000.0) * 255)))
			write_pixel(file,r,g,b)
			if(x != 999):
				file.write(' ')
		file.write('\n')
	file.close()

if __name__ == '__main__':
	main()
