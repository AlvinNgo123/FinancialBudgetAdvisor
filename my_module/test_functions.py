"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from functions import is_number_valid, is_saving_valid, are_all_categories_listed, parse_user_ranking, start_program
##
##

def test_is_number_valid():

    assert is_number_valid('14') == True
    assert is_number_valid('1234.34') == True
    assert is_number_valid('130.21455') == True
    assert is_number_valid('1.23.45') == False
    assert is_number_valid('1one4') == False
    assert is_number_valid('') == False


def test_is_saving_valid():

	assert is_saving_valid('1') == True
	assert is_saving_valid('2') == True
	assert is_saving_valid('3') == True
	assert is_saving_valid('4') == False
	assert is_saving_valid('one') == False
	assert is_saving_valid('') == False


def test_are_all_categories_listed():

	assert are_all_categories_listed(['housing', 'utilities', 'food', 'transportation', 'entertainment', 'personal']) == True
	assert are_all_categories_listed(['utilities', 'personal', 'entertainment', 'transportation', 'housing', 'food']) == True
	assert are_all_categories_listed(['utilities', 'personal', 'entertainment', 'transportation']) == False
	assert are_all_categories_listed(['utilities', 'personal', 'entertainment', 'transport', 'house', 'food']) == False
	assert are_all_categories_listed([]) == False


def test_parse_user_ranking():

	assert parse_user_ranking('housing, utilities, food') == ['housing', 'utilities', 'food']
	assert parse_user_ranking('housing,utilities,food') == ['housing', 'utilities', 'food']
	assert parse_user_ranking('hoUsiNg, utIliTies,F ooD') == ['housing', 'utilities', 'food']
	assert parse_user_ranking('a, b, cd') == ['a', 'b', 'cd']
	assert parse_user_ranking('') == ['']


def test_start_program():

	assert True






    



                 
    