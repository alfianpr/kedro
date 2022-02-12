#The Runner is an object that runs the pipeline. 
# Kedro resolves the order in which the nodes are executed

from kedro.pipeline import node
from kedro.pipeline import Pipeline
from kedro.io import DataCatalog, MemoryDataSet
from kedro.runner import SequentialRunner

#Node
def return_greeting():
    return "hello"

return_greeting_node = node(func=return_greeting, inputs=None, outputs="my_salutation")

#Join statements
def join_statements(greeting):
    return f"{greeting} kedro!"

join_statements_node = node(
    join_statements, inputs="my_salutation", outputs="my_message"
)

#Assemble nodes into a pipeline
pipeline = Pipeline([return_greeting_node, join_statements_node])

#Prepare a data catalog
data_catalog = DataCatalog({"my_salutation" : MemoryDataSet()})

#Create a runner to run the pipeline
runner = SequentialRunner()

#Run the pipeline
print(runner.run(pipeline, data_catalog))