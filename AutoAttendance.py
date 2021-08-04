import cv2
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
import os
from openpyxl import load_workbook, Workbook
import openpyxl
import os
import time

# Capitlizing all names
def lower(studentlist):
    for name in studentlist:
        studentlist[studentlist.index(name)] = name.lower()


#Finding img files and appending it into a list
def loopFiles():
    filelist = os.listdir(os.getcwd())
    imglist = []
    for i in filelist:
        if i.lower().endswith(('.png','.jpg','jpeg')):
                 imglist.append(i)
    return imglist

def cleanstring(namelist):
    formatlist = []
    for i in namelist:
        namestring = i.split("‘")
        namestring = "".join(namestring)
        formatlist.append(namestring)
    return formatlist

def checkpresent(studentlist):
    list1 = []
    present = []
    imglist = loopFiles()
    for image in imglist: 
        #reading names from image
        img = cv2.imread(image)
        text = pytesseract.image_to_string(img)
        for i in text.splitlines(): #READING THE IMAGE AND TURNING IT INTO A ROUGH LIST STRING 
            list1.append(i.lower())
    
    list1 = cleanstring(list1)

    #Checking names from student list and appending it into present list
    for studname in studentlist:
        for i in list1:
            seperatlist = i.split()
            if studname in seperatlist:               
                present.append(studname.capitalize())
                break   
    return present 
    print(len(present))          


if __name__ == "__main__":

    #List of all students in the class
    studentlist = ["Gautham","Shreeju","Akshay","Anusaranya","Chandrasai",
                    "Aromal","Mihir","dona","Animesh","Ashwin","rahul",
                    "gayatri","shivam","gladys","eashwar","mahesh","Dineshkumar","Raj",
                    "Yash","Chandrakala","Ramyata","Harish","Soham","Abrial","Jivamani","Sayali","Tejas",
                    "Bhavana","Bhushan","Arun","Kartik","Pranesh","Ashreen","Raina","Mitesh","Shubhada","Ishita",
                    "Siddhesh","Nitin","Akash","Sen","Akshara","Pranit","Kevin","Adil","Anees","Devendra","Shoaib",
                    "Muthumari","Ajith","Santhni","Santhni","Harsh","Devika","Rishikesh","Rohit","Somdatt",
                    "Gauri","Brinda","Harikrishnan","Mahi","Shailesh","Vishnu","Darshan","Amey","Tejal","Ankush","Roshani",
                    "Meenakshi","Sadiya","Aanam","Arman","Shalu","Divyesh","Shrinidhi","Varun","Huda","Vimal","Gautam",
                    "Harshit","Sneha","Shivani","Tejaswin","Sanjana","Sivakumar","Vamshi","Pratik","Mrunali","Rohit",
                    "Imran","Saikrishna","Hasnain","Kasim","Aftab","Aditya","Amirthavarshini","Hrithik","EASHWER"]

    

    #List of students with the same name
    doublenamelist = ["Rutuja Ravindra","Rutuja Rane", "Rutuja Santosh","Shubham Vinod","Shubham Bhalerao",
                    "Nikhil Gurrapu","Nikhil Jindam","Pranav Salunke","Pranav Bindu"]

    ##Turning all text to upper case as all elements in the recognised text will be upper
    lower(doublenamelist)
    lower(studentlist)

    present = checkpresent(studentlist)
    print(present)
    print(len(present))
    
    wb = load_workbook("Attendance.xlsx")

    #WORKSHEETS
    # ws = wb["INS"]
    # ws = wb["STQA"]
    # ws = wb["WS"]
    # ws = wb["GP"]
    # ws = wb["AI"]
    # ws = wb["GP pracs"]
    # ws = wb["STQA pracs"]
    # ws = wb["INS pracs"]
    # ws = wb["WS pracs"]
    # ws = wb["AI pracs"]
    ws = wb["PD pracs"]

    now = time.strftime("%x") #date
    ws["B2"].value = now



    #THIS PART MARKS THE STUDENT PRESENT
    # for i in range(2,111):
    #     for j in Present:
    #         if ws[f"A{i}"].value == j:
    #             ws[f"B{i}"].value = "P"


    wb.save("Attendance.xlsx")




    
    #Incase ub need to add students in a new worksheet

    # rows = 2
    # for i in studentlist:
    #     ws[f"A{rows}"].value = i.capitalize()
    #     rows = rows+1