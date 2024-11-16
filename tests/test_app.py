import pytest
from src.supereasyTk import newTk

@pytest.fixture
def appInstance():
    return newTk.Application()

class TestAppInstance:

    def test_can_instantiate(cls, appInstance: newTk.Application):
        assert isinstance(appInstance, newTk.Application)

class TestAppVariables:

    def test_variable_window_size(cls, appInstance: newTk.Application):
        assert type(appInstance.size) == str

class TestAppFeatures:

    def test_button_addition(cls, appInstance: newTk.Application):
        """
            Tests if adding a button works
        """
        appInstance.add_element(
                    newTk.Button, {
                "text": "TestButton"
            }, 
                    element_window_manager_options = {
                "row": 0,
                "column": 0
            })
        
        assert len(appInstance._all_elements) > 0

    def test_button_addition_chaining(cls, appInstance: newTk.Application):

        appInstance\
            .add_element(
                    newTk.Button, {
                "text": "TestButton"
            }, 
                    element_window_manager_options = {
                "row": 0,
                "column": 0
            })\
            .add_element(
                    newTk.Button, {
                "text": "TestButton2"
            }, 
                    element_window_manager_options = {
                "row": 0,
                "column": 1
            })
        
        assert len(appInstance._all_elements) > 1


    def test_label_addition(cls, appInstance: newTk.Application):

        appInstance\
            .add_element(
                    newTk.Label, {
                "text": "TestLabel"
            }, 
                    element_window_manager_options = {
                "row": 1,
                "column": 1
            })
        
        assert len(appInstance._all_elements) > 0