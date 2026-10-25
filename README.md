# Django Code Intelligence System

> Fill this top section from your Examate project card on Day 1. Replace every line in angle brackets.

## Problem
>Django contains thousands of Python files, making it difficult for developers to quickly understand its internal implementation. Developers often spend time searching through source code to find relevant information. AI-powered code assistants may provide outdated answers when the source code changes and the searchable index is not updated. My project aims to solve this problem by detecting code changes and updating only the affected files, helping developers get accurate and up-to-date answers.

## Who it is for
>Django backend developers who need to understand and navigate large codebases.
>Software development team leads who need to track code changes and find accurate information about Django's implementation

## Signature feature
>Automatically detects added, modified, and deleted Django source files and updates only the affected files in the searchable index, keeping AI-generated answers up to date with the latest code changes.

## Hardest problem (my interview story)
>The hardest problem is keeping the searchable index synchronized with the Django source code when files are added, modified, or deleted. The system must update only the affected files without re-indexing the entire codebase and ensure that AI-generated answers refer to the correct and latest source code.

## Dataset
|              Source           |                 Link             |        Documents    |           Pages           |  Licence / terms     |
|-------------------------------|----------------------------------|---------------------|---------------------------|----------------------|
| Django source code repository | https://github.com/django/django | 2,937 Python files  | N/A — source-code dataset | BSD 3-Clause License |

## 10 real questions
See [docs/QUESTIONS.md](docs/QUESTIONS.md).

## Run it
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
cp .env.example .env                                 # Windows: copy .env.example .env
uvicorn app.main:app --reload
curl localhost:8000/health
```
## Quality checks

Run these commands before pushing changes:

```powershell
ruff check .
python -m pytest -q

## Live link
<Added in Week 2>
