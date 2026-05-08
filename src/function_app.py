import logging
import azure.functions as func

app = func.FunctionApp()            

from triggers.extract_analista import app as analista
from triggers.extract_categoria import app as categoria
from triggers.extract_chamada_status_historico import app as chamada_status_historico
from triggers.extract_chamado_sla import app as chamado_sla
from triggers.extract_chamado import app as chamado
from triggers.extract_cliente_organizacao import app as cliente_organizacao
from triggers.extract_csat_avaliacao import app as csat_avaliacao
from triggers.extract_fila import app as fila
from triggers.extract_sla import app as sla
from triggers.extract_solicitante import app as solicitante


app.register_function(chamado)
app.register_function(analista)
app.register_function(solicitante)
app.register_function(categoria)
app.register_function(chamado_sla)
app.register_function(cliente_organizacao)
app.register_function(csat_avaliacao)
app.register_function(fila)
app.register_function(sla)
app.register_function(chamada_status_historico)

