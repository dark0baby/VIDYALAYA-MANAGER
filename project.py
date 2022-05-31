#***************KENDRIYA VIDYALAYA SEC-2 R.K PURAM ***************" 
#******************VIDYALAYA MANAGER *****************************" 
#***************Designed and Maintained By:***********************"
#***************KESHAV KUMAR   *************"       
 

import mysql.connector

# GLOBAL VARIABLES DECLARATION

myConnnection ="" 
cursor=""
userName="" 
password =""

#MODULE TO CHECK MYSQL CONNECTIVITY
def MYSQLconnectionCheck ():

    global myConnection 
    global userName 
    global password

    userName = input("\n ENTER MYSQL SERVER'S USERNAME : ")
    password = input("\n ENTER MYSQL SERVER'S PASSWORD : ")

    myConnection=mysql.connector.connect(host="localhost",user=userName,passwd=password , auth_plugin='mysql_native_password' ) 
    if myConnection:
        print("\n CONGRATULATIONS ! YOUR MYSQL CONNECTION HAS BEEN ESTABLISHED !")
        cursor=myConnection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS SMS")
        cursor.execute("COMMIT") 
        cursor.close()
        return myConnection 
    else:
        print("\nERROR	ESTABLISHING	MYSQL	CONNECTION	CHECK USERNAME AND PASSWORD !")

#MODULE TO ESTABLISHED MYSQL CONNECTION
def MYSQLconnection ():
 
    global userName 
    global password 
    global myConnection

    myConnection=mysql.connector.connect(host="localhost",user=userName,passwd=password , database="SMS" , auth_plugin='mysql_native_password' ) 
    if myConnection:
        return myConnection
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION !")
    myConnection.close()

#MODULE FOR NEW ADMISSION
def newStudent():
    if myConnection: 
        cursor=myConnection.cursor()
        createTable	="""CREATE	TABLE	IF	NOT	EXISTS	STUDENT(SNAME VARCHAR(30),FNAME VARCHAR(30),MNAME VARCHAR(30),PHONE	VARCHAR(12),ADDRESS	VARCHAR(100),SCLASS VARCHAR(5),SSECTION VARCHAR(5),SROLL_NO	VARCHAR(5),SADMISSION_NO VARCHAR(10) PRIMARY KEY)"""
        cursor.execute(createTable)

        sname=input("\n ENTER STUDENT'S NAME : ") 
        fname=input(" ENTER FATHER'S NAME : ") 
        mname=input(" ENTER MOTHER'S NAME : ") 
        phone=input(" ENTER CONTACT NO. : ") 
        address=input(" ENTER ADDRESS : ")
        sclass =input(" ENTER CLASS : ") 
        ssection=input(" ENTER SECTION : ") 
        sroll_no=input(" ENTER ROLL_NO : ")
        sadmission_no =input(" ENTER ADMISSION_NO : ")

        sql="INSERT INTO student(SNAME,FNAME,MNAME,PHONE,ADDRESS,SCLASS,SSECTION,SROLL_NO,SADMISSION_NO) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values=(sname,fname,mname,phone,address,sclass,ssection,sroll_no,sadmission_no) 
        cursor.execute(sql,values) 
        cursor.execute("COMMIT") 
        cursor.close()
        print("\nNew Student Enrolled Successfully !")
 
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION !")

#MODULE TO DISPLAY STUDENT'S DATA
def displayStudent(): 
    cursor=myConnection.cursor() 
    if myConnection:
        cursor.execute("SELECT * FROM STUDENT")
        data=cursor.fetchall()
        print(data) 
        cursor.close()
    else:
        print("\nSomthing Went Wrong ,Please Try Again !")

