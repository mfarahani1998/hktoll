def test_import():
    import hktoll

    assert hasattr(hktoll, "compute_tolls")
