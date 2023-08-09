# Author: Donaven Bruce

#variables for specific marital status/age group
married_count = 0
single_count = 0
divorced_count = 0
separated_count = 0

married_above_50 = 0
married_40s = 0
married_30s = 0
married_20s = 0

single_above_50 = 0
single_40s = 0
single_30s = 0
single_20s = 0

divorced_above_50 = 0
divorced_40s = 0
divorced_30s = 0
divorced_20s = 0

separated_above_50 = 0
separated_40s = 0
separated_30s = 0
separated_20s = 0

count = 0

# here i use while loop to collect information from user
while count < 6:
    marital_status = input("Please enter the person's marital status: ")
    age = int(input("Please enter the person's age: "))
    #check relationship status and age and accumulate the specific counter 
    if marital_status == "married" or marital_status == "MARRIED":
        married_count = married_count + 1
        if age >= 50:
            married_above_50 = married_above_50 + 1
        elif age >= 40:
            married_40s = married_40s + 1
        elif age >= 30:
            married_30s = married_30s + 1
        elif age >= 20:
            married_20s = married_20s + 1
    elif marital_status == "single" or marital_status == "SINGLE":
        single_count = single_count + 1
        if age >= 50:
            single_above_50 = single_above_50 + 1
        elif age >= 40:
            single_40s = single_40s + 1
        elif age >= 30:
            single_30s = single_30s + 1
        elif age >= 20:
            single_20s = single_20s + 1
    elif marital_status == "divorced" or marital_status == "DIVORCED":
        divorced_count = divorced_count + 1
        if age >= 50:
            divorced_above_50 = divorced_above_50 + 1
        elif age >= 40:
            divorced_40s = divorced_40s + 1
        elif age >= 30:
            divorced_30s = divorced_30s + 1
        elif age >= 20:
            divorced_20s = divorced_20s + 1
    elif marital_status == "separated" or marital_status == "SEPARATED":
        separated_count = separated_count + 1
        if age >= 50:
            separated_above_50 = separated_above_50 + 1
        elif age >= 40:
            separated_40s = separated_40s + 1
        elif age >= 30:
            separated_30s = separated_30s + 1
        elif age >= 20:
            separated_20s = separated_20s + 1
    else:
        print("Sorry! The marital status does not belong to one of the known statuses")

    count = count + 1

#Display the number of people for each group
print("The number of people who are married is:", married_count)
print("The number of people who are married and over 50 is:", married_above_50)
print("The number of people who are married and in the age group of 40's is:", married_40s)
print("The number of people who are married and in the age group of 30's is:", married_30s)
print("The number of people who are married and in the age group of 20's is:", married_20s)
print("")

print("The number of people who are single is:", single_count)
print("The number of people who are single and over 50 is:", single_above_50)
print("The number of people who are single and in the age group of 40's is:", single_40s)
print("The number of people who are single and in the age group of 30's is:", single_30s)
print("The number of people who are single and in the age group of 20's is:", single_20s)
print("")

print("The number of people who are divorced is:", divorced_count)
print("The number of people who are divorced and over 50 is:", divorced_above_50)
print("The number of people who are divorced and in the age group of 40's is:", divorced_40s)
print("The number of people who are divorced and in the age group of 30's is:", divorced_30s)
print("The number of people who are divorced and in the age group of 20's is:", divorced_20s)
print("")

print("The number of people who are separated is:", separated_count)
print("The number of people who are separated and over 50 is:", separated_above_50)
print("The number of people who are separated and in the age group of 40's is:", separated_40s)
print("The number of people who are separated and in the age group of 30's is:", separated_30s)
print("The number of people who are separated and in the age group of 20's is:", separated_20s)