from tkinter import *
import module
import numpy as np
root=Tk()
root.geometry("200x100")
village = "Kanmandale"
surveyNo = ""

def retrieve_input():
    surveyNo = textBox.get("1.0","end-1c")
    print("Input: ", surveyNo)
    surveyNo = surveyNo.replace(" ", "")
    surveyNo = surveyNo.split(",")
    print("Output: ", surveyNo)
    print("Village selected: ", village)
    print("XPATH: ",selectedVil[village])
    print("Entered survey number: ", surveyNo)
    surveyNo = np.array(surveyNo, dtype=int)
    Call = module.UtaraOpen(selectedVilXpath = selectedVil[village] , selectedSurveyNo = surveyNo )  #Enter selectedSurveyNo[n]
    

def dropvalue(value):
    global village
    village = value
    #print(value)

var = StringVar(root)
var.set("Kanmandale")
selectedVil = {
    'Kanmandale': "//*[@id='vilSelect']/option[14]",
    'Sherisalayban': "//*[@id='vilSelect']/option[103]",
    'Kundane': "//*[@id='vilSelect']/option[16]",
    'Puri': "//*[@id='vilSelect']/option[66]"
					}
option = OptionMenu(root, var, *selectedVil, command=dropvalue)
option.pack()

#Text box for enter 7/12 No.
textBox=Text(root, height=2, width=10)
textBox.pack()
buttonRun=Button(root, height=1, width=10, text="7/12 Open", 
                    command=lambda: retrieve_input())
#command=lambda: retrieve_input() >>> just means do this when i press the button
buttonRun.pack()

mainloop()
