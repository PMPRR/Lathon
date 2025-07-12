from lathon import Tabular

tab = Tabular("c|l|   c")
tab.addRow((1, 2, 3))
tab.addRow(["a", "b", "c"])
print(tab)
