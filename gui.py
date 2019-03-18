import appJar
from  appJar import gui
app = gui()

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Welcome to appJar")
app.setLabelBg("title", "red")
app.addLabel("url", "Website URL: ", 0, 0)
app.addEntry("ent1", 0, 1)
app.addLabel("twi", "Twilio:  ", 1, 0)
app.addEntry("ent2", 1, 1)
x = 2
def save() :
    for i in x:
        e = app.getEntry("ent"+ str(i))
        print(e)
   

app.addButton("Submit", save)
app.go()


