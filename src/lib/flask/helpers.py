def routeMatch(routeRule, routeInput):	
	routeRuleSplit = routeRule.split('/')
	routeInputSplit = routeInput.split('/')

	if len(routeRuleSplit) != len(routeInputSplit):
		return False, None

	params = {}
	for i in range(len(routeRuleSplit)):
		if '<' in routeRuleSplit[i]:
			# <int:postID>, <float:longitude>, <username>
			rule = routeRuleSplit[i]
			rule = rule.replace('<', '|')
			rule = rule.replace(':', '|')
			rule = rule.replace('>', '|')
			ruleSplit = rule.split('|')

			# <int:postID>
			if ruleSplit[1] == 'int':
				try:
					value = int(routeInputSplit[i])
					params[ruleSplit[2]] = value
				except ValueError:
					return False, None
						
			# <float:longitude>
			elif ruleSplit[1] == 'float':
				try:
					value = float(routeInputSplit[i])
					params[ruleSplit[2]] = value
				except ValueError:
					return False, None

			# <username>
			else:
				params[ruleSplit[1]] = routeInputSplit[i]
 
		else:
			if routeRuleSplit[i] != routeInputSplit[i]:
				return False, None

	return True, params

