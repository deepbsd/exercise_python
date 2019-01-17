def raindrops(number):
    mesg = ""
    if number % 3 == 0: mesg += 'Pling'
    if number % 5 == 0: mesg += 'Plang'
    if number % 7 == 0: mesg += 'Plong'
    return "{}".format(mesg or str(number))
