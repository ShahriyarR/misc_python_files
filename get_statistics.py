import mysql.connector
from termcolor import colored, cprint
from tabulate import tabulate

# MySQL Connection Parameters

cnx = mysql.connector.connect(user='root', password='12345',
                              host='localhost',
                              database='test')
table = cnx.cmd_statistics()

dictlist = []

column1 = colored('General Statistic Information', 'red', attrs=['reverse', 'dark'])
column2 = colored('Values', 'red', attrs=['reverse', 'dark'])

headers = [column1, column2]


for key, value in table.iteritems():
    temp = [colored(key,'green',attrs=['reverse']),value]
    dictlist.append(temp)


print tabulate(dictlist, headers, tablefmt="rst", numalign="right")

print cnx.get_server_info()
#print cnx.get_server_version()
print cnx.get_sql_mode()
print cnx.get_time_zone()
print cnx.get_autocommit()
print cnx.charset
print cnx.collation


cnx.close()