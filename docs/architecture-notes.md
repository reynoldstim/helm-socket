
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
