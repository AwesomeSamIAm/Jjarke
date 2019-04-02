## working(if hard-coded) interface
import appJar
from  appJar import gui
app = gui()

# window declarations
allentries = ["ent1", "ent2"]
app.addLabel("title", "Welcome to appJar")
app.setLabelBg("title", "red")

#label and entry declarations
app.addLabel("url", "Website URL: ", 0, 0)
app.addEntry("weburl", 0, 1)
app.addLabel("int", "Time Interval:  ", 1, 0)
app.addEntry("interv", 1, 1)
app.addLabel("asid", "Account sid: ", 2, 0 )
app.addEntry("sid",2,1 )
app.addLabel("auth", "Authorization Token: ", 3, 0)
app.addEntry("authtok", 3,1)
app.addLabel("twi", "Twilio Number: ", 4,0)
app.addEntry("twinum", 4,1)
app.addLabel("dest", "Destination Number: ", 5,0)
app.addEntry("destnum", 5,1)
#button function- saves entries to respective variable names
def save() :
   weburl = app.getEntry("weburl")
   interv = app.getEntry("interv")
   sid = app.getEntry("sid")
   authtok = app.getEntry("authtok")
   twinum = app.getEntry("twinum")
   destnum = app.getEntry("destnum")

   #printed variable names to check
   print(weburl)
   print(interv)
   print(sid)
   print(authtok)
   print(twinum)
   print(destnum)

#button declaration and window initialization
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
