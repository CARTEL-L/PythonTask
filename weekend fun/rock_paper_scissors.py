fp = input('player one enter play: ')
sp = input('player two enter play: ')
if (fp)== 'rock' and sp == 'scissors':
	print('Player 1 wins')
elif(fp)== 'rock' and sp == 'paper':
	print('Player 2 wins')
elif(fp) == 'rock' and sp == 'rock':
	print('Tie')
elif(sp)== 'rock' and fp == 'scissors':
	print('Player 2 wins')
elif(sp)== 'rock' and fp == 'paper':
	print('Player 1 wins')
elif(fp)== 'scissors' and sp == 'paper':
	print('Player 1 wins')
elif(fp)== 'paper' and sp == 'scissors':
	print('Player 2 wins')
elif(fp)== 'paper' and sp == 'paper':
	print('Tie')
elif(fp)== 'scissors' and sp == 'scissors':
	print('Tie')