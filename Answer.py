
'''
1. Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number 
and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.
'''
ans = []
for num in range(1,100+1):
    if (num % 3 == 0 and num % 5 == 0):
        ans.append("FizzBuzz")
    elif num % 3 == 0:
        ans.append("Fizz")
    elif num % 5 == 0:
        ans.append("Buzz")
    else:
        ans.append(str(num))
print(ans)





'''
2. Write a program that determine whether or not an integer input is a leap year.
'''
n = int(input("Please Enter the Year : "))
if (n%400 == 0):
    print(n,"-> true")
elif (n%100 == 0):
    print(n,"-> false")
elif (n%4 == 0):
    print(n,"-> true")
else:
    print(n,"-> false")
    
    
    
'''
3. Write a program that produce the following output giving an integer input n.

'''
# 3.1
n = int(input("Please Enter the number : "))
for i in range(0, n):
    for j in range(0, i+1):
        print("*",end="")
    print()
    

    
    
    
#3.2
n = int(input("Please Enter the number :"))
for i in range(0,n):
    for j in range(n - i):
        print (" ",end="")
    for j in range(0,i + 1):
        print("*",end="")
    print()

    
    
    
    
#3.3
n = int(input("Please Enter the number :"))
for i in range(n):
    print(" "*(n-i-1)+"* ",end="")
    if i>=1:
        print(" "*(2*i-1)+"* ",end="")
    print()

    
    
    
#3.4
n = int(input("Please Enter the number :"))       
for i in range(0,n):                       
    for j in range(0,n):
        if(i==j or j==n-1-i):
            print("*",end=" ")             
        else:
            print(" ",end=" ")             
    print()                                

    
    
    
    
#3.5 problem for even numbers.
n = int(input("Please Enter the number :"))     
for i in range(1, n+1):
    i = i - (n//2 +1)
    if i < 0:
        i = -i
    print(" " * i + "*" * (n - i*2) + " "*i)
  

'''
else
หลังจากที่เรากำหนดการทำงาน Exception Errors แล้ว หากเรารันโปรแกรมแล้วไม่พบข้อผิดพลาดที่เราได้กำหนดไว้ 
เราสามารถใช้บล็อก else ทำงานตามเงื่อนไขที่กำหนดไว้ได้
finally
เป็นการกำหนดคำสั่งเมื่อสิ้นสุดการทำงานบล็อก try except โดยบล็อก finally จะทำงานไม่ว่าจะมีข้อผิดพลาดเกิดขึ้นหรือไม่ก็ตาม

'''

#1.Write a program that finds all prime numbers up to n for input n 
n = int(input("Please Enter the number :")) 

for num in range(1, n + 1):  
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
 
