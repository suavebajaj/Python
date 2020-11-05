import pyautogui, time #Import Pyautogui (Control the mouse and keyboard to automate interactions)and Time (for sleep fucntion)
time.sleep(5) #Delay Timer
f = open("HelloScript.txt",'r') #Read the Script file/text 
for word in f: #For reading each word in file 
    pyautogui.typewrite(word) #This function will type the characters in the string that is passed
    pyautogui.press("enter") #To press the desired key
pyautogui.alert(text='Done', title='Sent 100 Hello\'s', button='OK!') #Displays a Alert box when the for loop is closed