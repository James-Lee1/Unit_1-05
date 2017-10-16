# Created by: James Lee
# Created on: Sep 2017
# Created for: ICS3U
# This program calculates the price of a pizza given its diameter

import ui

# Declare constants

HST = 1.13
COST_PER_INCH = 0.5
LABOUR_COST = 1.75

def pizza_calculate_button_touch_up_inside(sender):
	
	# Calculates cost of pizza given diameter
	
	# Input
	diameter = float(view['diameter_textbox'].text)
	
	# Ensures pizza cannot be non existent
	if diameter < 0:
		view['validity_label'].text = 'Sorry, not a valid diameter'
	
	# Ensures pizza cannot be non existent
	elif diameter == 0:
		view['validity_label'].text = 'Sorry, not a valid diameter'
	
	else:		
		
		view['validity_label'].text = ''
		
		# Process
		price = HST * (COST_PER_INCH * diameter + LABOUR_COST)
	
		# Output
		view['price_label'].text = 'The price is $%.2f' %price
	
view = ui.load_view()
view.present('full_screen')
