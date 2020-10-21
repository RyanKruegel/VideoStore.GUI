"""
Program: videoStoreGUI.py
Author: Ryan 10/21/2020

GUI-based version of the videoStore.py application

"""


from breezypythongui import EasyFrame
from tkinter.font import Font

class Rental(EasyFrame):

	def __init__(self):
		"""Sets up the window and the widgets."""
		EasyFrame.__init__(self, title = "Ryan's VideoRama", background = "lightgreen")
				# create a variable to store a font object
		myFont = Font(family = "Helvetica", size = 10, weight = "bold")

		# Add the label widgets		
		self.addLabel(text = "Which Videos Are Out For Rent?", row = 0, column = 0, background = "lightgreen", font = myFont)
		self.addLabel(text = "New Movies", row = 1, column = 0, background = "lightgreen", font = myFont)
		self.addLabel(text = "Old Movies", row = 2, column = 0, background = "lightgreen", font = myFont)
		self.addLabel(text = "Total Cost", row = 4, column = 0, background = "lightgreen", font = myFont)
		
		# add the entry field widgets
		self.newMovies = self.addIntegerField(value = 0, row = 1, column = 0)		
		self.oldMovies = self.addIntegerField(value = 0, row = 2, column = 0)
		self.totalCost = self.addIntegerField(value = 0.00, row = 4, column = 0)

		# add the command button
		self.addButton(text = "Purchase", row = 3, column = 0, columnspan = 2, command = self.rental)

	# Event handling method
	def rental(self):
			# Variables and constants 
	
			newMovies = 3.00
			oldMovies = 2.00
			totalCost = newMovies + oldMovies

			# for loop to determine the total cost of the movies rented
			totalCost = (newMovies * 3) + (oldMovies * 2)
			if newMovies + oldMovies == totalCost:
						result == totalCost

			# output of the total cost
			self.totalCost.setNumber(totalCost)

			print("The customer is renting " + str(newMovies) + " New Movie(s). And " + str(oldMovies) + " Old Movie(s).") 
			print("The total charge is: $" + str(totalCost))


# definition of the main() function
def main():
	Rental().mainloop()

	# global call to main()
main()