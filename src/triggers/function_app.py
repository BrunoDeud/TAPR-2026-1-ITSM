import azure.functions as func
from database_utils import execute_sync_template 

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