# import things
from flask_table import Table, Col
import pandas as pd

# Declare your table
# Or, equivalently, some dicts
df = pd.read_csv()
items = df.to_html(classes='table dataTable my-0',table_id="dataTable", border='0')
titles=df.columns.values

def getTable():
    #items = df.style.format('<input name= "topic" value="{}" />').render()
    return items
