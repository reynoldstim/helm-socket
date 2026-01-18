
## Overall Architecture

Client (Browser / CLI)
        │
        │ WebSocket
        ▼
Control Plane (this project)
        │
        │ Session + Policy Messages
        ▼
Execution Agent (separate service)
        │
        │ Docker / K8s / SSH / PTY
        ▼
Linux Container / Remote Host

## Session State

CREATED
  ↓ (ws_attach)
ATTACHED
  ↓ (client_detach | ttl_expired)
DETACHED
  ↓ (ttl_expired | explicit_close)
TERMINATED


## Core Concepts (Domain Model)
Concept	Description
Tenant	Security boundary (org, workspace, account)
Principal	Authenticated identity (user, service, agent)
Session	Logical interactive session
Connection	A WebSocket attached to a session
Agent	Backend executor (TTY host, VM, container, etc.)