#MODULE TO UPDATE STUDENT'S RECORD
def updateStudent(): 
    cursor=myConnection.cursor() 
    if myConnection:
        admission_no=input("ENTER ADMISSION NO")
        sql="SELECT * FROM STUDENT WHERE SADMISSION_NO= %s"
        cursor.execute(sql,(admission_no,)) 
        data=cursor.fetchall()
    if data:
        print("PRESS 1 FOR NAME") 
        print("PRESS 2 FOR CLASS") 
        print("PRESS 3 FOR ROLL NO")
        print("PRESS 4 FOR SECTION")
        print("PRESS 5 FOR FATHER'S NAME")
        print("PRESS 6 FOR MOTHER'S NAME")
        print("PRESS 7 FOR CONTACT NO")
        print("PRESS 8 FOR ADDRESS")
        print("PRESS 9 FOR ADMISSION NUMBER")
        choice=int(input("Enter Your Choice")) 
        if choice==1:
            name=input("ENTER NAME OF THE STUDENT :")
            sql="UPDATE STUDENT SET SNAME= %s WHERE SADMISSION_NO =%s"
            cursor.execute(sql,(name,admission_no)) 
            cursor.execute("COMMIT")
            print("NAME UPDATED")

        elif choice == 2:
            std=input("ENTER CLASS OF THE STUDENT :")
            sql="UPDATE STUDENT SET SCLASS= %s WHERE SADMISSION_NO=%s"
            cursor.execute(sql,(std,admission_no)) 
            cursor.execute("COMMIT") 
            print("CLASS UPDATED")

        elif choice==3:
            roll_no=int(input("ENTER ROLL NO OF THE STUDENT :"))
            sql="UPDATE	STUDENT	SET	SROLL_NO=	%s	WHERE SADMISSION_NO = %s"
            cursor.execute(sql,(roll_no,admission_no)) 
            cursor.execute("COMMIT")
            print("ROLL NO UPDATED")
        
        elif choice == 4:
            sec=input("ENTER SECTION OF THE STUDENT :")
            sql="UPDATE STUDENT SET ssection= %s WHERE SADMISSION_NO=%s"
            cursor.execute(sql,(sec,admission_no)) 
            cursor.execute("COMMIT") 
            print("SECTION UPDATED")
            
        elif choice == 5:
            FATHER_NAME=input("ENTER FATHER'S NAME OF THE STUDENT :")
            sql="UPDATE STUDENT SET fname= %s WHERE SADMISSION_NO=%s"
            cursor.execute(sql,(FATHER_NAME,admission_no)) 
            cursor.execute("COMMIT") 
            print("FATHER_NAME UPDATED")
            
        elif choice == 6:
            MOTHER_NAME=input("ENTER MOTHER_NAME OF THE STUDENT :")
            sql="UPDATE STUDENT SET mname= %s WHERE SADMISSION_NO=%s"
            cursor.execute(sql,(MOTHER_NAME,admission_no)) 
            cursor.execute("COMMIT") 
            print("MOTHER_NAME UPDATED")
            
        elif choice == 7:
            CONTACT_NO=input("ENTER CONTACT_NO OF THE STUDENT :")
            sql="UPDATE STUDENT SET phone = %s WHERE SADMISSION_NO=%s"
            cursor.execute(sql,(CONTACT_NO,admission_no)) 
            cursor.execute("COMMIT") 
            print("CONTACT_NO UPDATED")
            
        elif choice == 8:
            ADD=input("ENTER ADDRESS OF THE STUDENT :")
            sql="UPDATE STUDENT SET address= %s WHERE SADMISSION_NO=%s"
            cursor.execute(sql,(ADD,admission_no)) 
            cursor.execute("COMMIT") 
            print("ADDRESS UPDATED")
            
        elif choice == 9:
            Add_no=input("ENTER Addmission numbber OF THE STUDENT :")
            sql="UPDATE STUDENT SET sadmission_no= %s WHERE SADMISSION_NO=%s"
            cursor.execute(sql,(Add_no,admission_no)) 
            cursor.execute("COMMIT") 
            print("Addmission numbber UPDATED")
        

        else:
            print("Record Not Found Try Again !")
        cursor.close()
    else:
        print("\nSomthing Went Wrong ,Please Try Again !")


#MODULE TO ISSUE TRANSFER CERTIFICATE
def transferStudent(): 
    cursor=myConnection.cursor()
    if myConnection:
        admission_no=input("ENTER ADMISSION NO OF THE STUDENT :") 
        cursor=myConnection.cursor()
        sql="SELECT * FROM STUDENT WHERE SADMISSION_NO= %s"
        cursor.execute(sql,(admission_no,)) 
        data=cursor.fetchall()
        if data:
            sql=("DELETE FROM STUDENT WHERE SADMISSION_NO=%s")
            cursor.execute(sql,(admission_no,)) 
            cursor.execute("COMMIT")
            print("Student's Transfer Certificate Generated !!!") 
        else:
            print("Record Not Found , Please Try Again !") 
            cursor.close()

    else:
        print("\nSomthing Went Wrong ,Please Try Again !")

#MODULE TO PROVIDE HELP FOR USER
def helpMe():
    print("Please, Visit The Offcial Website Of Vidyalaya To Download The Mannual!!!")


# MAIN SCREEN OF THE SYSTEM print("#################")

print("\n| 	                 SESSION 2020 - 2021 		           |") 
print("\n|		                   WELCOME	                       |")
print("\n|	           KENDRIYA VIDYALAYA SEC-2 R.K PURAM          |")
print("\n|********************VIDYALAYA MANAGER********************|")
print("\n|*****************DESIGNED AND MAINTAINED BY:*************|") 
print("\n|****************    KESHAV KUMAR   *************|")  
print("\n|                                              	       |")
print("\n|                 	VIDYALAYA MANAGER		               |") 
print("\n| 	                                               	       |")
print("#############################################################")


#STARTING POINT OF THE SYSTEM
 
myConnection = MYSQLconnectionCheck () 
if myConnection:
    MYSQLconnection () 
    while(1):
        print("|	Enter 1 - New Admission.		       |") 
        print("|	Enter 2 -  Display Student's Data.	   |") 
        print("|	Enter 3 -  Update Students's Data .	   |") 
        print("|	Enter 4 -  Issue Transfer Certififcate.|") 
        print("|	Enter 5- Exit.	                       |")
        print("|	Enter 0 - Help.	                       |") 
        

        choice=int(input("PLEASE ENTER YOUR CHOICE :	")) 
        if choice==1:
            newStudent() 
        elif choice==2:
            displayStudent() 
        elif choice==3:
            updateStudent() 
        elif choice==4:
            transferStudent()
        elif choice==5:
            break  
        elif choice==0:
 
            helpMe() 
    else:
        print("Sorry ,May Be You Are Giving Me Wrong Input, Please Try Again !!! ")
else:
    print("Check Your MYSQL Connection First !!! ") 
    
# END OF THE PROJECT
