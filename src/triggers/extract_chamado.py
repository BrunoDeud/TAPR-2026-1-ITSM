import logging
import os
import azure.functions as func
import pyodbc

app = func.Blueprint()

@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_chamado(myTimer: func.TimerRequest) -> None:
    logging.info('tabela chamado')
    
    sql_server = os.getenv("SQL_SERVER_SOURCE")
    sql_database = os.getenv("SQL_DATABASE_SOURCE")
    sql_user = os.getenv("SQL_USER_SOURCE")
    sql_pass = os.getenv("SQL_PASSWORD_SOURCE")

    logging.info(f'servidor={sql_server}, banco de dados={sql_database}, usuario={sql_user}, senha={sql_pass} ')

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
            
            query = "select top 10 * from itsm.chamado"

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
                    
                    cursor_tgt.execute("DELETE FROM itsm.chamado  ")
                    
                    # Permite inserir dados em colunas IDENTITY (IDs manuais)
                    cursor_tgt.execute("SET IDENTITY_INSERT itsm.chamado   ON")
                    
                    # A tabela chamado   tem 19 colunas
                    query_insert = """
                        INSERT INTO itsm.chamado   
                        (id_chamado, nr_chamado, ds_tipo_chamado, ds_status_chamado, ds_prioridade, dt_criacao, dt_resolucao, dt_ultima_atualizacao, id_analista_atual, id_reporter, id_categoria, id_cliente_organizacao, id_fila_atual, ds_titulo, ds_descricao, dt_inclusao, dt_atualizacao, nm_sistema_origem, cd_registro_origem) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """
                    
                    # Inserção linha a linha
                    for row in rows:
                        cursor_tgt.execute(query_insert, *row)
                    
                    # Desabilita a inserção manual (Boas práticas de segurança)
                    cursor_tgt.execute("SET IDENTITY_INSERT itsm.chamado   OFF")
                    
                    # Salva as alterações
                    conn_tgt.commit()
                    logging.info("Tabela chamado   copiada com sucesso para o banco de destino!")                     

    except Exception as e:
        logging.error(f"Erro ao ler itsm.chamado: {str(e)}")
        raise