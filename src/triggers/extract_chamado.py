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
            
            query = "select * from itsm.chamado"

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
                    cursor_tgt.execute("SET IDENTITY_INSERT itsm.chamado ON")
                    
                    # A tabela chamado tem 19 colunas
                    query_merge = """
                        MERGE INTO itsm.chamado AS Target
                        USING (VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)) 
                            AS Source (id_chamado, nr_chamado, ds_tipo_chamado, ds_status_chamado, ds_prioridade, dt_criacao, dt_resolucao, dt_ultima_atualizacao, id_analista_atual, id_reporter, id_categoria, id_cliente_organizacao, id_fila_atual, ds_titulo, ds_descricao, dt_inclusao, dt_atualizacao, nm_sistema_origem, cd_registro_origem)
                        ON Target.id_chamado = Source.id_chamado
                        WHEN MATCHED THEN
                            UPDATE SET 
                                nr_chamado = Source.nr_chamado,
                                ds_tipo_chamado = Source.ds_tipo_chamado,
                                ds_status_chamado = Source.ds_status_chamado,
                                ds_prioridade = Source.ds_prioridade,
                                dt_criacao = Source.dt_criacao,
                                dt_resolucao = Source.dt_resolucao,
                                dt_ultima_atualizacao = Source.dt_ultima_atualizacao,
                                id_analista_atual = Source.id_analista_atual,
                                id_reporter = Source.id_reporter,
                                id_categoria = Source.id_categoria,
                                id_cliente_organizacao = Source.id_cliente_organizacao,
                                id_fila_atual = Source.id_fila_atual,
                                ds_titulo = Source.ds_titulo,
                                ds_descricao = Source.ds_descricao,
                                dt_inclusao = Source.dt_inclusao,
                                dt_atualizacao = Source.dt_atualizacao,
                                nm_sistema_origem = Source.nm_sistema_origem,
                                cd_registro_origem = Source.cd_registro_origem
                        WHEN NOT MATCHED BY TARGET THEN
                            INSERT (id_chamado, nr_chamado, ds_tipo_chamado, ds_status_chamado, ds_prioridade, dt_criacao, dt_resolucao, dt_ultima_atualizacao, id_analista_atual, id_reporter, id_categoria, id_cliente_organizacao, id_fila_atual, ds_titulo, ds_descricao, dt_inclusao, dt_atualizacao, nm_sistema_origem, cd_registro_origem) 
                            VALUES (Source.id_chamado, Source.nr_chamado, Source.ds_tipo_chamado, Source.ds_status_chamado, Source.ds_prioridade, Source.dt_criacao, Source.dt_resolucao, Source.dt_ultima_atualizacao, Source.id_analista_atual, Source.id_reporter, Source.id_categoria, Source.id_cliente_organizacao, Source.id_fila_atual, Source.ds_titulo, Source.ds_descricao, Source.dt_inclusao, Source.dt_atualizacao, Source.nm_sistema_origem, Source.cd_registro_origem);
                    """
                    
                    # Inserção linha a linha
                    cursor_tgt.executemany(query_merge, [tuple(row) for row in rows])
                    
                    # Desabilita a inserção manual (Boas práticas de segurança)
                    cursor_tgt.execute("SET IDENTITY_INSERT itsm.chamado OFF")
                    
                    # Salva as alterações
                    conn_tgt.commit()
                    logging.info("Tabela chamado copiada com sucesso para o banco de destino!")                     

    except Exception as e:
        logging.error(f"Erro ao ler itsm.chamado: {str(e)}")
        raise