#!/usr/bin/env bash
set -euo pipefail
echo "Creating base constraints in Neo4j..."
cat schemas/ontology.cypher | cypher-shell -u neo4j -p "$(echo $NEO4J_AUTH | cut -d/ -f2)"
echo "Done."

