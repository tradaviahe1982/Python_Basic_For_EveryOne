TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000
DEPENDENT_DEDUCTION = 3000
grossIncome = float(input('Nhập tổng thu nhập cá nhân: '))
numDependents = int(input('Nhập số người phụ thuộc: '))
taxableIncome = grossIncome - STANDARD_DEDUCTION - (DEPENDENT_DEDUCTION*numDependents)
incomeTax = taxableIncome * TAX_RATE;
print ("Thuế thu nhập cá nhân là $: " + str(incomeTax))
