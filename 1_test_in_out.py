# import pytest
# from .1_in_out
#
# @pytest.mark.parametrize('name', ['John', 'Smith', 'Timur'])
# def test_print_my_name(name):
#     assert name == 'John'
#
#
import pytest

from a1_in_out import print_team_winner, print_my_name, print_star_rect


@pytest.mark.parametrize('name', ['Барселона', 'Ливерпуль', 'Timur'])
def test_print_team_winner(mocker, name):
    mocker.patch('builtins.input', return_value=name)
    result = print_team_winner()
    assert result == f"{name} - чемпион!"


@pytest.mark.parametrize('name', ['John', 'Smith', 'Timur'])
def test_print_my_name_2(mocker, name):
    mocker.patch('builtins.input', return_value=name)
    result = print_my_name()
    assert result == f"Привет, {name}"


def test_print_rect():
    result = print_star_rect()
    assert result == """**********
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
**********"""