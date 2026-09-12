# LangChain Masterclass

## Setup

Open PowerShell in the project directory and create the virtual environment:

```powershell
python -m venv .venv
```

Activate the environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the project dependencies:

```powershell
python -m pip install -r requirements.txt
```

Create the local environment file from the example:

```powershell
Copy-Item .env.example .env
```

Open `.env` and replace the placeholder value with your Google API key:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

Keep `.env` private. It is excluded from version control.

### Linux and macOS

Open a terminal in the project directory and create the virtual environment:

```bash
python3 -m venv .venv
```

Activate the environment:

```bash
source .venv/bin/activate
```

Install the project dependencies:

```bash
python -m pip install -r requirements.txt
```

Create the local environment file from the example:

```bash
cp .env.example .env
```

Open `.env` and replace `your_google_api_key_here` with your Google API key.
