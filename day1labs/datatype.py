def data_type(x):
	x_type =type(x)
	if x_type == str:
		return len(x)
	elif x_type ==bool:
		return x
	elif x_type ==int:
		if x == 100:
			return 'equal to 100'
		elif x < 100:
			return 'less than 100'

		else:
			return 'more than 100'

	elif x_type ==list:
		try:
			if x[2]:
				return x[2]
		except(IndexError):
			return None
	else:
		return 'no value'

