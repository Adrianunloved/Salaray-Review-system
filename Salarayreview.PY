print("-----------------Title Boxing Salary review System -Hit it Hard----------------")
EMPloyeeINFo={}
totalsalary = 0
Retirementsalary = 0
allNetSalary = 0
maxsalary = 0
maxname =[]
for W in range(3):
    NetSalary = 0
    Nameinquire=input("What is your name")
    SSInquire=input("Input your social security code")
    Payinquire=int(input("What is your salary"))
    totalsalary += Payinquire
    Percentage=int(input("what percentage of salary do you contribute to retirement"))
    if Percentage<0 or Percentage>40:
            Percentage=(input("percentage invalid please input valid percentage "))
    Retirementsalary += Payinquire * Percentage
    NetSalary = (Payinquire - Retirementsalary)
    allNetSalary +=  NetSalary
    EMPloyeeINFo.update({Nameinquire: (SSInquire, Payinquire, Percentage,NetSalary)})


print("Employee Code      Salary           Retirement         Net Salary ")
for key in EMPloyeeINFo:
    splitname = key.split(" ")
    lastname = splitname[1]

    val = EMPloyeeINFo[key]
    ssn = str(val[0])
    empcode = lastname + ssn[-4:]
    sal = int(val[1])
    pct = float(val[2])
    Net = float(val[3])
    # print(key,val)
    print("%s         $%.2f              $%.2f             $%.2f" % (empcode, sal, sal * pct,(Net*-1)))


print("                             super Salary System Advanced                       ")
print("_________________________________________________________________________________")
print("total")
print("               $%.2f              $%.2f             $%.2f"  % (totalsalary,Retirementsalary,(allNetSalary*-1)))

print( "Note %s has the highest salaray at $%.2f" % (maxname,maxsalary))
