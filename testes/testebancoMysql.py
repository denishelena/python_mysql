import MySQLdb


con = MySQLdb.Connect(db="teste",user="root",password="root",host="127.0.0.1")
cur = con.cursor()


#create table
sql = "create table pessoa"\
    "(pescodigo integer primary key,"\
    "pesnome varchar(40),"\
    "pesmail varchar(50))"

#cur.execute(sql)




sql = "insert into pessoa values (1, 'denis', 'denis@gmail.com')"
cur.execute(sql)
con.commit()


sql = "select * from pessoa"
cur.execute(sql)
recset = cur.fetchall()

for registros in recset:
    print(registros)


