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
def extract_sla(myTimer: func.TimerRequest) -> None:
    logging.info('tabela chamado_sla')    
 
@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_sla(myTimer: func.TimerRequest) -> None:
    logging.info('tabela analista')    
   
@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_sla(myTimer: func.TimerRequest) -> None:
    logging.info('tabela categoria')    
 
@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_sla(myTimer: func.TimerRequest) -> None:
    logging.info('tabela chamada_status_historico')    
  
@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_sla(myTimer: func.TimerRequest) -> None:
    logging.info('tabela cliente_organizacao')    
 
@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_sla(myTimer: func.TimerRequest) -> None:
    logging.info('tabela csat_avaliacao')    