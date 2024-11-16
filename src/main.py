import sys
sys.dont_write_bytecode = True
####################################################
import supereasyTk.newTk as newTk

app = newTk.Application(app_title = "Marek's TkInterWrapperTest")

app\
    .add_element(
        newTk.Button, {
    "text": "ButtonName"
}, 
        element_window_manager_options = {
    "row": 0,
    "column": 0,
    "padx": 50
})\
    .add_element(
        newTk.Button, {
    "text": "ButtonName2",
    "bg": "yellow",
    "relief": "groove"
}, 
        element_window_manager_options = {
    "row": 0,
    "column": 1,
    "padx": 50
})\
    .add_element(
        newTk.Label, {
    "text": "LabelText"
        }, element_window_manager_options = {
    "row": 1,
    "column": 1
})

app()