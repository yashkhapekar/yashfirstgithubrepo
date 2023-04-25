# escape sequence and string formatting


st="Hello Yash"
print(st)
st1="Hello \nYash"
print(st1)
st1="Hello \tYash"
print(st1)
st1="Hello \bYash"
print(st1)
st1="Hello \\New Yash"
print(st1)
st1="Hello \"New\"Yash"
print(st1)
st1="Hello \'New\'Yash"
print(st1)
st1='\\\\'
print(st1)
st1='/\/\/\/\/\/\/\/\\'
print(st1)
st1='\\"\\n\\t\\v\\'
print(st1)





# string formatting
st = "Hello Python How Are You ?"
print(st)
course="Yash"
st="Hello " +course+" How Are You ?"
print(st)
dt=67.69
st ="Hello {} How Are You {} ?".format(course,dt)
print(st)
st=f"Hello {course} How Are You  {dt}?"
print(st)
st=f"Hello %f How Are You ?"%(dt)
print(st)
st=f"Hello %s How Are You %f ? Your Marks %d"%(course,dt,100)
print(st)
course =" PYTHON "
st1="Hello "+course+" How Are You ?"
print(st1)
dt=69
st1=f"Hello {course} How Are You {dt}?"
print(st1)
st1=f"Hello %s How Are You  ?"%(dt)
print(st1)
st1=f"Hello %s How Are You %f ? Your Marks %d"%(course,dt,100)
print(st1)
course="JAVA"
st2="Hello "+course+" How Are YOU ?"
print(st2)
dt = 82
st2=f"Hello %s How Are You ?"%(dt)
print(st2)
st2=f"Hello %s How Are You %f ? Your Marks %d"%(course, dt,100)
print(st2)
course="Shrikant"
st3="Hello "+course+" How Are You ?"
print(st3)
dt=(89)
st3=f"Hello %s How Are You %f ? Your Marks %d"%(course,dt,88)
print(st3)
st3=f"Hello %s How Are You ?"%(dt)
print(st3)




# string concation
st=  "YASH\n"
st1= "PYTHON\n"
st2= "JAVA\n"
print(st+st1+st2)
print(st2,st2,st)
print(st+st+st)


#
st  = " Yash"
st1 = " Python "
st2 = " Java "
st3 = " Shrikant"
print ("Yash \n Java \t  Shrikant ")
print ("Shrikant \n Java\b Shrikant ")
print("\b java \t Yash \n Shrikant ")