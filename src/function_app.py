import logging
import azure.functions as func

app = func.FunctionApp()

from src.triggers.extract_analista import app as extract_analista
from src.triggers.extract_categoria import app as extract_categoria
from src.triggers.extract_chamado_sla import app as extract_chamado_sla
from src.triggers.extract_chamada_status_historico import app as extract_chamada_status_historico
from src.triggers.extract_chamado import app as extract_chamado
from src.triggers.extract_cliente_organizacao import app as extract_cliente_organizacao
from src.triggers.extract_csat_avaliacao import app as extract_csat_avaliacao
from src.triggers.extract_fila import app as extract_fila
from src.triggers.extract_sla import app as extract_sla
from src.triggers.extract_solicitante import app as extract_solicitante

app.register_functions(extract_analista)
app.register_functions(extract_categoria)
app.register_functions(extract_chamado_sla)
app.register_functions(extract_chamada_status_historico)
app.register_functions(extract_chamado)
app.register_functions(extract_cliente_organizacao)
app.register_functions(extract_csat_avaliacao)
app.register_functions(extract_fila)
app.register_functions(extract_sla)
app.register_functions(extract_solicitante)