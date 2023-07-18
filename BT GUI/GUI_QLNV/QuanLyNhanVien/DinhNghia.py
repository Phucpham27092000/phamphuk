import mysql.connector
def getConnection():
    connection = mysql.connector.connect(host = 'localhost', 
                                         user = 'root', 
                                         passwd = '27092000', 
                                         database = 'Quanlynhanvien', 
                                         auth_plugin='mysql_native_password'
                                         )
    return connection