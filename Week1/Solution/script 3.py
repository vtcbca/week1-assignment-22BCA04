#write a python script to enter any number and check it is palindram or not
n=input("Enter Any Number:: ")
n1=n[-1::-1]  #using for slicingS
if n==n1:
    print("{} is a palindrom number".format(n))
else:
    print("{} is not a palindrom number".format(n))
