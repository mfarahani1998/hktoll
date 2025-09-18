import os
from datetime import datetime


# Patch environment to point to sample data via URL overrides
def _override_url(path):
    return "file://" + os.path.abspath(path)


def test_offline_route_uses_samples(monkeypatch, tmp_path):
    import hktoll.datasets as ds

    root = os.path.join(os.path.dirname(__file__), "data")

    # Monkeypatch downloader to read local files
    def fake_download(url: str) -> bytes:
        if url.endswith("TUN_BRIDGE_TOLL.csv"):
            return open(os.path.join(root, "hk_flat_sample.csv"), "rb").read()
        if url.endswith("TUN_BRIDGE_TV_TOLL.csv"):
            return open(os.path.join(root, "hk_tv_sample.csv"), "rb").read()
        if url.endswith("TRAFFIC_FEATURES.kmz"):
            return open(os.path.join(root, "traffic_features_sample.kmz"), "rb").read()
        raise AssertionError("Unexpected URL " + url)

    monkeypatch.setattr(ds, "_download", fake_download)

    from hktoll.engine import compute_tolls

    coords = [(114.1582, 22.2799), (114.1640, 22.2801), (114.1721, 22.2975)]
    when = datetime.fromisoformat("2025-09-17T08:30:00+08:00")
    events, total = compute_tolls(coords, vehicle="private_car", when=when)
    assert total >= 30.0
    assert any(e.facility_id for e in events)
