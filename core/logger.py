# -*- coding: utf-8 -*-
"""
Log
"""
from datetime import datetime


def log(termo, file="log_init.txt"):
    """Log."""
    print("Log init ok")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S - %d/%m/%Y")
    with (open(file, "a+")) as arquivo:
        arquivo.write(
            "Termo:" + str(termo) + "- Inicio:" + current_time + "\n"
        )


def log_erro(file="log_error.txt"):
    """Log error."""
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S - %d/%m/%Y")
    with (open(file, "a+")) as arquivo:
        arquivo.write("Erro ocorrido em:" + current_time + "\n")
