# API

## Python

```python
from hktoll import compute_tolls, annotate_geojson_with_tolls, TollEvent

events, total = compute_tolls(route=[(114.16,22.28),(114.18,22.29)], vehicle="private_car")
```

## REST

- `POST /v1/tolls/route`:
  - body: `{ "coords": [[lon,lat],...], "vehicle": "private_car", "when": "ISO-8601" }`
  - response: `{ "total_hkd": 60.0, "events": [TollEvent,...] }`
