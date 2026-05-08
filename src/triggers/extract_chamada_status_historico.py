import logging
import azure.functions as func

app = func.FunctionApp() 
 
@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def extract_chamada_status_historico(myTimer: func.TimerRequest) -> None:
    logging.info('tabela chamada_status_historico') 