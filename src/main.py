import sys
sys.dont_write_bytecode = True
####################################################
import supereasyTk.newTk as newTk

app = newTk.Application()
app.add_element(newTk.Button, {
    "text": "ButtonName"
}, element_window_manager_options = {
    "row": 0,
    "column": 0
})
app()