# Write a program that will determine weather when the value of temperature and Humidity is provided by user.


temp = float(input("Enter the Temperature"))
hum = float(input("Enter the Humidity"))

if temp >= 30 and hum >= 90 :
    print("Hot and Humid")

elif temp >= 30 and hum < 90 :
    print("Hot")

elif temp < 30 and hum >= 90 :
    print("Cool and Humid")

elif temp < 30 and hum < 90 :
    print("Cool")   

else:
    print("Please give approprate Humidity and Temperature") 
