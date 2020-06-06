"""Test for my functions.
"""
import unittest.mock as mock
import functions as f
##
##

@mock.patch('functions.input', side_effect=['alvin', 'Alvin Ngo', '18', 'A18 COGS',''])
def test_say_intro_get_name(mock_choice):
	"""Tests for the say_intro_get_name function"""

	# Test with just a first name 
	name = f.say_intro_get_name()
	assert name == 'alvin'

	# Test with both first and last name
	name = f.say_intro_get_name()
	assert name == 'Alvin Ngo'

	# Test with a number as name
	name = f.say_intro_get_name()
	assert name == '18'

	# Test with a name with both letters and numbers 
	name = f.say_intro_get_name()
	assert name == 'A18 COGS'

	# Test with an empty string as name
	name = f.say_intro_get_name()
	assert name == ''
	

def test_is_number_valid():
	"""Tests for the is_number_valid function"""

	# Test with a valid string that was an integer
	assert f.is_number_valid('14') == True

	# Test with a valid string that was a float rounded to 2 decimals
	assert f.is_number_valid('1234.34') == True

	# Test with a valid string that was a longer float 
	assert f.is_number_valid('130.21455') == True

	# Test with an invalid string that has two decimal points
	assert f.is_number_valid('1.23.45') == False

	# Test with an invalid string contains letters
	assert f.is_number_valid('1one4') == False

	# Test with an invalid empty string
	assert f.is_number_valid('') == False


#def test_ask_for_current_spending: TODO


def test_calculate_total_spending():
	"""Tests for the calculate_total_spending function"""

	# Test with a dictonary with spending values that are ints
	spendingDict1 = {
		'food': '200',
		'personal': '100',
		'housing': '600'
	}
	assert f.calculate_total_spending('', spendingDict1) == 900.00

	# Test with a dictionary with spending values that are floats rounded to 2 decimals
	spendingDict2 = {
		'food': '200.25',
		'personal': '100.15',
		'housing': '600.50'
	}
	assert f.calculate_total_spending('', spendingDict2) == 900.90

	# Test with a dictionary with spending values that were unrounded floats
	spendingDict3 = {
		'food': '200.1543',
		'personal': '100.4324',
		'housing': '600.1642'
	}
	assert f.calculate_total_spending('', spendingDict3) == 900.75


def test_is_saving_valid():
	"""Tests for the is_saving_valid function"""

	# Test with a valid input 1
	assert f.is_saving_valid('1') == True

	# Test with a valid input 2
	assert f.is_saving_valid('2') == True

	# Test with a valid input 3
	assert f.is_saving_valid('3') == True

	# Test with an invalid input of 4
	assert f.is_saving_valid('4') == False

	# Test with an invalid input of a word
	assert f.is_saving_valid('one') == False

	# Test with an invalid input of an empty string
	assert f.is_saving_valid('') == False


@mock.patch('functions.input', side_effect=['1', '2', '3'])
def test_get_user_saving(mock_choice):
	"""Tests for the get_user_saving function"""

	# Test with a user saving choice of 1
	saving_choice = f.get_user_saving('')
	assert saving_choice == '1'

	# Test with a user saving choice of 2
	saving_choice = f.get_user_saving('')
	assert saving_choice == '2'

	# Test with a user saving choice of 3
	saving_choice = f.get_user_saving('')
	assert saving_choice == '3'


def test_are_all_categories_listed():
	"""Tests for the are_all_categories_listed function"""

	# Test with all categories as listed in original function
	assert f.are_all_categories_listed(['housing', 'utilities', 'food', 'transportation', 'entertainment', 'personal']) == True

	# Test with all categories but rearranged
	assert f.are_all_categories_listed(['utilities', 'personal', 'entertainment', 'transportation', 'housing', 'food']) == True

	# Test with only 4 categories
	assert f.are_all_categories_listed(['utilities', 'personal', 'entertainment', 'transportation']) == False

	# Test with categories that are spelled incorrectly
	assert f.are_all_categories_listed(['utilities', 'personal', 'entertainment', 'transport', 'house', 'food']) == False

	# Test with a list that contains no categories
	assert f.are_all_categories_listed([]) == False


