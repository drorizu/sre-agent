# SRE Agent

AI-powered Site Reliability Engineering (SRE) investigation and infrastructure intelligence platform.

SRE Agent is a modular, extensible platform designed to automate infrastructure investigations, analyze operational incidents, identify potential root causes, and assist engineering teams in maintaining reliable systems.

## Features
- AI-powered infrastructure investigations
- LLM provider abstraction
- Automated incident analysis
- Infrastructure monitoring and diagnostics
- Extensible skills and plugin architecture
- Integrations with Prometheus, Grafana, Kubernetes, AWS, and databases
- Model Context Protocol (MCP) support
- Multi-tenant architecture
- Authentication and role-based access control
- Governance, permissions, and audit logging
- Distributed background task execution
- Usage metering and billing
- OpenTelemetry-based observability

## Architecture

The platform follows a modular monolith architecture with clearly separated application domains.

Core components include:

- API: HTTP endpoints and request validation.
- Agent: LLM integration, context management, and planning.
- Orchestrators: Investigation coordination and execution.
- Skills: Reusable infrastructure investigation capabilities.
- Connectors: External infrastructure integrations.
- Plugins: Extensible functionality.
- MCP: Model Context Protocol integrations.
- Tools: Controlled execution of agent capabilities.
- Tenancy: Organization and tenant isolation.
- Auth: Authentication and authorization.
- Governance: Policies, approvals, and audit trails.
- Observability: Metrics, tracing, and telemetry.
- Billing: Usage metering and commercial entitlements.
- Persistence: Database models and repositories.
- Workers: Asynchronous background processing.

## Technology Stack
| Component | Technology |
|---|---|
| Language | Python 3.12+ |
| API framework | FastAPI |
| Data validation | Pydantic |
| ORM | SQLAlchemy 2.0 |
| Database | PostgreSQL |
| Migrations | Alembic |
| Cache and broker | Redis |
| Background tasks | Celery |
| Containers | Docker |
| Testing | Pytest |
| Code quality | Ruff and Mypy |
| Observability | OpenTelemetry |

## Requirements
- Python 3.12 or newer
- Docker Desktop
- Docker Compose
- Git
- Getting Started

Clone the repository:

