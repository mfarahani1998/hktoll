#!/usr/bin/env bash
set -euo pipefail
curl -s -X POST http://localhost:8000/v1/tolls/route -H "content-type: application/json" -d '{
  "coords": [[114.1582,22.2799],[114.1640,22.2801],[114.1721,22.2975]],
  "vehicle": "private_car",
  "when": "2025-09-17T08:30:00+08:00"
}' | jq .
