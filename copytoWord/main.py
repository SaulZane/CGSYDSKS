
# -*- coding: utf-8 -*-

import os
import sqlite3
def pth(fname):
    pth = os.path.dirname(__file__)
    return os.path.join(pth, fname)

from pydocxtpl import DocxWriter

conn = sqlite3.connect('CGS.db')
c = conn.cursor()

sqlcontent = "SELECT * FROM cgsall WHERE tixing='监管判断题'  and daan='错' order by id asc"
print(sqlcontent)
cursor = c.execute(sqlcontent)
result=[]
for row in cursor:
    Resultrow = {"id": row[0], "tigan": row[1], "tixing": row[2], "xuanxiang1": row[3], "xuanxiang2": row[4],
                 "xuanxiang3": row[5], "xuanxiang4": row[6], "xuanxiang5": row[7], "xuanxiang6": row[8],
                 "xuanxiang7": row[9], "jiexi": row[10], "daan": row[11], "defen": row[12]}
    print(Resultrow)
    result.append(Resultrow)
print(result)




payload2={'result': result}
writer = DocxWriter(pth('test.docx'))
writer.render(payload2)
writer.save(pth('test_result.docx'))