```bash
git clone github/drorizu/sre-agent.git
cd sre-agent
```


Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -e ".[dev]"
```

Configure environment variables:

```powershell
Copy-Item .env.example .env
```

Start infrastructure services:

```bash
docker compose up -d db redis
```

Run database migrations:

```bash
alembic upgrade head
```

Start the application:

```bash
uvicorn sre_agent.main:app --reload
```

## API documentation:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
- Health check: http://localhost:8000/health

## Development

Run tests:

```bash
pytest
```

Run linting:

```bash
ruff check .
```

Run formatting:

```bash
ruff format .
```

Run static type checking:

```bash
mypy src
```

## Project Structure

The source code is located in src/sre_agent/.

Application modules are organized by domain to maintain separation of concerns, testability, and extensibility.

See docs/architecture.md for additional architectural information.

## Security

Security is a core design requirement.

The platform is designed to incorporate:

- Tenant isolation
- Role-based access control
- Secure credential management
- Tool execution policies
- Human approval for sensitive operations
- Audit logging
- Input validation
- Secure API authentication

See docs/security.md.

## License

Proprietary software. All rights reserved.

## Project Structure
```
just give the codes one by one to fill these: 
sre-agent/
│
├── README.md
├── LICENSE
├── pyproject.toml
├── Makefile
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .gitignore
├── .env.example
├── alembic.ini
│
├── alembic/
│   ├── env.py
│   └── versions/
│
├── src/
│   └── sre_agent/
│       ├── __init__.py
│       ├── main.py
│       │
│       ├── api/
│       │   ├── __init__.py
│       │   ├── dependencies.py
│       │   ├── middleware.py
│       │   ├── routes/
│       │   │   ├── health.py
│       │   │   ├── investigations.py
│       │   │   ├── organizations.py
│       │   │   ├── connectors.py
│       │   │   ├── usage.py
│       │   │   └── admin.py
│       │   └── schemas/
│       │       ├── common.py
│       │       ├── investigation.py
│       │       ├── connector.py
│       │       └── organization.py
│       │
│       ├── core/
│       │   ├── config.py
│       │   ├── logging.py
│       │   ├── exceptions.py
│       │   ├── lifecycle.py
│       │   └── constants.py
│       │
│       ├── agent/
│       │   ├── llm/
│       │   │   ├── base.py
│       │   │   ├── client.py
│       │   │   └── providers/
│       │   ├── prompts/
│       │   ├── context/
│       │   └── planning/
│       │
│       ├── orchestrators/
│       │   ├── agent_orchestrator.py
│       │   └── investigation_orchestrator.py
│       │
│       ├── skills/
│       │   ├── base.py
│       │   ├── registry.py
│       │   ├── loader.py
│       │   └── infrastructure/
│       │       ├── cpu.py
│       │       ├── memory.py
│       │       ├── disk.py
│       │       ├── health.py
│       │       └── logs.py
│       │
│       ├── plugins/
│       │   ├── base.py
│       │   ├── manager.py
│       │   ├── registry.py
│       │   └── manifest.py
│       │
│       ├── connectors/
│       │   ├── base.py
│       │   ├── registry.py
│       │   ├── manager.py
│       │   ├── prometheus/
│       │   ├── grafana/
│       │   ├── kubernetes/
│       │   ├── aws/
│       │   └── databases/
│       │
│       ├── mcp/
│       │   ├── client.py
│       │   ├── server.py
│       │   ├── registry.py
│       │   └── adapters.py
│       │
│       ├── tools/
│       │   ├── base.py
│       │   ├── registry.py
│       │   ├── executor.py
│       │   ├── validation.py
│       │   └── policies.py
│       │
│       ├── investigations/
│       │   ├── models.py
│       │   ├── repository.py
│       │   ├── state_manager.py
│       │   └── lifecycle.py
│       │
│       ├── tenancy/
│       │   ├── context.py
│       │   ├── models.py
│       │   ├── repository.py
│       │   └── isolation.py
│       │
│       ├── auth/
│       │   ├── authentication.py
│       │   ├── authorization.py
│       │   ├── rbac.py
│       │   └── tokens.py
│       │
│       ├── governance/
│       │   ├── permissions.py
│       │   ├── policies.py
│       │   ├── approvals.py
│       │   └── audit.py
│       │
│       ├── observability/
│       │   ├── telemetry.py
│       │   ├── tracing.py
│       │   ├── metrics.py
│       │   ├── instrumentation.py
│       │   └── llm_tracing.py
│       │
│       ├── billing/
│       │   ├── models.py
│       │   ├── metering.py
│       │   ├── entitlements.py
│       │   └── usage.py
│       │
│       ├── persistence/
│       │   ├── database.py
│       │   ├── models/
│       │   └── repositories/
│       │
│       ├── workers/
│       │   ├── worker.py
│       │   └── tasks/
│       │
│       └── services/
│           ├── response_service.py
│           └── investigation_service.py
│
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── contract/
│   ├── security/
│   └── e2e/
│
├── deploy/
│   ├── docker/
│   ├── kubernetes/
│   └── monitoring/
│
├── docs/
│   ├── architecture.md
│   ├── security.md
│   ├── api.md
│   ├── connectors.md
│   ├── plugins.md
│   └── development.md
│
└── scripts/
    ├── create_admin.py
    ├── migrate.py
    └── seed.py
```

See LICENSE for details.

## Disclaimer

SRE Agent is an infrastructure investigation platform. Automated recommendations and diagnostic findings should be reviewed by authorized operators before disruptive infrastructure changes are made.
