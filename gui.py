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


# import appJar
# from  appJar import gui
# app = gui()
# web_url = 0
# twi= 0
# variables = ["web_url", "twi"]
# # add & configure widgets - widgets get a name, to help referencing them later
# allentries = ["ent1", "ent2"]
# app.addLabel("title", "Welcome to appJar")
# app.setLabelBg("title", "red")
# app.addLabel("url", "Website URL: ", 0, 0)
# app.addEntry("weburl", 0, 1)
# app.addLabel("twi", "Twilio:  ", 1, 0)
# app.addEntry("2", 1, 1)


# def save() :
#     e = app.getAllEntries()
#     def death():
#         for i in e:
#             a = e[i]
#             print(i)

#     # e.keys = e.values
#     print(e)
#     # for i in range(len(e)):
        
  
       
        

        


   

# app.addButton("Submit", save)
# app.go()
