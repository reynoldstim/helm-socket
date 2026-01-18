# API Notes

/health

/v1/sessions (POST only)

/v1/sessions/{id}/ws


POST /v1/sessions
Authorization: Bearer <JWT>

## Request Body
{
  "target": {
    "type": "agent",
    "id": "agent-abc"
  },
  "ttl_seconds": 3600,
  "metadata": {
    "purpose": "debug"
  }
}
## Response
{
  "session_id": "sess_123",
  "tenant_id": "acme",
  "expires_at": "2026-04-01T12:00:00Z",
  "ws_url": "wss://api.example.com/v1/sessions/sess_123/ws"
}

GET /v1/sessions/{session_id}
DELETE /v1/sessions/{session_id}

# WebSocket Messages

client -> api
GET /v1/sessions/{session_id}/ws
Authorization: Bearer <JWT>
{
  "type": "attach",
  "protocol_version": 1,
  "role": "client"
}
{
  "type": "heartbeat"
}
{
  "type": "detach"
}

api -> client
{
  "type": "session.accepted",
  "session_id": "sess_123"
}
{
  "type": "session.terminated",
  "reason": "ttl_expired"
}
{
  "type": "error",
  "code": "unauthorized"
}
