# !\usr\bin\python3
import csv
import pymysql

mydb = pymysql.connect(host='127.0.0.1', user='root', passwd='moon2far1!', db='Company', port=3306, charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)
cursor = mydb.cursor()

sql1 = "INSERT INTO Company.Project values (%s,%s,%s,%s);"
sql2 = "INSERT INTO Company.DEPT_LOCATIONS values (%s,%s);"
sql3 = "INSERT INTO Company.Department values (%s,%s,%s,%s);"
sql4 = "INSERT INTO Company.WorksOn values (%s,%s,%s);"
sql5 = "INSERT INTO Company.EMPLOYEE values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"

csv_data1 = csv.reader(open('Project.csv'))
csv_data2 = csv.reader(open('DEPT_LOCATIONS.csv'))
csv_data3 = csv.reader(open('DEPARTMENT.csv'))
csv_data4 = csv.reader(open('WORKS_ON.csv'))
csv_data5 = csv.reader(open('EMPLOYEE.csv'))

#For Project data
for value in csv_data1:
    cursor.execute(sql1, (value[0], value[1], value[2], value[3]))
#
#For loading Department Locations data
for value in csv_data2:
    cursor.execute(sql2, (value[0], value[1]))
#
#For Loading Department data
for value in csv_data3:
    cursor.execute(sql3, (value[0], value[1], value[2], value[3]))
#
#For loading Work_On data
for value in csv_data4:
    cursor.execute(sql4, (value[0], value[1], value[2]))

#For Employee Data
for value in csv_data5:
    # print (value[1])
    cursor.execute(sql5, (value[0], value[1],value[2], value[3],value[4], value[5]+", "+value[6]+", " +value[7],value[8], value[9],value[10],value[11]))

mydb.commit()

mydb.close()
