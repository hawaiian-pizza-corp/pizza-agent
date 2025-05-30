# 🍕 Pizza Agent 🕵️‍♂️

## Requirements

- Docker Desktop + MCP Toolkit extension
- Install the Brave MCP server (you need an API key - there is a free plan: https://brave.com/search/api/)

## Start Bob, the Pizza Agent

### "Run" mode with Docker Compose

If you are on macOS
```bash
cd agents
docker compose up --build
```

If you are on Linux:
```bash
cd agents
docker compose --file compose.linux.yml up --build
```
> - You can change of model by updating the `.env` file
> - ✋ This demo is using tools, so my advice is to stay with `ai/qwen2.5:latest`

### Development mode using DevContainer
> 👀 look at the `.devcontainer/` directory

#### First time - Initialize the Python environment

**Create virtual environment**:
```bash
python -m venv discovery
```

**Activate virtual environment**:
```bash
source discovery/bin/activate
```

> **To deactivate virtual environment**
>  ```bash
>  deactivate
>  ```

**Add dependencies**:

```
pip install -r requirements.txt
```

#### Start the agent

```bash
# activate the virtual environment: source discovery/bin/activate
cd agents
adk web
```
> Always use the python virtual environment when running the agent

## Use the demo agent

