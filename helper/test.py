
import re
userbudget="t300-700ads"
less="<700"
temp = 0
try :
    if '<' in userbudget:
        temp = int(re.findall(r'\d+', userbudget)[0]) - 1
    elif '>' in userbudget:
        temp = int(re.findall(r'\d+', userbudget)[0]) + 1
    elif '-' in userbudget:
        temp = int(re.findall(r'\d+', userbudget)[1])
    else :
        temp = str(userbudget)
except :
     print("")

print(temp)

if userbudget.isdigit():
    price = int(userbudget)
    if price == 1:
        rangeMax = 299
    elif price == 2:
        rangeMin = 300
        rangeMax = 700
    elif price == 3:
        rangeMin = 701
    elif price < 300:
        rangeMax = 299
    elif price < 701 and price >= 300:
        rangeMin = 300
        rangeMax = 700
    else:
        rangeMin = 701
else:
    rangeMin = 300
    rangeMax = 700
print(" Min: " + str(rangeMin) + " Max: " + str(rangeMax))

#try :
#    temp = re.findall(r'\d+', userBudget)[0]
#    print(temp)
#except :
#    rangeMin = 300
#    rangeMax = 700
#userbudget = [int(i) for i in userBudget.split() if i.isdigit()]
#print(userbudget)