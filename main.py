# CONNECT TO REMOTE DB2
import ibm_db
import conn_settings

print("Database: %s" % conn_settings.database)
print("Hostname: %s" %conn_settings.hostname)
print("Port: %s" % conn_settings.port)
print("Uid: %s" % conn_settings.uid)
print("Pwd: %s" % conn_settings.pwd)

conn = ibm_db.connect(
            f"DATABASE={conn_settings.database};\
            HOSTNAME={conn_settings.hostname};\
            PORT={conn_settings.port};\
            PROTOCOL=TCPIP;\
            UID={conn_settings.uid};\
            PWD={conn_settings.pwd}", "", "")

print(conn)

sql = '''
    SELECT *
    FROM EMPLOYEES
'''

stmt = ibm_db.exec_immediate(conn, sql)
dictionary = ibm_db.fetch_both(stmt)
while(dictionary):
    print(dictionary)
    dictionary = ibm_db.fetch_both(stmt)


# CREATE EXCEL REPORT



# SEND EMAIL NOTIFICATION