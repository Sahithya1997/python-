#Bank system

print("="*30)
customerNames=['sahithya','Daksha Brahmini','Manohar','Mahadev']
customerPins=['0123','4567','8910','1112']
customerBalances=[100000,200000,300303,69080]
deposition=0
withdrawal=0
balance=0
counter_1=1
counter_2=5

i=0 #temporary variable
#this statement below helps the program to run continuosly
while True:
    #os.system('cls')
    print("="*30)
    print(""*12,"welcome to Times Bank ",""*12)
    print("="*30)
    print("=<< 1.Open a new account       >>=")
    print("=<< 2.Withdraw Money           >>=")
    print("=<< 3.Deposit Money            >>=")
    print("=<< 4.Check Customers & Balance>>=")
    print("=<< 5.Exit/Quit                >>=")
    print("="*30)
    #The below statement takes the choice number from the user.
    choiceNumber=input("Select your choice number from above menu:")
    if choiceNumber=='1':
        print("choice number 1 is selected by the customer")
        #The  line below will atke the no.of customer from 
        NOC=eval(input("Number of Customers: "))  #NOC--number of customers eval--evalute

        i=i+NOC #stored in i
        #the if condition will restrict the no.of new account
        if i>5:
            print("\n")
            print("customer registration exceed reached or Customer registration too low")
            i=i-NOC
            while counter_1 <= i:
                #These few lines will take information from the customer
                name=input("Input Full name: ")
                customerNames.append(name)
                pin=str(input("please input a pin of your choice: "))
                customerPins.append(pin)
                balance=0
                deposition=eval(input("please input a value to deposit: "))
                balance=balance+deposition
                customerBalances.append(balance)
                print("/nName=",end="")
                print(customerNames[counter_2])
                print("pin=",end="")
                print(customerPins[counter_2])
                print("Balance",end="")
                print(customerBalnce[counter_2],end="")
                print("-/Rs")
                counter_1=counter_1+1
                counter_2=counter_2+1
                print("/nYour name is added to Cutomer system")
                print("Your pin is added to cutomer system")
                print("Your balance is added to customer system")
                print("----New account created successfully!----")
                print("/n")
                print("Your name is available on the customer list now:")
                print(customerNames)
                print("/n")
                print("Note please remember the Name and pin")
                print("="*30)
                #This statement below helps the user to go back to the start
        mainmenu=input("please press enter key to go back to main menu")
    elif choiceNumber=="2":
        j=0
        print("Choice number 2 is selected by the customer")
        #This ehile loop will prevent the user using the account
        while j<1:
            k=-1
            name=input("please input name: ")
            pin=input("please input pin: ")
            #Thie while loop will keep the function running when variable k is smaller than the length
            #CutomerNames list.
            while k<len(customerNames)-1:
                k=k+1
                #Thses two if conditions find where both the name and pin matches.
                if name==customerNames[k]:
                    if pin==customerPins[k]:
                        j=j+1
                        #These few statement would show the balance taken from the list
                        print("Your Current Balance:",end="")
                        print(customerBalances[k],end="")
                        print("-/Rs\n")
                        balance=customerBalances[k]
                        #statemnet below would show the balance taken from the list
                        withdrawal=eval(input("input value to withdraw:"))

                        #The if condition below would look whether the withdraw is 
                        if withdrawal>balance:
                            #This statement below would taken a deposition from the customer
                            deposition=eval(input("Please deposite a higher value because your balance mentioned above is not enough:"))
                            #These few statements would update the value and show the balance to user
                            balance=balance+deposition  
                            print("your current balance:",end="")
                            print(balance,end="")
                            print("-/Rs\n") #1000-500=500
                            balance=balance-withdrawal
                            print("-\n")
                            print("---withdraw successfull!---")
                            customerBalances[k]=balance
                            print("Your New Balance:",balance,end="")
                            print("-/Rs\n\n")
                    else:
                        #else condition mentioned above is to do withdrawal if the balance is greater than withdrawl amount 
                        #withdraw amount
                        balance=balance-withdrawal
                        #these few statement would update the values in the list and show it to the customer
                        print("\n")
                        print("----withdraw Successfull---")
                        customerBalances[k]=balance
                        print("your New Balance: ",balance,end='')
                        print("-/Rs\n\n")
            if j<1:
                #if condition above would work when the pin or the name is wrong.
                print("Your name and pin does not match!\n")
                break
            #This statement below helps the user to go back to the mainmenu
        mainMenu=input("please pres enter key to go to mainmenu: ")
    elif choiceNumber=="3":
        print("choice number 3 is selected by the cutomer")
        n=0
        #The while loop below would work when the pin or the user name  invalid
        while n<1:
            k=-1
            name=input("please inut name: ")
            pin=inpu("please input pin: ")
            #The while loop below will keep the function running 
            while k<len(customerNames)-1:
                k=k+1
                #The two if conditions below would find whether
                if name==customerNames[k]:
                    if pin==customerPins[k]:
                        n=n+1
                        #These statements below would show the customer the deposition 
                        #The deposition made
                        print("your current Balance: ",end="")
                        print(customerBalances[k],end="")
                        print("-/Rs")
                        balance=(customerBalances[k])
                        #This statement below takes the deposition from the customer
                        deposition=eval(input("enter the value you want deposite  amount: "))
                        balance=balance+deposition #1000+500=1500
                        customerBalances[k]=balance
                        print("\n")
                        print("----Deposition sucssfull!----")
                        print("Your New Balance: ",balance,end="")
                        print("-/Rs\n\n")
                if n<1:
                    print("Your name and pin does not match!\n")
                    break
                #This statement below helps the user to go back to mainMenu
            mainMenu=input("pleasebpress enter key go back to mainmenu: ")
    elif choiceNumber=="4":
        print("Choice number 4 is selected by the customer")
        k=0
        print("customer name list and balance mentioned below: ")
        print("\n")
            #The while loop below will keeping running untill 
        while k<=len(customerNames)-1:
            print("->.Customer=",customerNames[k])
            print("->.Balance",customerBalances[k],end="")
            print("-/Rs")
            print("\n")
            k=k+1
                #These statement below helps the user to go back to mainmenu
            mainMenu=input("please press enter key go back to mainmenu: ")
    elif chiceNumber=="5":
                #These statements would be just showed to the customer.
        print("Choice number 5 is selected by the customer")
        print("Thank you for using our banking system")
        print("\n")
        print("come again")
        print("Bye Bye")
        break
    else:
     #This else function above would work when wrong function
        print("invalid option selected by the customer")
        print("please try again")
        #This statement below help the user to go back to mainmenu
        mainMenu=input("please press enter key go back to mainmenu: ")





                        







                         
                        





                



            
                




