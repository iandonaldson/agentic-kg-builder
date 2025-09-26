# MCP client logic
from typing import Any, Dict
import httpx

class MCPClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    async def list_tools(self) -> Dict[str, Any]:
        async with httpx.AsyncClient(timeout=30) as client:
            r = await client.get(f"{self.base_url}/tools")
            r.raise_for_status()
            return r.json()

    async def call(self, tool: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        async with httpx.AsyncClient(timeout=120) as client:
            r = await client.post(f"{self.base_url}/call/{tool}", json=payload)
            r.raise_for_status()
            return r.json()

