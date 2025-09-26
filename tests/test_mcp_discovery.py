# Test MCP discovery
import asyncio
import os
import pytest
from orchestrator.src.orchestrator.mcp_client import MCPClient

@pytest.mark.asyncio
async def test_content_server_has_tools():
    base = f"http://localhost:{os.environ.get('MCP_CONTENT_PORT','3001')}"
    client = MCPClient(base)
    tools = await client.list_tools()
    assert isinstance(tools, dict) and len(tools) >= 1

@pytest.mark.asyncio
async def test_neo4j_server_has_tools():
    base = f"http://localhost:{os.environ.get('MCP_NEO4J_PORT','3002')}"
    client = MCPClient(base)
    tools = await client.list_tools()
    assert isinstance(tools, dict) and len(tools) >= 1
