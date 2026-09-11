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
