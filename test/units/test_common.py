import pytest

from chainloader.units import is_type


@pytest.mark.unittest
class TestUnitsCommon:
    def test_is_type(self):
        is_int = is_type(int)
        assert is_int(1) == 1
        assert is_int(2) == 2
        with pytest.raises(TypeError):
            _ = is_int(1.0)
        with pytest.raises(TypeError):
            _ = is_int('skldfjlsd')
