import xlwings as xw
from sqlmodel import Field, Session, SQLModel, create_engine
from typing import Optional

class cgsall(SQLModel,table=True):  #
    id: Optional[int] = Field(default=None, primary_key=True)
    tigan: str
    tixing: Optional[str]
    xuanxiang1: Optional[str]
    xuanxiang2: Optional[str]
    xuanxiang3:Optional[str]
    xuanxiang4:Optional[str]
    xuanxiang5:Optional[str]
    xuanxiang6:Optional[str]
    xuanxiang7:Optional[str]
    jiexi:Optional[str]
    daan:str
    defen:int

def main():
    engine = create_engine("sqlite:///CGS.db", echo=True)

    SQLModel.metadata.create_all(engine)

    app = xw.App(visible=True, add_book=False)
    wb = app.books.open('cgs2022.xls')
    sht = wb.sheets['cgs2022']
    with Session(engine) as session:
        for i in range(5, 2637,1):
            dataline=sht.range('A'+str(i)+':L'+str(i)).value
            datarowtowrite = cgsall(tigan=dataline[0], tixing=dataline[1], xuanxiang1=dataline[2], xuanxiang2=dataline[3],
                                    xuanxiang3=dataline[4], xuanxiang4=dataline[5], xuanxiang5=dataline[6],
                                    xuanxiang6=dataline[7], xuanxiang7=dataline[8], jiexi=dataline[9],
                                    daan=dataline[10], defen=dataline[11])

            session.add(datarowtowrite)
            session.commit()
    wb.close()
    app.quit()




if __name__ == "__main__":
    main()
