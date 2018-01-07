Implement database in MongoDB as an example of a document-oriented NOSQL system, and see how data is stored and queried in such a system. 

Following are the steps:

We are Using Python.
1.	Perform SQL database connection
2.	Load Data for all tables in SQL
3.	Create MongoDB database
4.	Create two Collections 'Projects_Collection' and 'Departments_Collection'
5.	Write SQL query for Projects Collections by joining Employee, Department, Projects and WorkOn Tables and fetch the required columns from each of the tables as follows:
PNumber, Pname,Dname,Fname,Lname,Hours
6.	Execute the above query and fetch all the rows of results in a variable project_result
7.	Create a python dictionary project_document = {}
8.	Map the results that is stored in the project_result and create a json object or document by creating a dictionary where PNumber will be Key 
9.	Insert the created dictionary in project collection document
10.	Write SQL query for Department Collections by joining Employee, Department, Dept_Locations Tables and fetch the required columns from each of the tables as follows:
Dname,Lname,Dept_Locations
11.	Execute the above query and fetch all the rows of results in a variable department_result
12.	Create a python dictionary department_document = {}
13.	Map the results that is stored in the department _result and create a json object or document by creating a dictionary where DName will be Key 
14.	Insert the created dictionary in departments collection document
15.	Print both the collections and the documents

Data Structures:
Programming Language: Python
Data Structure: 
Python Dictionary: to create JSON object 
List: For list of Employees and Department in the dictionary


Explanation:
1. Show all the database command as follows:
 show dbs
Result of above command.
Project2  0.000GB
admin     0.000GB
local     0.000GB
myNewDB   0.000GB
2. Switch to current database “myNewDB” by following command
> use myNewDB
switched to db myNewDB
3. Display all existing Collections by following command
> show collections
Results of above command
Emp
myNewCollection1
4. Create a new collection “newDemo”
> db.createCollection("newDemo")
{ "ok" : 1 }
5. Check if the collection is created by command “show collections”
> show collections
Emp
myNewCollection1
newDemo
6. Insert a Document as follows
> db.newDemo.insert({"testkey":"Id","testvalue":"101"})
WriteResult({ "nInserted" : 1 })				#Result 
7. Query to find the document in the collections
> db.newDemo.find()
Result displays the document inserted
{ "_id" : ObjectId("5986e4442789cebe9b88017d"), "testkey" : "Id", "testvalue" : "101" }




STEPS FOR INSTALLING MONGO DB ON WINDOWS:

Download the latest production release of MongoDB Enterprise.

Install MongoDB Enterprise by locating the downloaded .msi file and completing the installation process.


For setting up the MongoDB environment, a folder is created which acts as data directory for MongoDB by typing “md \ data\ db”.

For starting MongoDB, run mongod.exe. Choose “Allow access” for security alert pop ups.


For connecting to MongoDB through mongo.exe shell open command prompt and type “C:\Program Files\MongoDB\Server\3.4\bin\mongo.exe”.

For stopping MongoDB , press Control + C in the terminal where mongod instance is running.


