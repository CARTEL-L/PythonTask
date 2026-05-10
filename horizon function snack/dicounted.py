def my_store(discount):
	print(discount)

item = input("Enter item name: ")
price = int(input('Enter item price: '))
promo_code = input('Enter promotional code: ')
if (promo_code)== "SAVE10":
	print('discounted price is', price-(price * 0.10))
elif (promo_code)== 'HALFOFF':
	print('discounted price is', price//2)
else:
	print("no discount")