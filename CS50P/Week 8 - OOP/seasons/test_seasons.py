# Problem set: https://cs50.harvard.edu/python/psets/8/seasons/

import pytest
from seasons import valid_date

def test_valid_date():
    with pytest.raises(SystemExit):
        valid_date("January 1, 1999")
    valid_date("1999-01-01")
