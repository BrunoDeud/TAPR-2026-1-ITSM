import logging
import azure.functions as func
import os
import pyodbc

app = func.Blueprint()

@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_fila(myTimer: func.TimerRequest) -> None:
    logging.info('tabela fila')   

    sql_server = os.getenv("SQL_SERVER_SOURCE")
    sql_database = os.getenv("SQL_DATABASE_SOURCE")
    sql_user = os.getenv("SQL_USER_SOURCE")
    sql_pass = os.getenv("SQL_PASSWORD_SOURCE")

    logging.info(f'Servidor: {sql_server}, Banco: {sql_database} , User: {sql_user}, Senha: {sql_pass}')

    # Configura a string de conexão para o banco de dados SQL Server
    conn_str = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={sql_server};"
        f"DATABASE={sql_database};"
        f"UID={sql_user};"
        f"PWD={sql_pass};"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
        "Connection Timeout=30;"
    )

   
    try:
        # Estabelece a conexão com o banco de dados usando pyodbc
        with pyodbc.connect(conn_str) as conn:
            # Cria um cursor para executar a consulta   
            cursor = conn.cursor()
            
            query = "select * from itsm.fila"

            # Executa a consulta SQL
            cursor.execute(query)

            # Busca todos os resultados da consulta
            rows = cursor.fetchall()

            logging.info(rows)  

            # Puxar variáveis do banco de destino 
            sql_server_tgt = os.getenv("SQL_SERVER_TARGET")
            sql_database_tgt = os.getenv("SQL_DATABASE_TARGET")
            sql_user_tgt = os.getenv("SQL_USER_TARGET")
            sql_pass_tgt = os.getenv("SQL_PASSWORD_TARGET")

            conn_str_tgt = (
                "DRIVER={ODBC Driver 18 for SQL Server};"
                f"SERVER={sql_server_tgt};"
                f"DATABASE={sql_database_tgt};"
                f"UID={sql_user_tgt};"  
                f"PWD={sql_pass_tgt};"
                "Encrypt=yes;"
                "TrustServerCertificate=no;"
                "Connection Timeout=30;"
            )

            if rows:
                with pyodbc.connect(conn_str_tgt) as conn_tgt:
                    cursor_tgt = conn_tgt.cursor()
                    
                    cursor_tgt.execute("DELETE FROM itsm.fila")
                    
                    # Permite inserir dados em colunas IDENTITY (IDs manuais)
                    cursor_tgt.execute("SET IDENTITY_INSERT itsm.fila  ON")
                    
                    # A tabela fila  tem 9 colunas
                    query_insert = """
                        INSERT INTO itsm.fila     
                        (id_fila, cd_fila, nm_fila, ds_descricao, fl_ativo, dt_inclusao, dt_atualizacao, nm_sistema_origem, cd_registro_origem) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """
                    
                    # Inserção linha a linha
                    for row in rows:
                        cursor_tgt.execute(query_insert, *row)
                    
                    # Desabilita a inserção manual (Boas práticas de segurança)
                    cursor_tgt.execute("SET IDENTITY_INSERT itsm.fila OFF")
                    
                    # Salva as alterações
                    conn_tgt.commit()
                    logging.info("Tabela fila copiada com sucesso para o banco de destino!")            

    except Exception as e:
        logging.error(f"Erro ao ler itsm.fila: {str(e)}")
        raise