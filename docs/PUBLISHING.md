# Publishing guide

This covers: 1) GitHub; 2) PyPI; 3) Language‑agnostic distribution.

---

## 1) Publish on GitHub (Linux + PyCharm)

1. **Create a GitHub repository**
   - Name: `hktoll`
   - Init with no files (we already have them).

2. **Initialize git locally**
   ```bash
   cd hktoll
   git init
   git add -A
   git commit -m "chore: initial public release"
   ```

3. **Set the remote & push**
   ```bash
   git branch -M main
   git remote add origin git@github.com:YOURUSER/hktoll.git
   git push -u origin main
   ```

4. **Enable CI (optional but recommended)**
   - CI config is already under `.github/workflows/ci.yml`.
   - On GitHub: Settings → Actions → General → Allow all actions.

5. **Add repository metadata**
   - Description, topics: `hong-kong`, `transport`, `tolls`, `routing`.
   - Add a README badge for PyPI once published.

### Using PyCharm
- Open PyCharm → *Open* → select this folder.
- Create a Python interpreter using `.venv` (or your preferred environment).
- Run/Debug configurations:
  - `Module name`: `hktoll.cli`
  - Parameters: `route --coords "114.1582,22.2799;114.1721,22.2975"`
  - Working directory: project root.

---

## 2) Distribute on PyPI

1. **Create accounts**
   - https://pypi.org/ and https://test.pypi.org/ (recommended to test first).
   - Create an API token (user settings) and store it securely.

2. **Build**
   ```bash
   python -m pip install -U build twine
   python -m build  # creates dist/*.tar.gz and dist/*.whl
   ```

3. **Upload to Test PyPI (dry run)**
   ```bash
   python -m twine upload --repository testpypi dist/*
   ```

4. **Install from Test PyPI and test**
   ```bash
   python -m pip install --index-url https://test.pypi.org/simple/ --no-deps hktoll
   ```

5. **Upload to PyPI**
   ```bash
   python -m twine upload dist/*
   ```

6. **Release on GitHub**
   - Tag a release: `git tag v0.1.0 && git push origin v0.1.0`
   - Create a GitHub Release with release notes.

---

## 3) Make it language‑agnostic

Option A: **HTTP service**
- `hktoll serve` starts a FastAPI server with `/v1/tolls/route`.
- Docker:
  ```bash
  docker build -t hktoll:0.1.0 .
  docker run --rm -p 8000:8000 hktoll:0.1.0
  ```
- Any language can call the REST endpoint with JSON (examples under `examples/`).

Option B: **CLI**
- Use the `hktoll` CLI and parse JSON output in any language (e.g. Node, Go, Java).

Option C: **gRPC (advanced)**
- Not included in v1 to keep deps small; can be added later if demanded.

---

## 4) Project hygiene checklist for a first OSS project

- [x] License
- [x] README with quickstart & usage
- [x] Tests (`pytest`), CI
- [x] Versioning and CHANGELOG
- [x] Code style (ruff), pre-commit (optional)
- [x] Clear contribution guidelines and code of conduct
- [x] SECURITY policy
