import logging
import azure.functions as func
import os
import pyodbc 

app = func.Blueprint()
 

@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_analista(myTimer: func.TimerRequest) -> None:
    logging.info('tabela analista')  


    sql_server = os.getenv("SQL_SERVER_SOURCE")
    sql_database = os.getenv("SQL_DATABASE_SOURCE")
    sql_user = os.getenv("SQL_USER_SOURCE")
    sql_pass = os.getenv("SQL_PASSWORD_SOURCE")

    logging.info(f'Servidor: {sql_server}, Banco: {sql_database} , User: {sql_user}, Senha: {sql_pass}')