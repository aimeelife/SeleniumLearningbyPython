#encoding=utf-8
import pyodbc

class DatabaseInit(object):
    def __init__(self,driverName,ServerName,dbName,userName,password):
        self.driver=driverName
        self.Server=ServerName
        self.Database=dbName
        self.uid=userName
        self.pwd=password


    def insertDatas(self):
        try:
            conn=pyodbc.connect(
            driver=self.driver,
            Server=self.Server,
            Database=self.Database,
            uid=self.uid,
            pwd=self.pwd
            )
            cur=conn.cursor()
            sql="insert into test([index],search,expect) values (?,?,?);"
            print ('Inserting a new row into table')
            with cur.execute(sql,'4','test1','test1'):
                print "Index4 record successfuly inserted!"

            # Delete Query
            print ('Deleting index record 4')
            tsql = "DELETE FROM test WHERE [index] = ?"
            with cur.execute(tsql, '4'):
                print ('Successfuly Deleted!')

        except pyodbc.Error,e:
            raise e
        else:
            #conn.commit()
            cur.execute("select * from test;")
            for i in cur.fetchall():
                print i[0],i[1],i[2]
            cur.close()
            conn.close()

if __name__=='__main__':
    db=DatabaseInit(driverName='{SQL Server}',
                    ServerName='localhost',
                    dbName='testdb',
                    userName='Python',
                    password='qa')
    db.insertDatas()
    print "Init finished"



