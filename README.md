# agentic-kg-builder
Set of agents is used to generate a knowledge graph from structured and unstructured data in a neo4j database with MCP connections from google's ADK.

One-line project goal and stack (ADK orchestrator + MCP servers + Neo4j).

Quick start:

cp configs/.env.example .env

make up && sleep 5 && make init

pytest -q

mcp_servers/content_server and mcp_servers/neo4j_server should each expose:

GET /tools → JSON dict of tool schemas (stubbed at first).

POST /call/<tool> → stub returns { "ok": true }.

Acceptance tests (run locally):
cp configs/.env.example .env

make up

docker ps shows 3 containers (kg_neo4j, mcp_content, mcp_neo4j)

pytest -q passes (2 tests)

Open http://localhost:7474
 (Neo4j Browser) and login with neo4j/test.