# Contributing Guidelines

Welcome to the project! Please follow these rules for smooth collaboration.

## Branch Naming
Each student must work on their own branch:
<USN>_<feature>

Example:
1CR23AD001_stack

## File Naming
- Use **snake_case** for Python files → `data_loader.py`
- Use **PascalCase** for notebooks → `DataAnalysis.ipynb`
- Avoid spaces or special characters.

## Commit Messages
Use clear, descriptive commit messages:
feat: added student login feature
fix: corrected bug in data processing
docs: updated README with setup steps

## Workflow
1. **Clone** the repo.
2. **Create your branch**:  
    git checkout -b <USN_feature>
3. Make changes in src/ or your team’s folder.
4. Commit regularly.
5. Push your branch:
    git push origin <branch_name>
6. Open a Pull Request (PR) for review.

## Code Style
Use PEP8 for Python.
Always activate virtual environment.
Don’t push venv/, .idea/, .vscode/, or temporary files.
