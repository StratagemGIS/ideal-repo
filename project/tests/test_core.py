from project.src import core

import pytest


test_cases = [
    (10.0, 20.0, 30.0),
    (100_000.0, -1.0, 99_999.0),
]


@pytest.mark.parametrize('num1, num2, expected', test_cases)
def test_add(num1, num2, expected):
    assert core.add(num1, num2) == expected


def test_add_failure():
    with pytest.raises(TypeError):
        core.add(10, 20)
