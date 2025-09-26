// Cypher ontology schema
CREATE CONSTRAINT company_id IF NOT EXISTS FOR (c:Company) REQUIRE c.id IS UNIQUE;
CREATE INDEX company_name IF NOT EXISTS FOR (c:Company) ON (c.name);
CREATE CONSTRAINT doc_id IF NOT EXISTS FOR (d:Doc) REQUIRE d.id IS UNIQUE;
CREATE INDEX doc_url IF NOT EXISTS FOR (d:Doc) ON (d.url);
