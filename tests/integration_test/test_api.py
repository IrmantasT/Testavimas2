from calc.api_mok import get_only_numbers
from unittest.mock import patch, MagicMock


def test_api_read_only_numbers():
    test_data = ["1,3,4,5,32,ab,c21,v32","432,443,1443,adf4,435"]
    expected = "1|3|4|5|32|432|443|1443|435"

    fake_api = MagicMock()
    fake_api.get_data.return_value = test_data
    with patch('calc.api_mok.API', fake_api):
        result = get_only_numbers()
        assert result == expected
