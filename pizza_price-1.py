# Created by: James Lee
# Created on: Sep 2017
# Created for: ICS3U
# This program calculates the price of a pizza given its diameter

import ui

def pizza_calculate_button_touch_up_inside(sender):
	
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
		price = 1.13 * (0.5 * diameter + 1.75)
	
		# Output
		view['price_label'].text = 'The price is $%.2f' %price
	
view = ui.load_view()
view.present('full_screen')
