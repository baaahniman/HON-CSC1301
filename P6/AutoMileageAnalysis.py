import sys
from Date import *


with open(sys.argv[1], 'r') as f:
    contents = f.read()

data = []
for items in contents.splitlines():
    data.append(items)

print("\nAuto Gas Analysis, Year {}".format(data[1]))
print("{}\n".format(data[0]))
print("Date                Gallons   $Spent MilesDriven DaysToNextFill    MPG")
print("----------------------------------------------------------------------")

new_data = {}
miles = []
for item in data[2:]:
    x = item.split("&")
    new_data[x[0]] = []
    new_data[x[0]].append(x[1:]) # Key is date and value is other contents
    miles.append(x[3])

miles_travelled = []
for i in range(0,len(miles)-1):
    miles_travelled.append(int(miles[i+1])-int(miles[i]))
miles_travelled.pop()


date = []
for keys, values in new_data.items():
    dates = keys.strip()
    indivisual_date = dates.split("/")
    date.append(indivisual_date)

datesinbetween = []
count = 0
indivisual_list = []
total_gallons = 0
total_spent = 0
total_miles = 0
total_next_days = 0
total_mpg = 0
for keys, values in new_data.items():
    dates = keys.strip()
    indivisual_date = dates.split("/")
    indivisual_list.append(indivisual_date)
    m = indivisual_date[0]
    d = indivisual_date[1]
    y = indivisual_date[2]
    dates = Date(int(m),int(d),int(y))
    total_gallons += float(values[0][0])
    total_spent += float(values[0][1])
    if count < len(new_data)-2:
        datesinbetween.append(dates.days_between(Date(int(date[count+1][0]),int(date[count+1][1]),int(date[count+1][2]))))
        #print(miles_travelled[count])
        mpg = (float(miles_travelled[count])/float(values[0][0]))
        #print(dates," "*(18-len(str(dates))),values[0][0],values[0][1]," "*4,miles_travelled[count]," "*12,datesinbetween[count]," ","{:.2f}".format(mpg))
        print("%-18s%9.2f%9.2f%12d%10d%12.2f" %(dates,float(values[0][0]),float(values[0][1]),miles_travelled[count],datesinbetween[count],float(mpg)))
        total_miles += int(miles_travelled[count])
        total_next_days += int(datesinbetween[count])
        total_mpg += float(mpg)
    if count == len(new_data)-2:
        print("%-18s%9.2f%9.2f" %(dates,float(values[0][0]),float(values[0][1])))
    count += 1

print("----------------------------------------------------------------------")
print("Totals:"," "*12,"%.2f"%(total_gallons)," "*1,"%.2f"%(total_spent)," "*6,total_miles)
print("Averages:"," "*45,int(total_next_days/(len(new_data)-2))," "*5,"%.2f"%(total_mpg/(len(new_data)-2)))
print("----------------------------------------------------------------------")
print()

    


    

    
