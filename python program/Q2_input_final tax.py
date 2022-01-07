
a=int(input("Enter your Gross Income(in nearest penny): $"))  #taking gross income input from user
b=int(input("Enter number of your Dependents: "))  #number of dependents given by user
c=a-10000-(3000*b)  # calculating tax income
Tax=c*0.2  #final tax
print("Your tax is $",Tax)
