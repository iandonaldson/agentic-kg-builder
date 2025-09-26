# Smoke test for environment
def test_repo_layout():
    import os
    expected = ["orchestrator", "mcp_servers", "schemas", "configs", "docker-compose.yml"]
    for e in expected:
        assert os.path.exists(e), f"Missing {e}"

