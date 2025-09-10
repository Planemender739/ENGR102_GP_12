
#--------------THESE ARE PRACTICE FROM THE VIDEO, SEE MY NEXT HEADER AND THAT IS WHERE THE WORK BEGINS-----------------------------

from math import *

# 9x12 sheet of paper with 1 inch sides, making it 7*10*1


#print("A flap 1 inch square produces a volume of",7*10*1,"cubic inches.")  #This would be for the paper with 1 inch sides
#print("A flap 0.5 inches square produces a volume of",8*11*.5,"cubic inches.") #This would be for .5 inch sides

#x=3.1415926 #Defining that x=pi

#print("A flap",x,"inches square produces a volume of",(9-2*x) * (12-2*x)*x,"cubic inches.")  #part c


#import SymPy as sp  #Bringing in all commands from SymPy library
#x=sp.symbols('x')   #Setting X as a variable we can solve for
#volume=(9-2*x)*(12-2*x)*x    #L*H*W for volume
#print(volume)



#Now, we substitute using the volume.subs() command to find 
#print("A flap 1 inch square produces a volume of",volume.subs(x,1),"cubic inches.")  #This would be for the paper with 1 inch sides
#print("A flap 0.5 inches square produces a volume of",volume.subs(x,0.5),"cubic inches.") #This would be for .5 inch sides
#c=3.1415926 #Defining x=pi
#print("A flap",c,"inches square produces a volume of",volume.subs(x,c),"cubic inches.")  #part c

#xvals=[1,0.5,3.1415926]
#volumes=[volume.subs(x,i) for i in xvals] #Go thru each list and substitute those values for x.
#print("Squares with side lengths",xvals,"produce volumes of",volumes)


#-----------------------------------------------------ANSWERS BEGIN HERE --------------------------------------------------------------------

#1a math 151 python lab 1
#Print stated equation in 1(a)

x=(((e**2.0)+log(19.0))**2.0)/(2025.0+8.0**3.0)
x=(((e**2)+log(19))**2)/(2025+8**3)
print(x)

#1b
#calculate 12natural log of 49 plus tangent of 2pi/3
y=12*log(49)+tan(2*pi/3)
print(y)

#---------------------------------------------

#2 a,b Lets calculate the interest on a loan with a given term and principle
r=.071 #7.1% interest rate
P=30000 #Principle of $30,000
t=9 #Time in months
m=12 #number of compoundings per year, meaning m=12 would be monthly.

#R9 is the monthly payment with a term of 9 months
R9=P*((r/m)*(1+(r/m))**(m*t))/((1+(r/m))**(m*t)-1)
print(R9)

t=7 
#R7 is the monthly payment with a term of 7 months
R7=P*((r/m)*(1+(r/m))**(m*t))/((1+(r/m))**(m*t)-1)
print(R7)

#2c #Now we will calculate the total amount paid over the course of the term of the loan.

print("On the 9 year term, you will pay a total of:",R9*108,"dollars")
print("On the 7 year term, you will pay a total of:",R7*84,"dollars")

#------------------------------------------------------------

#3 #an object moves in a straight line from (14,3) to (30,12)
#F=ai+bj 
x1=14
x2=30
y1=3
y2=12

#3a   Displacement vector

from math import *
DV=((x2-x1),(y2-y1))
print("The displacement vector is",DV)

#3b Magnitude of the displacement vector

magnitude_DV=(sqrt((16**2+9**2)))
print("The length, or magnitude of the displacement vector is",magnitude_DV)


#3c 
#work=force*displacement*cos(theta)
Force_mag=sqrt((9)**2 + (2)**2)
print("The magnitude of the force vector is",Force_mag)
theta_rad=((16.82*pi)/180)
Work=Force_mag*magnitude_DV*cos(theta_rad)
print("The amount of work done on the object was",Work,"units")


#3d
#the angle between the vectors of force and displacement on the object was 16.82*
#Using the dot product
#Lets define the x1,x2,y1,y2 again so that we dont have to run everywhere to read them!

x1=16
x2=9
y1=9
y2=2
adotb=((x2*x1)+(y2*y1))  #This is the dot product simplified to one object

magnitude_DV=sqrt((x1**2+x2**2)) #DV being displacement vector
magnitude_FV=sqrt((y1**2)+y2**2)  #FV being force vector


theta=acos((adotb)/(magnitude_DV*magnitude_FV))  #Using ArcCos, we can solve for theta, the angle between the two vectors
print("The angle between the displacement vector and the force vector is",theta,"radians or",theta*180/pi,'degrees.')


