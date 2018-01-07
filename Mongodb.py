import pymysql
from pymongo import MongoClient
from lxml import etree

mydb = pymysql.connect(host='127.0.0.1', user='root', passwd='moon2far1!', db='Company', port=3306, charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)
conn = mydb.cursor()

client = MongoClient("localhost",27017)
db_client = client['Project2']
database = db_client['MongoProject2']
project_collection = database['Projects_Collection']
department_collection = database['Departments_Collection']


query1 = "Select Proj.Pnumber,Proj.Pname,Dept.Dname,Emp.Fname, Emp.Lname,WO.hours " \
         "from Project as Proj inner join Department as Dept " \
         "inner join Workson as WO inner join Employee as Emp " \
         "ON Proj.DNumber = Dept.DNumber " \
         "and Proj.PNumber = WO.ProjectNumber and WO.essn = Emp.EmployeeSSN"

conn.execute(query1)
project_result = conn.fetchall()

project_document = {}

for proj in project_result:
    if proj['Pnumber'] not in project_document:
        project_document[proj['Pnumber']] = {"Project_Number":proj['Pnumber'],"Project_Name":proj['Pname'],"Department_Name":proj['Dname'] , "Employee" : []}

    project_document[proj['Pnumber']]['Employee'].append({"First_Name": proj['Fname'], "Last_Name": proj['Lname'], "Hours_Worked": proj['hours']})

for p in project_document.values():
    project_collection.insert_one(p)


print(project_document)
print(len(project_document.keys()))

#Creating XML Document for Projects Document
projects_root = etree.Element("Projects")

for proj in project_document.values():
    Project_Element = etree.SubElement(projects_root,"Project")
    Project_Element.attrib["Project_No"]= str(proj['Project_Number'])
    Project_Name = etree.SubElement(Project_Element,"Project_Name")
    Project_Name.text = proj['Project_Name']
    Dept_Name = etree.SubElement(Project_Element,"Dept_Name")
    Dept_Name.text = proj['Department_Name']
    Employees = etree.SubElement(Project_Element,"Employees")
    for emp in proj["Employee"]:
        Employee = etree.SubElement(Employees,"Employee")
        FirstName = etree.SubElement(Employee,"FirstName")
        FirstName.text = emp['First_Name']
        LastName = etree.SubElement(Employee,"LastName")
        LastName.text = emp['Last_Name']
        Hours = etree.SubElement(Employee,"Hours")
        Hours.text = str(emp['Hours_Worked'])

xml = etree.tostring(projects_root, pretty_print=True)
with open("Project.xml","wb") as file:
    file.write(xml)


query3 = "Select Dept.Dname,Emp.Lname,DLoc.Location_Name from (Department as Dept left outer join Dept_Locations as DLoc " \
         "on Dept.DNumber = DLoc.Location_No) inner join Employee as Emp on Dept.ESSN = Emp.EmployeeSSN"
conn.execute(query3)

dept_result = conn.fetchall()

department_document = {}
print(dept_result)
for dept in dept_result:
    if dept['Dname'] not in department_document:
        department_document[dept['Dname']] =  {"DeptName":dept['Dname'], "LastName" :dept['Lname'], "DLocation": []}
    department_document[dept['Dname']]["DLocation"].append(dept['Location_Name'])

print(department_document)
print(len(department_document.keys()))

for d in department_document.values():
    department_collection.insert_one(d)

departments_root = etree.Element("Department")

for dept in department_document.values():
    Department_Name = etree.SubElement(departments_root,"Department")
    Department_Name.text= dept['DeptName']
    Last_Name = etree.SubElement(departments_root,"LastName")
    Last_Name.text = dept['LastName']
    Dept_Location = etree.SubElement(departments_root,"Department_Locations")
    for loc in dept["DLocation"]:
        DLocation = etree.SubElement(Dept_Location,"Dept_Location")
        DLocation.text = loc

xml = etree.tostring(departments_root, pretty_print=True)
with open("Department.xml","wb") as file:
    file.write(xml)



