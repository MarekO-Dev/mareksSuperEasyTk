import sys 
sys.dont_write_bytecode = True

import pytest
import supereasyTk.feature1 as feature1


@pytest.fixture
def instance():
    return feature1.Application()

@pytest.fixture
def instance_arg_window_size_not_tuple():
    return feature1.Application([900, 300])

def test_caninstatiate(instance):
    assert isinstance(instance, feature1.Application)

def test_window_size_argument(instance_arg_window_size_not_tuple):
    pass #assert instance_arg_window_size_not_tuple

class TestValid:
    def test_window_size_is_str(cls, instance):
        assert type(instance.size) == str
    def test_sup2(cls):
        assert 1 == 1   