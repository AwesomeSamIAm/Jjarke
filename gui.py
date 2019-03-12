import appJar
from  appJar import gui
app = gui()
# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Welcome to appJar")
app.setLabelBg("title", "red")
app.go()
