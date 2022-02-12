# A pipeline organises the dependencies and execution order
# of a collection of nodes, and connects inputs and outputs 
# while keeping your code modular. 

from kedro.pipeline import node
from kedro.pipeline import Pipeline

def return_greeting():
    return "hello"

return_greeting_node = node(func=return_greeting, inputs=None, outputs="my_salutation")

def join_statements(greeting):
    return f"{greeting} kedro!"

join_statements_node = node(
    join_statements, inputs="My_salutation", outputs="my_message"
)

#Assemble nodes into a pipeline
pipeline = Pipeline([return_greeting_node, join_statements_node])