import sys
sys.dont_write_bytecode = True
####################################################
import supereasyTk.feature1 as feature

app = feature.Application()
print(app.size)

app.mainloop()