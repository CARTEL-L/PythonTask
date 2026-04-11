number = int(input('Enter digit: '))
hours = number // 0.0166668
minutes = hours // 60
seconds = minutes // 60
print(hours, 'hours ', minutes, 'minutes and', seconds, 'seconds')
