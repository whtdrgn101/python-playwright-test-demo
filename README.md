# Python API Test Demo

## Setup

### 1. Create a virtual environment (recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

If you have pip available:
```bash
pip install -e .
```

Or install pytest-asyncio directly:
```bash
pip install pytest-asyncio
```

If pip is not available, install it first:
```bash
sudo apt install python3-pip python3-venv
```

Then create and activate the virtual environment as shown above.

### 3. Run tests

```bash
pytest tests/ -v
```

## Dependencies

- pytest-asyncio (for async test support)
- rest_api_testing (your testing library)