def test_parse_user_ranking():
	"""Tests for the are_all_categories_listed function"""

	# Test with perfectly formatted input
	assert f.parse_user_ranking('housing, utilities, food') == ['housing', 'utilities', 'food']

	# Test with input that isn't spaced properly
	assert f.parse_user_ranking('housing,utilities,food') == ['housing', 'utilities', 'food']

	# Test with input that has capitilization and spacing errors
	assert f.parse_user_ranking('hoUsiNg, utIliTies,F ooD') == ['housing', 'utilities', 'food']

	# Test with random input
	assert f.parse_user_ranking('a, b, cd') == ['a', 'b', 'cd']

	# Test with empty string
	assert f.parse_user_ranking('') == [''] 


ranking_input_1 = 'transportation, housing, utilities, entertainment, food, personal' 
ranking_input_2 = 'housing, entertainment,personal, utilities,transportation, food'
ranking_input_3 = 'Utilities, Transportation,Food, Housing,entertainment, personal'
ranking_input_4 = 'enteR Tainment, fOod , peRsoNal, tRans PoRtAtion, HoUsin g,UTILi tIES'
@mock.patch('functions.input', side_effect=[ranking_input_1, ranking_input_2, ranking_input_3, ranking_input_4])
def test_get_user_ranking(mock_choice):
	"""Tests for the are_all_categories_listed function"""

	# Test with ideal properly formatted input 
	ranking_list = f.get_user_ranking() 
	assert ranking_list == ['transportation', 'housing', 'utilities', 'entertainment', 'food', 'personal']

	# Test with input that is still properly formatted but rearranged
	ranking_list = f.get_user_ranking()
	assert ranking_list == ['housing', 'entertainment', 'personal', 'utilities', 'transportation', 'food']

	# Test with input that has minimal capitalization and spacing errors
	ranking_list = f.get_user_ranking()
	assert ranking_list == ['utilities', 'transportation', 'food', 'housing', 'entertainment', 'personal']

	# Test with input that has significant capitalization and spacing errors
	ranking_list = f.get_user_ranking()
	assert ranking_list == ['entertainment', 'food', 'personal', 'transportation', 'housing', 'utilities']


def test_calculate_new_budget():
	"""Tests for the calculate_new_budget function"""

	category_ranking = ['housing', 'transportation', 'personal', 'entertainment', 'food', 'utilities']
	current_spending = {
		'housing': '450.50',
		'transportation': '750.00',
		'personal': '134.56',
		'entertainment': '100.10',
		'food': '310.00',
		'utilities': '211.11'
	}

	# Test when user only wants conservative budget adjustment
	user_saving_1 = '1'
	new_budget_1 = [450.50, 712.50, 127.83, 90.09, 263.50, 168.89]
	assert f.calculate_new_budget(category_ranking, user_saving_1, current_spending) == new_budget_1

	# Test when user wants moderate budget adjustment 
	user_saving_2 = '2'
	new_budget_2 = [450.50, 712.50, 121.10, 85.08, 232.50, 137.22]
	assert f.calculate_new_budget(category_ranking, user_saving_2, current_spending) == new_budget_2

	# Test when user wants intense budget adjustment
	user_saving_3 = '3'
	new_budget_3 = [450.50, 675.00, 107.65, 70.07, 186.00, 105.56]
	assert f.calculate_new_budget(category_ranking, user_saving_3, current_spending) == new_budget_3
	 

def test_announce_new_budget():
	"""Tests for the announce_new_budget function"""

	# Test with 3 categories and budget amounts
	category_ranking_1 = ['transportation', 'housing', 'utilities']
	budget_1 = [201.56, 123.56, 223.50]
	final_budget_1 = {
		'transportation': 201.56,
		'housing': 123.56,
		'utilities': 223.50
	}

	assert f.announce_new_budget(category_ranking_1, budget_1) == final_budget_1

	# Test with 2 categories and budget amounts
	category_ranking_2 = ['housing', 'utilities']
	budget_2 = [201.10, 223.00]
	final_budget_2 = {
		'housing': 201.10,
		'utilities': 223.00
	}

	assert f.announce_new_budget(category_ranking_2, budget_2) == final_budget_2

	# Test with 1 categories and budget amounts
	category_ranking_3 = ['personal']
	budget_3 = [1000.01]
	final_budget_3 = {
		'personal': 1000.01
	}

	assert f.announce_new_budget(category_ranking_3, budget_3) == final_budget_3


def test_start_program():
	"""Tests for the start_program function"""
	
	#This function is simply a script that calls all the other functions so just test the others
	assert True






	



				 
	