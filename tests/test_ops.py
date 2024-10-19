from python_starter.ops import add, multiply

import pytest

# uncomment if needed
#from unittest import TestCase



class TestAdd:
    # you can use the parametrize fixture for concise looping like so
    @pytest.mark.parametrize("a,b,expected", [(3,5,8), (2,4,6)])
    def test_add(self, a, b, expected):
        assert add(a, b) == expected


class TestMultiply:
    # you can use the parametrize fixture for concise looping like so
    @pytest.mark.parametrize("a,b,expected", [(3,5,15), (2,4,8)])
    def test_multiply(self, a, b, expected):
        assert multiply(a, b) == expected
