def totalFruit(fruits: List[int]) -> int:
	# If you don't have this you'll get a time limit exceeded error.
	if len(set(fruits)) <= 2:
		return len(fruits)

	max_len = 0
	left = 0

	for i in range(len(fruits) + 1):
		while len(set(fruits[left:i])) > 2:
			left += 1

		if len(fruits[left:i]) > max_len:
			max_len = len(fruits[left:i])

	return max_len