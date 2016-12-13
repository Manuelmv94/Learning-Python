print ("Temperature Converter")
print ("Enter the temperature you want to convert from Fahrenheit degrees to Celsius degrees")
F=int(input())
C=5*(F-32)/9
print ("A temperature of %s degrees Fahrenheit is %s in Celsius" % (F,C))
if C > 100 :
	print ("Water boils at this temperature (under typical conditions)")
else:
	print ("Water does not boil at this temperature (under typical conditions)")
