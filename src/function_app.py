import logging
import azure.functions as func

app = func.FunctionApp()

@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_chamado(myTimer: func.TimerRequest) -> None:
    logging.info('tabela chamado')

@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_sla(myTimer: func.TimerRequest) -> None:
    logging.info('tabela sla')    

@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_chamado_sla(myTimer: func.TimerRequest) -> None:
    logging.info('tabela chamado_sla')    
 
@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_analista(myTimer: func.TimerRequest) -> None:
    logging.info('tabela analista')    
   
@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_categoria(myTimer: func.TimerRequest) -> None:
    logging.info('tabela categoria')    
 
@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_chamada_status_historico(myTimer: func.TimerRequest) -> None:
    logging.info('tabela chamada_status_historico')    
  
@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_cliente_organizacao(myTimer: func.TimerRequest) -> None:
    logging.info('tabela cliente_organizacao')    
 
@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_csat_avaliacao(myTimer: func.TimerRequest) -> None:
    logging.info('tabela csat_avaliacao')    

@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_fila(myTimer: func.TimerRequest) -> None:
    logging.info('tabela fila')        

@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_solicitante(myTimer: func.TimerRequest) -> None:
    logging.info('tabela solicitante')    