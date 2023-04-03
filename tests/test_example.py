from dataclasses import dataclass

from pytest import fail, mark

from paul6325106.pytesttabulateformatter import fail


@dataclass
class Sandwich:
    name: str
    meat: bool
    dairy: bool


def pytest_generate_tests(metafunc):
    argnames = ['sandwich']
    argvalues = []
    ids = []

    argvalues.append([Sandwich('Ham Sandwich', True, False)])
    ids.append('Ham Sandwich')

    argvalues.append([Sandwich('Cheese Sandwich', False, True)])
    ids.append('Cheese Sandwich')

    argvalues.append([Sandwich('Ham and Cheese Sandwich', True, True)])
    ids.append('Ham and Cheese Sandwich')

    argvalues.append([Sandwich('Peanut Butter and Jam Sandwich', False, False)])
    ids.append('Peanut Butter and Jam Sandwich')

    metafunc.parametrize(argnames=argnames, argvalues=argvalues, ids=ids)


@mark.tabulate_formatted(title='Sandwiches containing dairy', headers='keys')
def test_sandwich_should_not_contain_dairy(sandwich):
    if sandwich.dairy:
        fail(row_data={'Name': sandwich.name})


@mark.tabulate_formatted(title='Sandwiches containing meat', headers='keys')
def test_sandwich_should_not_contain_meat(sandwich):
    if sandwich.meat:
        fail(row_data={'Name': sandwich.name})
