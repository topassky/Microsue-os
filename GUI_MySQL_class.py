import mysql.connector
import GuiDBConfig as guiConf 



class MySQL():
    # class attribute
    GUIDB  = 'GuiDB'   
     
    #------------------------------------------------------
    def connect(self):
        # connect by unpacking dictionary credentials
        conn = mysql.connector.connect(**guiConf.dbConfig)
    
        # create cursor 
        cursor = conn.cursor()    
            
        return conn, cursor
    
    #------------------------------------------------------    
    def close(self, cursor, conn):        
        # close cursor
        cursor.close()
                
        # close connection to MySQL
        conn.close()    

    #------------------------------------------------------
    def createDB(self,db_name):
        # connect to MySQL
        conn, cursor = self.connect()
        
        try:
            cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(db_name))
        except mysql.connector.Error as err:
            print("Failed to create DB: {}".format(err))        

        # close cursor and connection
        self.close(cursor, conn)

    def addAddress(self, customer_id):
        
        # connect to MySQL
        conn, cursor = self.connect()        
        
        # insert data
        cursor.execute("INSERT INTO parpadeos (id,alarma) VALUES ({},{})".format("null",customer_id))
                 
        # commit transaction
        conn.commit ()
        
        # close cursor and connection
        self.close(cursor, conn)

                      

    #------------------------------------------------------
    def dropTables(self):
        # connect to MySQL
        conn, cursor = self.connect()
    
        cursor.execute("DROP TABLE quotations")   
    
        # close cursor and connection
        self.close(cursor, conn)    

   
            
    #------------------------------------------------------        
    def insertdata(self, alarma):
        # connect to MySQL
        conn, cursor = self.connect()
       
        
        # insert data
        cursor.execute("INSERT INTO parpadeos (id,alarma) VALUES ({},{})".format("null",alarma))
                 
        # commit transaction
        conn.commit ()

        # close cursor and connection
        self.close(cursor, conn)
        

        
    #------------------------------------------------------        
    def ConsultData(self):
        # connect to MySQL
        conn, cursor = self.connect()   
            
        # execute command
        cursor.execute("select * from parpadeos order by id desc limit 1;")
        respuesta = cursor.fetchall()

        # close cursor and connection
        self.close(cursor, conn) 

        return respuesta
