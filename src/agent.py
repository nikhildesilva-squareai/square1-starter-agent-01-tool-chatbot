"""ToolAgent: an LLM agent that decides when to call tools and integrates results."""

from anthropic import Anthropic


class ToolAgent:
    """Conversational agent that uses Claude with tool-use to answer questions.

    The agent maintains a conversation history, sends messages to Claude with
    tool definitions, and handles the tool-use loop (call tool -> feed result
    back -> get final answer).
    """

    def __init__(self, client: Anthropic | None = None, model: str = "claude-sonnet-4-20250514"):
        """Initialise the agent with an Anthropic client and model.

        Args:
            client: An Anthropic client instance. If None, create one from env.
            model: The Claude model to use.
        """
        raise NotImplementedError("TODO: implement agent initialisation (store client, model, conversation history)")

    def run(self, user_message: str) -> str:
        """Process a user message and return the agent's text response.

        This method should:
        1. Add the user message to conversation history.
        2. Call Claude with the current history and tool definitions.
        3. If Claude requests tool use, execute the tool and feed the result back.
        4. Repeat until Claude produces a final text response.
        5. Return the final text response.

        Args:
            user_message: The user's input text.

        Returns:
            The agent's final text response after any tool calls.
        """
        raise NotImplementedError("TODO: implement the tool-use agent loop")
