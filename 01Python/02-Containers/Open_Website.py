#!/bin/python

import webbrowser

websites = {
    'facebook'  : '"https://www.facebook.com/"',
    'instagram' : '"https://www.instagram.com/"'
}

def openWebsite():
    websiteName = input(f"Enter the desired website from {websites.keys()} \nAnswer: ")
    Value=websites.get(websiteName.lower())
    if Value !=None:
        print (Value) #checking the Value associated to the input key
        webbrowser.open(Value,new=2)
    else:
        print("Unrecognized Input")
        return 1 #run back to the main Fn