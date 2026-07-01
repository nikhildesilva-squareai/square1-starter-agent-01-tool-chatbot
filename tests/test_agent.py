"""Contract tests for the Tool-Using Chatbot.

These tests verify the public interface of each module.
They are expected to FAIL against the stubs and PASS once implemented.
"""

import pytest
from src.tools import define_tools, execute_tool
from src.agent import ToolAgent


class TestDefineTools:
    """Tool schemas must be valid Anthropic tool-use format."""

    def test_tool_schema_validity(self):
        """define_tools() returns a list of dicts each with name, description, input_schema."""
        tools = define_tools()
        assert isinstance(tools, list) and len(tools) >= 3
        for tool in tools:
            assert "name" in tool
            assert "description" in tool
            assert "input_schema" in tool
            assert tool["input_schema"].get("type") == "object"


class TestExecuteTool:
    """Tool execution must return a string result."""

    def test_tool_execution_returns_result(self):
        """execute_tool('calculator', ...) returns a string with the computed answer."""
        result = execute_tool("calculator", {"expression": "2 + 2"})
        assert isinstance(result, str)
        assert "4" in result


class TestToolAgent:
    """The agent must accept a user message and return a text response."""

    def test_agent_processes_user_message(self):
        """ToolAgent.run() returns a non-empty string for a simple question."""
        agent = ToolAgent()
        response = agent.run("What is 2 + 2?")
        assert isinstance(response, str) and len(response) > 0
