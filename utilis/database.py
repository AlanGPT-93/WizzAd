"""
Concerned with storing and retrieving books from a list. 
"""

from .context_manager import DataConnection 

location_db = "C:/Users/Alan.Garcia/OneDrive - OneWorkplace/Documentos/Python/projects/wizzad_data/creatives.db"

## Función que crea una tabla según la query propuesta
def create_table(query):
    with DataConnection(location_db) as connection:
        cursor = connection.cursor()
        cursor.execute(query)


## Ayuda a obtener datos de una tabla según la query propuesta
def get_data(query):
    with DataConnection(location_db) as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
    return data


## Ayuda a almacenar nuevos datos en una tabla según la query propuesta
def add_data(query, data_tab):
    with DataConnection(location_db) as connection:
        cursor = connection.cursor()
        for r in data_tab.values:
            #print(r)
            cursor.execute(query, tuple(r) )


## Ayuda a realizar UPDATE en datos de una tabla según la query propuesta
def update_data_tablas_amort(query, data_tab_amort):
    with DataConnection(location_db) as connection:
        cursor = connection.cursor()
        for r in data_tab_amort:
            #print(r)
            cursor.execute(query, (r,) )