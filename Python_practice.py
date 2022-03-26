print("Hellow World")
counties = ['Arapahoe', 'Denver', 'Jefferson']
print(counties[2])
x=len(counties)
print(x)
#counties2 = counties[0,2]
#print[counties2]
counties.append("El Paso")
print(counties)
counties.insert(9,"Emad")
print(counties)
counties.remove("Emad")
print(counties)
counties.pop(2)
print(counties)



#disctionary

my_dictionary = dict()
my_dictionary = {}

counties_dict{}
counties_dict["Arapahoe"] = 422829, [Denver]=463353,[Jefferson]=432438

print("len(counties_dict)")


print("counties_dict.keys()")
print("counties_dict.values()")
print("counties_dict.items()")



#print a value from dictionary
counties_dict['Arapahoe']
counties_dict.get("Arapahoe")
print(counties_dict['Arapahoe'])
print(counties_dict.get("Arapahoe"))

voting_data = []
 voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
 voting_data.append({"county":"Denver", "registered_voters": 463353})
 voting_data.append({"county":"Jefferson", "registered_voters": 432438})
 print("voting_data")





 #for loop in dictionary - return the keys in dictionary
 for county in countries_dict.keys()
    print(country)

#for loop in dictionary - return the values in dictionary
for voters in country_dict.values()
    print(voters)

#Or
for county in counties_dict:
        print(counties_dict.get(country))    

#to get both value and key in a dictionary
for county, voters in counties_dict.items():
    print(county, voters)


#for loop in a list
for i in range(len(counties)):
    print(counties[i])
