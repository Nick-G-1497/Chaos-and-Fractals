import numpy as np 
import matplotlib.pyplot as plt

class BifurcationDiagram:
	''' Bifurcation Diagram is a class generated and used in order to investagate and explore the logistic map's bifurcation diagram'''
	
	resolution = 500
	max_itt = 2000
	x0 = 10
	
	def __init__ (self):
		i = 0
		self.rate_space = []
		while(i < 4):
			i = i + .1
			self.rate_space.append(i)
			
		
	
	def get_rate_space (self):
		''' Define a linear space of discrete numbers. Save into an itterable. This is basically the same thing as np.linspace() but not conbined to numpy types as it is an object in raw python '''
		return self.rate_space
	

	def logistic_equation (self, r, x):
		''' This function returns the fundamental function which being called itteratively creates our fractal behavior 
		
		X_n+1 = rx(1 - x) '''
		
		return r * x * (1 - x)
	
		
	def plot(self):
		
		rate_space = np.linspace(0.7,4,10000)
		m=0.7
		# Initialize your data containers identically
		X = []
		Y = []
		# l is never used, I removed it.
		for r in rate_space:
		    # Add one value to X instead of resetting it.
		    X.append(r)
		    xn = np.random.random()
		    for n in range(self.max_itt):
		      xn = self.logistic_equation(r, xn)
		    Y.append(xn)
		# Remove the line between successive data points, this renders
		# the plot illegible. Use a small marker instead.
		plt.plot(X, Y, ls='', marker=',')
		plt.xlabel('Rate (r)')
		plt.ylabel('Steady State Solution')
		plt.title('Logistic Map Bifurcation Diagram')
		plt.show()
			
if __name__ == '__main__':
	''' Main block of code that gets executed '''
	b = BifurcationDiagram() 
	plt.figure()
	b.plot()
