#!usr/bin/python
# Function to take input from Person
def input_name():
    """  ()->int
    Returns sum of all the alphabets of name
    """
    First_name= input("Enter the first Name")
    Middle_name= input("Enter the middle Name")
    Last_name= input("Enter the last Name")
    count1=count_string(First_name)
    count2=count_string(Middle_name)
    count3=count_string(Last_name)
    return count_num(str(count1+count2+count3))


# Function to take input from person
def input_dob():
    """ ()->int
    Returns sum of digits of dob
    """
    dob= input("Enter the DOB in format DD-MM-YYYY")
    sum1=0
    for ch in dob:
        if ch.isdigit():
            sum1+=int(ch)
    return count_num(str(sum1))
    
    

# Function to sum up the string
def count_string(str1):
    """  (str1)->int
    Returns sum of characters in the string
    >>>count_string('Amita')
    9
    >>> count_string('')
    0
    """
    count=0
    for ch in str1:
        if ch=='A' or ch=='J' or ch=='S' or ch=='a' or ch=='j' or ch=='s':
            count+=1
            count = count_num(str(count))
        elif ch=='B' or ch=='K' or ch=='T' or ch=='b' or ch=='k' or ch=='t':
            count+=2
            ccount = count_num(str(count))
        elif ch=='C' or ch=='L' or ch=='U' or ch=='c' or ch=='l' or ch=='u':
            count+=3
            count = count_num(str(count))
        elif ch=='D' or ch=='M' or ch=='V' or ch=='d' or ch=='m' or ch=='v':
            count+=4
            count = count_num(str(count))
        elif ch=='E' or ch=='N' or ch=='W' or ch=='e' or ch=='n' or ch=='w':
            count+=5
            count = count_num(str(count))
        elif ch=='F' or ch=='O' or ch=='X' or ch=='f' or ch=='o' or ch=='x':
            count+=6
            count = count_num(str(count))
        elif ch=='G' or ch=='P' or ch=='Y' or ch=='g' or ch=='p' or ch=='y':
            count+=7
            count = count_num(str(count))
        elif ch=='H' or ch=='Q' or ch=='Z' or ch=='h' or ch=='q' or ch=='z':
            count+=8
            count = count_num(str(count))
        elif ch=='I' or ch=='R' or ch=='i' or ch=='r' :
            count+=9
            count = count_num(str(count))
        else:
            count+=0
            count = count_num(str(count))
         
    return count_num(str(count))
        
#Function to add numbers
def count_num(str1):
    """ (str)->int
    Returns numeric value of the sum of digits
    >>> count_num('56')
    2
    >>>count_num('34')
    7
    """
    sum1=0
    for ch2 in str1:
        sum1+=int(ch2)

    if sum1>9:
        sum1=count_num(str(sum1))
        
    return sum1
