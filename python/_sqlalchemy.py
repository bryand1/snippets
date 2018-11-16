from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()

engine = create_engine('mysql+mysqldb://root:pass@23.92.23.113/mydb')
