"""Tool definitions and execution logic for the Tool-Using Chatbot."""


def define_tools() -> list[dict]:
    """Return a list of tool schemas in Anthropic tool-use format.

    Each tool schema should include:
    - name: unique identifier for the tool
    - description: what the tool does
    - input_schema: JSON Schema describing the tool's parameters

    Implement at least three tools: calculator, weather lookup, and web search.
    """
    raise NotImplementedError("TODO: implement tool schema definitions")


def execute_tool(tool_name: str, tool_input: dict) -> str:
    """Execute a tool by name with the given input and return the result as a string.

    Args:
        tool_name: The name of the tool to execute (must match a defined tool).
        tool_input: A dictionary of input parameters matching the tool's input_schema.

    Returns:
        A string containing the tool's output.

    Raises:
        ValueError: If the tool_name is not recognised.
    """
    raise NotImplementedError("TODO: implement tool execution dispatcher")
