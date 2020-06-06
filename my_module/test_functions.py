"""Test for my functions.
"""
import unittest.mock as mock
import functions as f
##
##

@mock.patch('functions.input', side_effect=['alvin', 'Ngo COGS', '18', ''])
def test_say_intro_get_name(mock_choice):

	name = f.say_intro_get_name()
	assert name == 'alvin'

	name = f.say_intro_get_name()
	assert name == 'Ngo COGS'

	name = f.say_intro_get_name()
	assert name == '18'

	name = f.say_intro_get_name()
	assert name == ''
	

def test_is_number_valid():

	assert f.is_number_valid('14') == True
	assert f.is_number_valid('1234.34') == True
	assert f.is_number_valid('130.21455') == True
	assert f.is_number_valid('1.23.45') == False
	assert f.is_number_valid('1one4') == False
	assert f.is_number_valid('') == False


#def test_ask_for_current_spending: TODO


def test_calculate_total_spending():

	spendingDict1 = {
		'food': '200',
		'personal': '100',
		'housing': '600'
	}
	assert f.calculate_total_spending('', spendingDict1) == 900.00

	spendingDict2 = {
		'food': '200.25',
		'personal': '100.15',
		'housing': '600.50'
	}
	assert f.calculate_total_spending('', spendingDict2) == 900.90

	spendingDict3 = {
		'food': '200.1543',
		'personal': '100.4324',
		'housing': '600.1642'
	}
	assert f.calculate_total_spending('', spendingDict3) == 900.75


def test_is_saving_valid():

	assert f.is_saving_valid('1') == True
	assert f.is_saving_valid('2') == True
	assert f.is_saving_valid('3') == True
	assert f.is_saving_valid('4') == False
	assert f.is_saving_valid('one') == False
	assert f.is_saving_valid('') == False


@mock.patch('functions.input', side_effect=['1', '2', '3'])
def test_get_user_saving(mock_choice):

	saving_choice = f.get_user_saving('')
	assert saving_choice == '1'

	saving_choice = f.get_user_saving('')
	assert saving_choice == '2'

	saving_choice = f.get_user_saving('')
	assert saving_choice == '3'


def test_are_all_categories_listed():

	assert f.are_all_categories_listed(['housing', 'utilities', 'food', 'transportation', 'entertainment', 'personal']) == True
	assert f.are_all_categories_listed(['utilities', 'personal', 'entertainment', 'transportation', 'housing', 'food']) == True
	assert f.are_all_categories_listed(['utilities', 'personal', 'entertainment', 'transportation']) == False
	assert f.are_all_categories_listed(['utilities', 'personal', 'entertainment', 'transport', 'house', 'food']) == False
	assert f.are_all_categories_listed([]) == False


def test_parse_user_ranking():

	assert f.parse_user_ranking('housing, utilities, food') == ['housing', 'utilities', 'food']
	assert f.parse_user_ranking('housing,utilities,food') == ['housing', 'utilities', 'food']
	assert f.parse_user_ranking('hoUsiNg, utIliTies,F ooD') == ['housing', 'utilities', 'food']
	assert f.parse_user_ranking('a, b, cd') == ['a', 'b', 'cd']
	assert f.parse_user_ranking('') == ['']


ranking_input_1 = 'transportation, housing, utilities, entertainment, food, personal' 
ranking_input_2 = 'housing, entertainment,personal, utilities,transportation, food'
ranking_input_3 = 'Utilities, Transportation,Food, Housing,entertainment, personal'
ranking_input_4 = 'enteR Tainment, fOod , peRsoNal, tRans PoRtAtion, HoUsin g,UTILi tIES'
@mock.patch('functions.input', side_effect=[ranking_input_1, ranking_input_2, ranking_input_3, ranking_input_4])
def test_get_user_ranking(mock_choice):

	ranking_list = f.get_user_ranking() 
	assert ranking_list == ['transportation', 'housing', 'utilities', 'entertainment', 'food', 'personal']

	ranking_list = f.get_user_ranking()
	assert ranking_list == ['housing', 'entertainment', 'personal', 'utilities', 'transportation', 'food']

	ranking_list = f.get_user_ranking()
	assert ranking_list == ['utilities', 'transportation', 'food', 'housing', 'entertainment', 'personal']

	ranking_list = f.get_user_ranking()
	assert ranking_list == ['entertainment', 'food', 'personal', 'transportation', 'housing', 'utilities']


def test_announce_new_budget():

	category_ranking_1 = ['transportation', 'housing', 'utilities']
	budget_1 = [201.56, 123.56, 223.50]
	final_budget_1 = {
		'transportation': 201.56,
		'housing': 123.56,
		'utilities': 223.50
	}

	assert f.announce_new_budget(category_ranking_1, budget_1) == final_budget_1

	category_ranking_2 = ['housing', 'utilities']
	budget_2 = [201.10, 223.00]
	final_budget_2 = {
		'housing': 201.10,
		'utilities': 223.00
	}

	assert f.announce_new_budget(category_ranking_2, budget_2) == final_budget_2

	category_ranking_3 = ['personal']
	budget_3 = [1000.01]
	final_budget_3 = {
		'personal': 1000.01
	}

	assert f.announce_new_budget(category_ranking_3, budget_3) == final_budget_3




def test_start_program():

	assert True






	



				 
	