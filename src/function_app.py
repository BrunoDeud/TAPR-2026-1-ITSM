import logging
import azure.functions as func

app = func.FunctionApp()

from triggers.function_app import app as extraction_blueprint

app.register_functions(extraction_blueprint)