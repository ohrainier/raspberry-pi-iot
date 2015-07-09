print "starting. . . . "
tempfile = open("/sys/bus/w1/devices/28-000004ac2572/w1_slave")
msg = tempfile.read()
tempfile.close()
tempdata = msg.split("\n")[1].split(" ")[9]
temperature = float(tempdata[2:])
temperature = temperature/1000
fahrenheitTemp = temperature * 9/5 + 32

print "Celsius: ", temperature
print "Fahrenheit: ", fahrenheitTemp
