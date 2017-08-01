import re

def hey(str):
    if re.search('([A-Z]{3,}|[1-9]{1},).*[?!]$', str):
    	return 'Whoa, chill out!'

    if re.search('[A-Z]{4,}', str):
    	return 'Whoa, chill out!'

    if re.search('(\xc4|\xe4|\xdc|\xfc)+.*!$', str):
    	return 'Whoa, chill out!'

    if re.search('^\s*$', str):
    	return 'Fine. Be that way!'

    if re.search('\?$|\? +$', str):
    	return 'Sure.'

    return 'Whatever.'