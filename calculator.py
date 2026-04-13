principle = int(input('Enter amount: '))
rate = float(input('Interest rate: '))
duration = int(input('Duration: '))
P1 = rate * (1 + rate)**duration
P2 = (1 + rate)**duration-1
M = P1/P2
print('Monthly interest rate is', M)
