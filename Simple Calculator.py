num1=int(input('Enter 1st no. :'))
num2=int(input('Enter 2nd no. :'))
print('Choose the operation to be followed')
print("1=Addition,2=sub,3=mul,4=div,5=div[display on remainder],6=div[only qoutient],7=fac,8=exponent,9=mul table")
x=int(input('choosen operation number:'))
if x==1:
   add=num1+num2
   print('ADD IS-',add)
elif x==2:
         sub=num1-num2
         print('SUB IS-',sub)
elif x==3:
         mul=num1*num2
         print('MUL IS-',mul)
elif x==4:
         if num2==0:
           print('INVALID NO.')
         else:
           div=num1//num2
           print('DIV IS-',div)
elif x==5:
    if num2==0:
       print('INVALID NO.')
    else:
           mod=num1//num2
           print('MODULUD IS-',mod)
elif x==6:
        qou=num1/num2
        print('QOUTIENT IS-',qou)
elif x==7:
        num =int(input('Enter the number'))
        fac=1
        while i<=num:
             fac=i*1
             i=i+1
             print('fac of',num,"is",fac)
elif x==8:
         exp=num1**num2
         print('EXPONENT value for',num1,'^',num2,'is-',exp)
elif x==9:
         tab=int(input('enter the no. of which you want table'))
         last=int(input("Enter till which no you want mul"))
         a=tab
         y=last
         for tab in range(a,a*y,a+a):
          print(a, end="")
else:
    print('no valid input')
         
    
