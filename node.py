from kedro.pipeline import node

def return_greeting():
    return "hello"

return_greeting_node = node(func=return_greeting, inputs=None, outputs="my_salutation")

print(return_greeting_node)