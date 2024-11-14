import pytest
from src.supereasyTk import newTk

@pytest.fixture
def appInstance():
    return newTk.Application()

class TestAppInstance:

    def test_can_instantiate(cls, appInstance: newTk.Application):
        assert isinstance(appInstance, newTk.Application)

class TestAppVariables:

    def test_variable_window_size(cls, appInstance):
        assert type(appInstance.size) == str

class TestAppFeatures:

    def test_button_addition(appInstance):
        pass