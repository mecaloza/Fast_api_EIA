
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
from pydantic import BaseModel



app = FastAPI()

class Dot_current(BaseModel):
  value:float
  units:str
  devices_id:int

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/get_dots/{item_id}")
async def read_item(item_id):
    try:
      mydb=mysql.connector.connect(host="dbadmin.c2xacwacu1dj.us-west-2.rds.amazonaws.com", user="admin",password="Admineia*",database="DBEIA")

      mycursor=mydb.cursor(buffered=True,dictionary=True)
      mycursor.execute("SELECT * FROM DBEIA.eia_api_dots WHERE devices_id=1")
      # myresult=mycursor.fetchall()
      content={}
      list_dots=mycursor.fetchall()
      mycursor.execute("SELECT * FROM DBEIA.eia_api_dots WHERE devices_id=2")

      list_dots_2=mycursor.fetchall()


      row_1=[]
      cont_1=0
      for i in list_dots:
        print("asd",i["value"])
        dict_1={}
        dict_1["id"]=cont_1
        dict_1["value"]=i["value"]
        row_1.append(dict_1)
        cont_1=cont_1+1
      row_2=[]
      cont_2=0
      for y in list_dots_2:
        dict_1={}
        dict_1["id"]=cont_2
        dict_1["value"]=y["value"]
        row_2.append(dict_1)
        cont_2=cont_2+1

      content["list_1"]=row_1
      content["list_2"]=row_2
      print("asdas",content)
      return {"data":content}
    except Exception as e:
      print("error",e)
      return False


@app.get("/create_machine/")
async def create_machine():
    try:
      mydb=mysql.connector.connect(host="dbadmin.c2xacwacu1dj.us-west-2.rds.amazonaws.com", user="admin",password="Admineia*",database="DBEIA")
      mycursor=mydb.cursor(buffered=True,dictionary=True)
      mycursor.execute("SELECT * FROM DBEIA.eia_api_machines ")
      myresult=mycursor.fetchall()
      return {"result": myresult}
    except Exception as e:
      print("error",e)
      return False




@app.post("/create_current_dot/")
async def create_current_dot(dot:Dot_current):
    try:
      mydb=mysql.connector.connect(host="dbadmin.c2xacwacu1dj.us-west-2.rds.amazonaws.com", user="admin",password="Admineia*",database="DBEIA")

      mycursor=mydb.cursor(buffered=True,dictionary=True)   
      mycursor.execute("INSERT INTO DBEIA.eia_api_dots (value,units,devices_id) VALUES (%s,%s,%s)",(dot.value,dot.units,dot.devices_id))
      mydb.commit()
      return{"dot":dot}
    
    except Exception as e:
      print("error",e)
      return False

@app.get("/get_dots_app/{item_id}")
async def read_item(item_id):
    try:
      mydb=mysql.connector.connect(host="dbadmin.c2xacwacu1dj.us-west-2.rds.amazonaws.com", user="admin",password="Admineia*",database="DBEIA")

      mycursor=mydb.cursor(buffered=True,dictionary=True)
      mycursor.execute("SELECT * FROM DBEIA.eia_api_dots WHERE devices_id=1")
      # myresult=mycursor.fetchall()
      content={}
      list_dots=mycursor.fetchall()
      mycursor.execute("SELECT * FROM DBEIA.eia_api_dots WHERE devices_id=2")

      list_dots_2=mycursor.fetchall()


      row_1_data=[]
      row_1_dots=[]

      cont_1=0
      for i in list_dots:
        print("asd",i["value"])
        
        row_1_dots.append(cont_1)
        row_1_data.append(i["value"])
        cont_1=cont_1+1
      row_2_data=[]
      row_2_dots=[]
      cont_2=0
      for y in list_dots_2:
      
        row_2_dots.append(cont_2)
        row_2_data.append(y["value"])

        cont_2=cont_2+1

      content["list_1_data"]=row_1_data
      content["list_1_dots"]=row_1_dots
      content["list_2_data"]=row_2_data
      content["list_2_dots"]=row_2_dots
      print("asdas",content)
      return {"data":content}
    except Exception as e:
      print("error",e)
      return False