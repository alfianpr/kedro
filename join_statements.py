from kedro.pipeline import node

def return_greeting():
    return "hello"

return_greeting_node = node(func=return_greeting, inputs=None, outputs="my_salutation")

def join_statements(greeting):
    return f"{greeting} kedro!"

join_statements_node = node(
    join_statements, inputs="My_salutation", outputs="my_message"
)
