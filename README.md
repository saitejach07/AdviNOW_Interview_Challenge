# Goal of the Assignment:
 ## Primary Goal : 
  1.Design and implement a backend framework with Fast API <br/> 
  2.Develop databases <br/> 
  3.Design usable API for business logic functional interfaces and CSV import and export. <br/> 

 ## The final deliverables include:
  1.A populated database. <br/> 
  2.Two working APIs: <br/> 
       One for accessing filtered data pertaining to businesses and symptoms. <br/> 
       One for data import from CSV file. <br/> 
      
-----------------------------------------------------------------------------------------------------

# Organising the task / Steps Followed :

## 1. Setting Up the Environment 
Created a Virtual Environment - isolated environment & Installed the Dependencies <br/> 
### To create Venv <br/> 
python3 -m venv venv <br/> 
### To Activate Venv <br/> 
source venv/bin/activate <br/> 
### To Install Dependencies <br/> 
pip install -r requirements.txt <br/> 

## 2. Created Data Models <br/> 
Here I've defined the Business and Symptom models in models.py using SQLAlchemy. <br/> 
This will define the relation b/w both the tables<br/> 
Please check the app/models.py for updated code<br/> 

## 3. Created a DB - I've chose SQlite & Generated Migration Script and Run Migration <br/> 
update settings.py to configure db_url for SQlite  <br/> 
### After that generate & apply the migration scrip using following cmds       <br/>  
alembic revision --autogenerate -m "Initial migration  <br/> 
alembic upgrade head  # This will create .dp file <br/> 

## 4. Desiging a Database Mock-Up Based on the Provided Data  <br/>  
Here I've analyzed the structure of the business_symptom_data.csv by Using the following columns <br/>  
Business ID Business Name Symptom Code Symptom Name Symptom Diagnostic <br/>  

## 5. Created '/import' Endpoint for Importing a CSV File <br/>  
### Implemented the /import endpoint in views.py which accepts CSV file to upload and populate the businesses and symptoms tables.  <br/>  
Used, @router.post("/import") #this is a decorator that defines a POST route at the /import endpoint within an APIRouter.  <br/>  

## Testing : Tested using the below cmd
curl -X POST "http://127.0.0.1:8013/import" \
-F "file=@/path/to/business_symptom_data.csv"

## Output : 
(venv) curl -X POST "http://127.0.0.1:8013/import" \
-F "file=@/Users/saitejachatarajupalli/Downloads/ADviNOW/interview-challenge-v2/app/data/business_symptom_data.csv" <br/> 

{"message":"Data imported successfully"}% <br/> 

## 6. Created '/data' endpoint that returns business and symptom data
### Implemented the /data endpoint in views.py which gets and return business and symptom data.
Used, @router.get("/data") <br/> 
def get_data() <br/> 

## Testing : Tested using the below cmd
curl -X 'GET' \
  'http://127.0.0.1:8013/data?business_id=1104&diagnostic=true' \
  -H 'accept: application/json'

## Output :
[{"Business ID":1104,"Business Name":"MedStop","Symptom Code":"SYMPT0001","Symptom Name":"Patient Age","Symptom Diagnostic":"1"},{"Business ID":1104,"Business Name":"MedStop","Symptom Code":"SYMPT0010","Symptom Name":"Fatigue","Symptom Diagnostic":"1"},{"Business ID":1104,"Business Name":"MedStop","Symptom Code":"SYMPT0012","Symptom Name":"Headache","Symptom Diagnostic":"1"},{"Business ID":1104,"Business Name":"MedStop","Symptom Code":"SYMPT0070","Symptom Name":"Rash","Symptom Diagnostic":"1"}]% 

## SQlite cmds:
### sqlite3 app.db <br/> 
SQLite version 3.39.5 2022-10-14 20:58:05 <br/> 
Enter ".help" for usage hints.<br/> 
### .tables <br/> 
alembic_version  businesses       symptoms   <br/> 
### SELECT * FROM businesses; <br/> 
1004|SportHealth <br/> 
1104|MedStop<br/> 
### SELECT * FROM symptoms; <br/> 
1|SYMPT0001|Patient Age|1|1004<br/> 
2|SYMPT0004|Fever|1|1004<br/> 
3|SYMPT0001|Patient Age|1|1104<br/> 
4|SYMPT0010|Fatigue|1|1104<br/> 
5|SYMPT0005|Nausea|1|1004<br/> 
6|SYMPT0012|Headache|1|1004<br/> 
7|SYMPT0012|Headache|1|1104<br/> 
8|SYMPT0111|MedStop Form|0|1104<br/> 
9|SYMPT1023|SportHealth Test|0|1004<br/> 
10|SYMPT0070|Rash|1|1004<br/> 
11|SYMPT0070|Rash|1|1104<br/> 
12|SYMPT0310|MedStop Screen|0|1104<br/> 

### Why 2 tables used -  For the benifits of Normalization, SQLAlchemy Best Practices, Scalability ,One-to-Many Relationship,Reducing Redundancy

# ---- Final Deliverables : Populated DB & 2 working API's Achieved ----
