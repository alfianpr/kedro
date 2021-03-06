#A DataCatalog is a Kedro concept.
# It is the registry of all data sources that the project can use.
# It maps the names of node inputs and outputs as keys in a DataSet, 
# which is a Kedro class that can be specialised for different types of data storage. 

from kedro.pipeline import node
from kedro.pipeline import Pipeline
from kedro.io import DataCatalog, MemoryDataSet

#Node
def return_greeting():
    return "hello"

return_greeting_node = node(func=return_greeting, inputs=None, outputs="my_salutation")

#Join statements
def join_statements(greeting):
    return f"{greeting} kedro!"

join_statements_node = node(
    join_statements, inputs="My_salutation", outputs="my_message"
)

#Assemble nodes into a pipeline
pipeline = Pipeline([return_greeting_node, join_statements_node])

#Prepare a data catalog
data_catalog = DataCatalog({"my_salutation" : MemoryDataSet})

