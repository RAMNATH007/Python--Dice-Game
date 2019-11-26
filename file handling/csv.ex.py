import csv
with open("student.csv","w") as f:
    a=csv.writer(f)
    a.writerow(["NAME","ID","MARKS","ADDRESS"])
    while True:
        name=input("enter s_name:")
        id=input("enter s_id")
        marks=int(input("enter s_marks"))
        addr=input("enter s_addr")
        a.writerow([name,id,marks,addr])
        option=input("Do you want to insert one more record[Yes|no]:")
        if option.lower()=="no":
            break
    print("students data are inserted successfully")
import csv
with open('student.csv','r+') as f:
    r=csv.reader(f)
    w=csv.writer(f)
    data=list(r)
    for row in data:
        if row[0]=="ramnath":
            w.writerow([row[0],100,row[2],row[3]])