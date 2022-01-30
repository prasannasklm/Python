# read the marks of the strudent in the range 0.0 to 1.0 and print the score according to the points >=0.9 A, >=0.8 B, >-0.7 C, >= 0.6 D, <=0.6 fail
# if the score is out of range print the error message
score=float(input("enter the score between 0.0 to 1.0 :"))
if(score>=1.0 or score<=0.0):
    print("enter the score in the given ragne!!!")
    quit()
else:
    if(score>=0.9):
        print("A")
    elif(score>=0.8):
        print("B")
    elif(score>=0.7):
        print("C")
    elif(score>=0.6):
        print("D")
    elif(score<0.6):
        print("FAIL!!!")
print("end of the program!!!")
