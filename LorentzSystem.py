import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


'''
Lorentz is a tool to plot the strange attractor of the Lorentz system
'''
class Lorentz  :
	
	sigma = 10.0
	ro = 28.0
	beta = 2.667
	
	def __init__(self, number_of_evolutions, dt):
		self.number_of_evolutions = number_of_evolutions
		
		self.dt = dt 
	
		
	def lorentz_attractor (self, x0, y0, z0) :
		X = np.empty(self.number_of_evolutions +	1)
		Y = np.empty(self.number_of_evolutions +	1)
		Z = np.empty(self.number_of_evolutions +	1)
		

		itterations = np.linspace(0, self.number_of_evolutions )
		
		X[0] = x0
		Y[0] = y0
		Z[0] = z0
		
		for i in range(self.number_of_evolutions):
			x_dot = self.sigma * ( Y[i] - X[i] )
			y_dot = X[i] * (self.ro - Z[i]) - Y[i]
			z_dot = X[i] * Y[i] - self.beta * Z[i]
		
		
			X[i+1] = X[i] + (x_dot * self.dt ) 
			Y[i+1] = Y[i] + (y_dot * self.dt ) 
			Z[i+1] = Z[i] + (z_dot * self.dt ) 
			
		
		fig = plt.figure()
		ax = plt.axes(projection='3d')
		ax.plot3D(X, Y, Z, lw=0.5)
		ax.set_xlabel('X Axis')
		ax.set_ylabel('Y Axis')
		ax.set_zlabel('Z Axis')
		ax.set_title('Lorenz Strange Attractor')
		
		plt.show()
		
		
		
if __name__ == '__main__':
	l = Lorentz(10000, 0.01)
	
	l.lorentz_attractor(0, 1.0, 1.05)
	
	
