# def ConnectDB():
#     SERVER = os.environ.get('SERVER')
#     USER = os.environ.get('USER')
#     PASSWORD = os.environ.get('PASSWORD')
#     DB = os.environ.get('DB')
#     try:
#         conn = pymssql.connect(server=SERVER, user=USER,
#                                password=PASSWORD, database=DB)
#         log.info("--DB Connected")
#         return conn
#     except pymssql.Error as e:
#         log.error(f"--DB Connection Error - {e}")
#         return returnValue(500, "Something went wrong, Please try again")


# def AccessDBData(conn, query):
#     cursor = conn.cursor(as_dict=True)
#     log.info(f"--Running query - {query}")
#     try:
#         # cursor.execute("")
#         cursor.execute(f"{query};")
#         row = cursor.fetchall()
#         if cursor.rowcount > 0:
#             conn.commit()
#             log.info(f"--Query results - {row}")
#             # row is list of results(json)
#             return row
#         return []
#     except pymssql.OperationalError as e:
#         log.error(f"--DB insertion/update/delete Error - {e}")
#         return False
#     except pymssql.Error as e:
#         log.error(f"--DB insertion/update/delete Error - {e}")
#         cursor.execute("ROLLBACK;")
#         conn.rollback()
#         return False


# autopep8 is important to get rid of additional indentation.
