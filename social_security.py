import csv

with open('csvData.csv', mode='r') as infile:
    reader = csv.reader(infile)
    mydict = list(reader)
    ssnCode = input("Enter the first 3 digits of SSN to lookup: ")
    for i in range(0,len(mydict)):
        if len(mydict[i][1]) > 4:
            if mydict[i][1][3] == "-":
                args = mydict[i][1].split('-')
                for num in range(int(args[0]),int(args[1])+1):
                    if int(ssnCode) == num:
                        print("SSN Code " + ssnCode + " belongs to " + mydict[i][0] + ".")
                        exit()
            elif mydict[i][1][3] == " ":
                args = mydict[i][1].split(' ')
                if ssnCode == args[1]:
                        print("SSN Code " + ssnCode + " belongs to " + mydict[i][0] + ".")
                        exit()
                if ssnCode == args[1]:
                        print("SSN Code " + ssnCode + " belongs to " + mydict[i][0] + ".")
                        exit()
        elif ssnCode == mydict[i][1]:
            print("SSN Code " + ssnCode + " belongs to " + mydict[i][0] + ".")
            exit()
    print("No match for that SSN Code.")