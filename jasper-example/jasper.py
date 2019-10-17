# -*- coding: utf-8 -*-
import os
from platform import python_version
from pyreportjasper import JasperPy

def advanced_example_using_database():
    input_file = os.path.dirname(os.path.abspath(__file__)) + \
                 '/examples/hello_world.jrxml'
    output = os.path.dirname(os.path.abspath(__file__)) + '/output/examples'
    con = {
        'driver': 'postgres',
        'username': 'DB_USERNAME',
        'password': 'DB_PASSWORD',
        'host': 'DB_HOST',
        'database': 'DB_DATABASE',
        'schema': 'DB_SCHEMA',
        'port': '5432'
    }
    jasper = JasperPy()
    jasper.process(
        input_file,
        output_file=output,
        format_list=["pdf", "rtf", "xml"],
        parameters={'python_version': python_version()},
        db_connection=con,
        locale='pt_BR'  # LOCALE Ex.:(en_US, de_GE)
