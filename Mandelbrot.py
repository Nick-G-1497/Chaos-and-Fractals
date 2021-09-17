import numpy as np
import matplotlib.pyplot as plt

class Mandelbrot:
	'''Modular class which allows the user to generate the Mandelbrot set'''
	resolution = 512
	max_itt = 1024
	real_axis = np.linspace(-3, 3, resolution)
	imaginary_axis = np.linspace(-3, 3, resolution)
	
	def optimized_escape_time(self, x0, y0):
		''' Optimized Algorithm to determine if a numbe r escapes the set in a reasonably amount of itterations - optimization comes directly from wikipedia ''' 
		x_squared = 0
		j_squared = 0
		w = 0
		i = 0
	
		while ( (x_squared + j_squared) <= 4 and i < self.max_itt):
			x =  x_squared - j_squared + x0
			y = w - x_squared - j_squared + y0 
			x_squared = x * x
			w = (x + y) * (x + y)
			i = i + 1
			
		return i
		
	def escape_time(self, x0, j0):
		'''Return the number of itterations it takes to blow up starting at a particular starting point'''
		c = np.complex(x0, j0)
		i = 0
		z = 0
		while (abs(z) <= 2 and i < self.max_itt) :
			z = (z*z) + c
			i = i+1
		return i 
	
	def plot_optimized(self):
		''' Plot using the optimized algorithm from wikipedia'''
		for x in self.real_axis:
			for j in self.imaginary_axis:
				escape_time = self.optimized_escape_time(x, j)
				if(escape_time < self.max_itt):
					plt.scatter(x, j, sz=.1)
		plt.show()
		
	def plot(self):
		''' Plot using the complex data type built into python '''
		plt.figure()
		plt.title('Mandelbrot Set')
		plt.axis('equal')
		plt.xlabel('Real Axis')
		plt.ylabel('Imaginary Axis')
		for x in self.real_axis:
			for j in self.imaginary_axis:
				escape_itt = self.escape_time(x, j)
				if(escape_itt >= self.max_itt):
					plt.scatter(x, j, 1)
		plt.show()
		
	def plot_with_color(self):
		''' Plot the Mandelbrot set and additionally add in some color shading to represent the speed at which the value exits the set'''
		plt.figure()
		plt.title('Mandelbrot Set')
		plt.axis('equal')
		plt.xlabel('Real Axis')
		plt.ylabel('Imaginary Axis')
		for x in self.real_axis:
			for j in self.imaginary_axis:
				escape_itt = self.escape_time(x, j)
				plt.scatter(x,
				            j, 
				            c = self.color_map(escape_itt))
							
		plt.show()	
	
	def color_map(self, itt):
		'''Returns a color mapping from the escape time itteration'''
		if itt >= self.max_itt:
			return 'b'
		if itt < 500:
			return 'y'
		if itt < 700:
			return 'g'
		if itt < self.max_itt:
			return 'r'
	
			
		
			
if __name__ == '__main__':
	''' Main code block to execute when we're using this as the main code block'''
	m = Mandelbrot()
	m.plot()

