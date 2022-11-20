alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number=['0','1','2','3','4','5','6','7','8','9']
input_letter=input("enter a letter")

if (input_letter in alphabet):
    print(input_letter +"is alphabet")
elif(input_letter in number):
    print(input_letter+" is a number")
else:
    print(input_letter+" is not a number alphabet ")


# < ---------------------------------------------------------METHOD 2 ---------------------------------------->

if('A'<=input_letter <='Z' or 'a'<= input_letter <='z'):
    print(input_letter + "is a alphabet")
else:
    print("not a alphabet")
