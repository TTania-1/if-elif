#print("Hello World")

#import hello

x = 10
if x > 100:
  print("Over 100")
elif x > 50:
  print ("Over 50")
elif x > 30:
  print( "Over 30")
else:
  print("under 30")


# <> >= <= != ==
  # and or not

print ("Python is cool")
a=1
while a <=100:
 print("Python is cool")
#a= a+1
 a += 1

for i in range (1, 2):
 print(i)

#zero based indexing language

 a += 1
 num = int (input("Enter a number:"))
#for i in range (1, num+1):
 #print(i)
 while a <= num:
  print("a")
#a= a+1
  a += 1


#Nested if statement

person = "Student"
university = "Oxford"

if person == "Student":
 if university == "Solent":
   print ("You are a Solent University student")
 else:
   print ("You are student but not a Solent University student")
else: 
  print("You are not a student")