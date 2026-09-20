# database_utils.py
import logging
import os
import pyodbc 

# Assinatura da função execute_sync_template para ser usada em outros módulos
def execute_sync_template(table_name: str, pk_column: str, columns: list) -> None:
    # Template Method para extrair dados da origem e fazer o MERGE no destino.
    logging.info(f'Iniciando processamento da tabela {table_name}')  

    # Monta a string de conexão para o banco de dados de origuem
    sql_server = os.getenv("SQL_SERVER_SOURCE")
    sql_database = os.getenv("SQL_DATABASE_SOURCE")
    sql_user = os.getenv("SQL_USER_SOURCE")
    sql_pass = os.getenv("SQL_PASSWORD_SOURCE")

    conn_str_src = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={sql_server};"
        f"DATABASE={sql_database};"
        f"UID={sql_user};"
        f"PWD={sql_pass};"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
        "Connection Timeout=30;"
    )

    # Monta a string de conexão para o banco de dados de destino
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

    # Executa a extração de dados das tabelas de origem e faz um MERGE no banco de dados de destino
    try:
        with pyodbc.connect(conn_str_src) as conn:
            cursor = conn.cursor()
            query_select = f"SELECT * FROM {table_name}"
            cursor.execute(query_select)
            rows = cursor.fetchall()
            
            logging.info(f"{len(rows)} linhas lidas de {table_name}")    

        if rows:
            placeholders = ", ".join(["?"] * len(columns))
            cols_joined = ", ".join(columns)
            source_cols_joined = ", ".join([f"Source.{c}" for c in columns])
            
            update_set = ",\n".join([f"{c} = Source.{c}" for c in columns if c != pk_column])
            
            query_merge = f"""
                MERGE INTO {table_name} AS Target
                USING (VALUES ({placeholders})) 
                    AS Source ({cols_joined})
                ON Target.{pk_column} = Source.{pk_column}
                WHEN MATCHED THEN
                    UPDATE SET 
                        {update_set}
                WHEN NOT MATCHED BY TARGET THEN
                    INSERT ({cols_joined})
                    VALUES ({source_cols_joined});
            """

            with pyodbc.connect(conn_str_tgt) as conn_tgt:
                cursor_tgt = conn_tgt.cursor()
                cursor_tgt.execute(f"SET IDENTITY_INSERT {table_name} ON")
                cursor_tgt.executemany(query_merge, [tuple(row) for row in rows])
                cursor_tgt.execute(f"SET IDENTITY_INSERT {table_name} OFF")
                conn_tgt.commit()
                
                logging.info(f"Tabela {table_name} copiada com sucesso!")       

    except Exception as e:
        logging.error(f"Erro ao processar {table_name}: {str(e)}")
        raise