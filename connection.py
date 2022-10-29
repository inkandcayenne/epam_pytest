# from sqlalchemy import create_engine
# from sqlalchemy import select
#
# engine = create_engine("mssql+pyodbc://DSN=EPGETBIW0395?driver=ODBC+Driver+18+for+SQL+Server?Trusted_Connection=yes")
# conn = engine.connect()
# s = select(['countries'])
# result = conn.execute(s)

#
import pytest
! pytest
#
# import pyodbc
# import pytest
# from datetime import date
#
#
# conn = pyodbc.connect(
#     'DSN=EPGETBIW0395;UID=testuser;PWD=TestPassword!;Trusted_Connection=yes;TrustServerCertificate'
#     '=yes;DATABASE=TRN')
# cursor = conn.cursor()
# cursor.execute("""
#                            select postal_code
#                              from hr.locations
#                             """)
# rows = cursor.fetchall()
# for row in rows:
#     print(row.postal_code is None)
#
# print(rows)