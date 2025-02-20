from langgraph import StateGraph, Node

def print_hello():
    print("Hello, World!")

# Create a StateGraph object
workflow = StateGraph()

# Add a single node called "print_node" with the print_hello function
workflow.add_node("print_node", print_hello) 

# Set the entry point of the graph to "print_node"
workflow.set_entry_point("print_node")

# Compile the graph
app = workflow.compile()

# Run the graph (this will execute the "print_hello" function)
app.run() 