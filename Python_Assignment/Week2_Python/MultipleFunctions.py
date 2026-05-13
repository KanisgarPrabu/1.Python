class MultipleFunctionsClass():
    def Subfields():
        list = ("Machine Learning" ,"Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing")
        print("Sub-fields in AI are:")
        for i in list:
            print(i)

    # Create Odd or even Function
    def OddEven():
        num = int(input("Enter a number"))
        if (num%2==0):
            print(f"{num} is Even number")
        else:
            print(f"{num} is Odd number")
    #Create Marriage Eligibilty Function based on gender
    def Elegible():
        gender = input("Your Gender")
        age = int(input("Your age"))
        if (gender.upper()=='MALE'):
           if(age<21):
               print("NOT ELIGIBLE")
           else:
               print("Eligible")
        elif(gender.upper()=="FEMALE"):
            if (age <19):
                print("NOT ELIGIBLE")
            else:
                print("ELIGIBLE")
    #Function to calculate 10th Percentage
    def percentage():
        Subject1 = int(input("Subject1="))
        Subject2 = int(input("Subject2="))
        Subject3 = int(input("Subject3="))
        Subject4 = int(input("Subject4="))
        Subject5 = int(input("Subject5="))
        total = Subject1+Subject2+Subject3+Subject4+Subject5
        print("Total :",total)
        percentage = (total/500)*100
        print("Percentage :",percentage)

    #Function to find area and perimeter of a triangle
    def triangle():
        Height = int(input("Height:"))
        Breadth = int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle:" , (Height*Breadth)/2)
        Height1 = int(input("Height1:"))
        Height2 = int(input("Height2:"))
        Breadth = int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triange:",(Height1+Height2+Breadth))