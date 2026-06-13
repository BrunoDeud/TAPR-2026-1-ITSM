import logging
import azure.functions as func
import os
import pyodbc

app = func.Blueprint()

@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_chamado_status_historico(myTimer: func.TimerRequest) -> None:
    logging.info('tabela chamado_status_historico') 

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
            
            query = "select * from itsm.chamado_status_historico"

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
                    
                    # Permite inserir dados em colunas IDENTITY (IDs manuais)
                    cursor_tgt.execute("SET IDENTITY_INSERT itsm.chamado_status_historico ON")
                    
                    # A tabela chamado_status_historico tem 12 colunas
                    query_merge = """
                        MERGE INTO itsm.chamado_status_historico AS Target
                        USING (VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)) 
                            AS Source (id_chamado_status_historico, id_chamado, ds_status_chamado, dt_inicio_status, dt_fim_status, qt_tempo_status_minutos, id_analista_responsavel, id_fila, dt_inclusao, dt_atualizacao, nm_sistema_origem, cd_registro_origem) 
                        ON Target.id_chamado_status_historico = Source.id_chamado_status_historico
                        WHEN MATCHED THEN
                            UPDATE SET 
                                id_chamado = Source.id_chamado,
                                ds_status_chamado = Source.ds_status_chamado,
                                dt_inicio_status = Source.dt_inicio_status,
                                dt_fim_status = Source.dt_fim_status,
                                qt_tempo_status_minutos = Source.qt_tempo_status_minutos,
                                id_analista_responsavel = Source.id_analista_responsavel,
                                id_fila = Source.id_fila,
                                dt_inclusao = Source.dt_inclusao,
                                dt_atualizacao = Source.dt_atualizacao,
                                nm_sistema_origem = Source.nm_sistema_origem,
                                cd_registro_origem = Source.cd_registro_origem
                        WHEN NOT MATCHED BY TARGET THEN
                            INSERT (id_chamado_status_historico, id_chamado, ds_status_chamado, dt_inicio_status, dt_fim_status, qt_tempo_status_minutos, id_analista_responsavel, id_fila, dt_inclusao, dt_atualizacao, nm_sistema_origem, cd_registro_origem) 
                            VALUES (Source.id_chamado_status_historico, Source.id_chamado, Source.ds_status_chamado, Source.dt_inicio_status, Source.dt_fim_status, Source.qt_tempo_status_minutos, Source.id_analista_responsavel, Source.id_fila, Source.dt_inclusao, Source.dt_atualizacao, Source.nm_sistema_origem, Source.cd_registro_origem);
                    """
                    
                    # Inserção linha a linha
                    cursor_tgt.executemany(query_merge, [tuple(row) for row in rows])
                    
                    # Desabilita a inserção manual (Boas práticas de segurança)
                    cursor_tgt.execute("SET IDENTITY_INSERT itsm.chamado_status_historico OFF")
                    
                    # Salva as alterações
                    conn_tgt.commit()
                    logging.info("Tabela chamado_status_historico copiada com sucesso para o banco de destino!")          

    except Exception as e:
        logging.error(f"Erro ao ler itsm.chamado_status_historico: {str(e)}")
        raise