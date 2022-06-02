from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from sqlmodel import Field, Session, SQLModel, create_engine, select
from typing import Optional
import sqlite3
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
origins = [
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Resultrow(BaseModel):
    id: Optional[str]
    tigan: str
    tixing: Optional[str]
    xuanxiang1: Optional[str]
    xuanxiang2: Optional[str]
    xuanxiang3: Optional[str]
    xuanxiang4: Optional[str]
    xuanxiang5: Optional[str]
    xuanxiang6: Optional[str]
    xuanxiang7: Optional[str]
    jiexi: Optional[str]
    daan: str
    defen: int


@app.get("/", response_model=Resultrow)
async def root(timuhao:int):
    conn = sqlite3.connect('CGS.db')
    c = conn.cursor()
    if(timuhao==1):
        sqlcontent = "delete from ks_temp"
        c.execute(sqlcontent)
        print(sqlcontent)
        conn.commit()
    if(timuhao>=1 and  timuhao<=5):
        sqlcontent = "SELECT * FROM cgsall WHERE tixing='基础选择题'  and id not in(select timuhao from ks_temp)ORDER BY RANDOM() LIMIT 1"
    elif(timuhao>=6 and timuhao<=10):
        sqlcontent = "SELECT * FROM cgsall WHERE tixing='基础判断题' and id not in(select timuhao from ks_temp) ORDER BY RANDOM() LIMIT 1"
    elif(timuhao>=11 and timuhao<=15):
        sqlcontent = "SELECT * FROM cgsall WHERE tixing='驾驶证选择题'  and id not in(select timuhao from ks_temp) ORDER BY RANDOM() LIMIT 1"
    elif(timuhao>=16 and timuhao<=20):
        sqlcontent = "SELECT * FROM cgsall WHERE tixing='驾驶证判断题'  and id not in(select timuhao from ks_temp) ORDER BY RANDOM() LIMIT 1"
    elif(timuhao>=21 and timuhao<=25):
        sqlcontent = "SELECT * FROM cgsall WHERE tixing='机动车选择题'  and id not in(select timuhao from ks_temp) ORDER BY RANDOM() LIMIT 1"
    elif(timuhao>=26 and timuhao<=30):
        sqlcontent = "SELECT * FROM cgsall WHERE tixing='机动车判断题' and id not in(select timuhao from ks_temp) ORDER BY RANDOM() LIMIT 1"
    elif(timuhao>=31 and timuhao<=65):
        sqlcontent = "SELECT * FROM cgsall WHERE tixing='监管选择题' and id not in(select timuhao from ks_temp) ORDER BY RANDOM() LIMIT 1"
    elif(timuhao>=66 and timuhao<=100):
        sqlcontent = "SELECT * FROM cgsall WHERE tixing='监管判断题' and id not in(select timuhao from ks_temp) ORDER BY RANDOM() LIMIT 1"
    print(sqlcontent)
    cursor = c.execute(sqlcontent)
    for row in cursor:
        Resultrow = {"id": row[0], "tigan": row[1], "tixing": row[2], "xuanxiang1": row[3], "xuanxiang2": row[4],
                     "xuanxiang3": row[5], "xuanxiang4": row[6], "xuanxiang5": row[7], "xuanxiang6": row[8],
                     "xuanxiang7": row[9], "jiexi": row[10], "daan": row[11], "defen": row[12]}
    sqlcontent="insert into ks_temp values ("+str(Resultrow['id'])+")"
    c.execute(sqlcontent)
    print(sqlcontent)
    conn.commit()
    conn.close()
    return Resultrow


if __name__ == '__main__':
    uvicorn.run("backend:app", host="0.0.0.0", port=8000, reload=True, log_level="info")
