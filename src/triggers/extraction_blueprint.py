import azure.functions as func
from triggers.database_util import execute_sync_template

app = func.Blueprint()

# Define a função de gatilho para extrair dados da tabela "itsm.analista"
@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False, use_monitor=False) 
def extract_analista(myTimer: func.TimerRequest) -> None:
    columns = [
        "id_analista", "cd_analista", "nm_analista", "ds_email", "ds_nivel", 
        "id_fila_atual", "fl_ativo", "dt_inclusao", "dt_atualizacao", 
        "nm_sistema_origem", "cd_registro_origem"
    ]
    
    # Chama a função execute_sync_template para processar a tabela "itsm.analista"
    execute_sync_template(
        table_name="itsm.analista", 
        pk_column="id_analista", 
        columns=columns
    )

# Define a função de gatilho para extrair dados da tabela "itsm.categoria"
@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False, use_monitor=False) 
def extract_categoria(myTimer: func.TimerRequest) -> None:
    columns = [
        "id_categoria", "cd_categoria", "nm_categoria", "ds_descricao", 
        "fl_ativo", "dt_inclusao", "dt_atualizacao", 
        "nm_sistema_origem", "cd_registro_origem"
    ]
    
    # Chama a função execute_sync_template para processar a tabela "itsm.categoria"
    execute_sync_template(
        table_name="itsm.categoria", 
        pk_column="id_categoria", 
        columns=columns
    )


# Define a função de gatilho para extrair dados da tabela "itsm.chamado_sla"
@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False, use_monitor=False)
def extract_chamado_sla(myTimer: func.TimerRequest) -> None:
    columns = [
        "id_chamado_sla", "id_chamado", "id_sla", "fl_breach",
        "qt_tempo_restante_minutos", "qt_tempo_decorrido_minutos",
        "qt_meta_minutos", "dt_referencia", "dt_inclusao", "dt_atualizacao",
        "nm_sistema_origem", "cd_registro_origem"
    ]

    # Chama a função execute_sync_template para processar a tabela "itsm.chamado_sla"
    execute_sync_template(
        table_name="itsm.chamado_sla",
        pk_column="id_chamado_sla",
        columns=columns
    )


# Define a função de gatilho para extrair dados da tabela "itsm.chamado_status_historico"
@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False, use_monitor=False)
def extract_chamado_status_historico(myTimer: func.TimerRequest) -> None:
    columns = [
        "id_chamado_status_historico", "id_chamado", "ds_status_chamado",
        "dt_inicio_status", "dt_fim_status", "qt_tempo_status_minutos",
        "id_analista_responsavel", "id_fila", "dt_inclusao", "dt_atualizacao",
        "nm_sistema_origem", "cd_registro_origem"
    ]

    # Chama a função execute_sync_template para processar a tabela "itsm.chamado_status_historico"
    execute_sync_template(
        table_name="itsm.chamado_status_historico",
        pk_column="id_chamado_status_historico",
        columns=columns
    )


# Define a função de gatilho para extrair dados da tabela "itsm.chamado"
@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False, use_monitor=False)
def extract_chamado(myTimer: func.TimerRequest) -> None:
    columns = [
        "id_chamado", "nr_chamado", "ds_tipo_chamado", "ds_status_chamado",
        "ds_prioridade", "dt_criacao", "dt_resolucao", "dt_ultima_atualizacao",
        "id_analista_atual", "id_reporter", "id_categoria", "id_cliente_organizacao",
        "id_fila_atual", "ds_titulo", "ds_descricao", "dt_inclusao",
        "dt_atualizacao", "nm_sistema_origem", "cd_registro_origem"
    ]

    # Chama a função execute_sync_template para processar a tabela "itsm.chamado"
    execute_sync_template(
        table_name="itsm.chamado",
        pk_column="id_chamado",
        columns=columns
    )


# Define a função de gatilho para extrair dados da tabela "itsm.cliente_organizacao"
@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False, use_monitor=False)
def extract_cliente_organizacao(myTimer: func.TimerRequest) -> None:
    columns = [
        "id_cliente_organizacao", "cd_cliente_organizacao",
        "nm_cliente_organizacao", "nr_cnpj", "fl_ativo", "dt_inclusao",
        "dt_atualizacao", "nm_sistema_origem", "cd_registro_origem"
    ]

    # Chama a função execute_sync_template para processar a tabela "itsm.cliente_organizacao"
    execute_sync_template(
        table_name="itsm.cliente_organizacao",
        pk_column="id_cliente_organizacao",
        columns=columns
    )


# Define a função de gatilho para extrair dados da tabela "itsm.csat_avaliacao"
@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False, use_monitor=False)
def extract_csat_avaliacao(myTimer: func.TimerRequest) -> None:
    columns = [
        "id_csat_avaliacao", "id_chamado", "id_analista", "nr_score",
        "ds_comentario", "dt_avaliacao", "dt_inclusao", "dt_atualizacao",
        "nm_sistema_origem", "cd_registro_origem"
    ]

    # Chama a função execute_sync_template para processar a tabela "itsm.csat_avaliacao"
    execute_sync_template(
        table_name="itsm.csat_avaliacao",
        pk_column="id_csat_avaliacao",
        columns=columns
    )


# Define a função de gatilho para extrair dados da tabela "itsm.fila"
@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False, use_monitor=False)
def extract_fila(myTimer: func.TimerRequest) -> None:
    columns = [
        "id_fila", "cd_fila", "nm_fila", "ds_descricao", "fl_ativo",
        "dt_inclusao", "dt_atualizacao", "nm_sistema_origem", "cd_registro_origem"
    ]

    # Chama a função execute_sync_template para processar a tabela "itsm.fila"
    execute_sync_template(
        table_name="itsm.fila",
        pk_column="id_fila",
        columns=columns
    )


# Define a função de gatilho para extrair dados da tabela "itsm.sla"
@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False, use_monitor=False)
def extract_sla(myTimer: func.TimerRequest) -> None:
    columns = [
        "id_sla", "cd_sla", "nm_sla", "qt_meta_minutos", "ds_descricao",
        "fl_ativo", "dt_inclusao", "dt_atualizacao", "nm_sistema_origem",
        "cd_registro_origem"
    ]

    # Chama a função execute_sync_template para processar a tabela "itsm.sla"
    execute_sync_template(
        table_name="itsm.sla",
        pk_column="id_sla",
        columns=columns
    )


# Define a função de gatilho para extrair dados da tabela "itsm.solicitante"
@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False, use_monitor=False)
def extract_solicitante(myTimer: func.TimerRequest) -> None:
    columns = [
        "id_solicitante", "cd_solicitante", "id_cliente_organizacao",
        "nm_solicitante", "ds_email", "ds_telefone", "fl_ativo", "dt_inclusao",
        "dt_atualizacao", "nm_sistema_origem", "cd_registro_origem"
    ]

    # Chama a função execute_sync_template para processar a tabela "itsm.solicitante"
    execute_sync_template(
        table_name="itsm.solicitante",
        pk_column="id_solicitante",
        columns=columns
    )