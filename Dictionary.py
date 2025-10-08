dict={'susheel':500 , 'Hari':600 , 'Ramu':700}
name=input("Enter student's name: ")
if name in dict:
    print("{}'s marks: {}".format(name,dict[name]))
else:
    print("Student not found.")