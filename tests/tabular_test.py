import pytest

from lathon import Tabular


def test_add_row_greater_than_spec():
    """
    Tests if a row with a lenght greater then the number os specs in a Tabular enviroment
    raises an Assertion Exception
    """
    tab = Tabular("c|c")
    with pytest.raises(AssertionError):
        row = [1, 2, 3]
        tab.addRow(row)
