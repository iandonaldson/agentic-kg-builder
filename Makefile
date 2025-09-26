.PHONY: up down logs init test fmt

up:
	docker compose up -d --build

down:
	docker compose down -v

logs:
	docker compose logs -f

init:
	bash scripts/init_neo4j.sh

test:
	pytest -q

fmt:
	trufflehog --version >/dev/null 2>&1 || true
	black orchestrator mcp_servers || true
	trufflehog filesystem --no-update --fail --entropy=False . || true
