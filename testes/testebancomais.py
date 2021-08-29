import sqlite3

con = sqlite3.connect("pessoas")
cur = con.cursor()

# insere dados
#sql = "insert into pessoa values (1, 'denis', 'denis@gmail.com')"
#cur.execute(sql)
#con.commit()


sql = "insert into pessoa values (?,?,?)"
dados=[(2,"thisciane","thisci@hot.com"),
       (3,"thiago","thi@hot.com"),
       (4, "marli","psh@gmail.com")]
#for registros in dados:
#    cur.execute(sql,registros)
#con.commit()


#cur.execute("delete from pessoa where pescodigo=2")
cur.execute("delete from pessoa where pesnome like 'denis'")

# recupera dados
sql = "select * from pessoa"
cur.execute(sql)
recset = cur.fetchall()

for registros in recset:
    print(registros)
