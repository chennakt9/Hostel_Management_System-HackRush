#!C:/Users/CHENNA/AppData/Local/Programs/Python/Python36/python
print("Content-Type: text/html")
print()


print("<h1>Welcome Python is powerful</h1>")

a='12-01-1700'





import mysql.connector
import cgi

data=cgi.FieldStorage()

id=data.getvalue("id")

print("<h1> Your Id is "+id+"</h1>")




mydb=mysql.connector.connect(user='root',password='',host='localhost',database='hostel1')

mycursor=mydb.cursor()

mycursor.execute("SELECT * FROM users")

myresult = mycursor.fetchall()

l=[]
for x in myresult:
  # print(x)
  l.append(x)


# print(l)





#This is for getting rooms of capacity 2
mycursor1 = mydb.cursor()

sql1 = "SELECT * FROM boys WHERE capacity ='2'"

mycursor1.execute(sql1)

myresult1 = mycursor1.fetchall()

k=[]
for x in myresult1:
  # print(x)
  k.append(x[1])

# print(k)




#This is for getting rooms of capacity 3
mycursor2 = mydb.cursor()

sql2 = "SELECT * FROM boys WHERE capacity ='3'"

mycursor2.execute(sql2)

myresult2 = mycursor2.fetchall()

g=[]
for x in myresult2:
  g.append(x[1])

# print(g)


#This is for getting outdates of capacity 3


mycursor3 = mydb.cursor()

sql3 = "SELECT * FROM boys WHERE capacity ='3'"

mycursor3.execute(sql3)

myresult3 = mycursor3.fetchall()

p=[]
for x in myresult3:
  p.append(x[4])

# print(p)


#This is for getting outdates of capacity 2


mycursor4 = mydb.cursor()

sql4 = "SELECT * FROM boys WHERE capacity ='3'"

mycursor4.execute(sql4)

myresult4 = mycursor4.fetchall()

h=[]
for x in myresult4:
  h.append(x[4])

# print(h)


# This is for getting of no. of males from usres with id=something




mycursor5 = mydb.cursor()

sql5 = "SELECT * FROM users WHERE id ="+id

mycursor5.execute(sql5)

myresult5 = mycursor5.fetchone()

# print(myresult5[1])
print("<br>")
print("<br>")

# print(myresult5[7])

print('''
	<html>
    <head>
        <link href = "../css/style2.css" rel = "stylesheet" type = "text/css"> 
    </head>
    <body>
        <h2>Details of the candidate</h2>
        <div class = "stud matter">
            <p>Name of the candidate: '''+myresult5[8]+'''</p>
            <p>Number of males: '''+str(myresult5[1])+'''</p>
            <p>Number of females: '''+str(myresult5[2])+'''</p>
            <p>Purpose of visit: '''+str(myresult5[3])+'''</p>
            <p>Date of arrival: '''+str(myresult5[5])+'''</p>
            <p>Date of departure: '''+str(myresult5[6])+'''</p>
            <p>Mess facility: '''+str(myresult5[4])+'''</p>
            <p>Reffered by: '''+str(myresult5[7])+'''</p>
            <p>Email Address: '''+str(myresult5[10])+'''</p>
            <p>Contact number: '''+str(myresult5[9])+'''</p>
        </div>
        
    </body>
</html>


	''')





print("<h2>Allocated rooms :</h2>")
#Avinash code
from datetime import datetime 
t3=[]
l3=g
l2=k
d3=p
d2=h
n=myresult5[1]
if n%3==1 and n!=1:
	n1=(n//3)-1
	n2=2
else:
  n1=n//3
  n2=((n%3)+1)//2
Id=str(myresult5[5][8:10]+myresult5[5][4:8]+myresult5[5][0:4])
od=str(myresult5[6][8:10]+myresult5[6][4:8]+myresult5[6][0:4])
k=0
for U in range(n1):
	# print(1)
	f=(sorted(d3, key=lambda x: datetime.strptime(x, "%d-%m-%Y").strftime("%Y-%m-%d")))[::-1]
	G=0
	# print(len(d3))
	for Z in range(len(d3)):
		S4=[f[Z],Id]
		qwsa=(sorted(S4, key=lambda x: datetime.strptime(x, "%d-%m-%Y").strftime("%Y-%m-%d")))
		# print(qwsa)
		if qwsa[1]==Id and qwsa[0]!=Id:
			# print(1)
			# print("<br>")
			print("<h3>tiplebed room "+str(l3[d3.index(f[Z])])+"</h3>")
			t3.append(l3[d3.index(f[Z])])
			d3[d3.index(f[Z])]=od
			G=1
			break
	if G==0:
		k+=3/2
for Q in range(n2+int(k+0.5)):
	f=(sorted(d2, key=lambda x: datetime.strptime(x, "%d-%m-%Y").strftime("%Y-%m-%d")))[::-1]
	K=0
	for q in range(len(d2)):
		ufds=(sorted([f[q],Id], key=lambda x: datetime.strptime(x, "%d-%m-%Y").strftime("%Y-%m-%d")))
		if ufds[1]==Id and ufds[0]!=Id:
			
			print("<h3>doublebed room "+str(l2[d2.index(f[q])])+"</h3>")
			t3.append(l2[d2.index(f[q])])
			d2[d2.index(f[q])]=od
			K=1
			break
	if K==0:
		# print("<br>")
		# print("<br>")
		print("<h3>all rooms are full</h3>")

		break
print("<br>")
#Avinash code block ended

print('''
	
	<h2>Your opinion:</p>
	<div class = "request">
	    <button class = "accept" onclick="location.href = 'echo_parse.php';">Accept</button>
	    <button class = "decline" onclick="location.href = 'echo_parse.php';">Decline</button>
	</div>


	''')

#<button onclick="location.href = 'www.yoursite.com';" id="myButton" class="float-left submit-button" >Home</button>

# print(t3)
# print(myresult5[6])
for j in t3:
	mycursor6 = mydb.cursor()



	sql6 = "UPDATE boys SET outdate = %s WHERE roomno = %s"
	val=(myresult5[6][8:10]+myresult5[6][4:8]+myresult5[6][0:4],j)

	mycursor6.execute(sql6,val)

	mydb.commit()

	print(mycursor6.rowcount, "record(s) affected")













