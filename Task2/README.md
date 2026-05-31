# DTS114TC Coursework Project

## Project Overview

This repository contains an AI-powered meta-software development generator. The project uses a Jupyter Notebook to create a complete Flask-based software project, including SDLC documentation, UML files, a generated website image, and a Flask API.

The current demonstration business problem is `AI Football Match Analyst`, but the notebook is designed so the user can change the `business_problem` variable and regenerate a different project.

## Meta-Software Generator Idea

The notebook demonstrates how an AI-assisted development assistant can produce:
- problem statement
- personas
- PRD
- requirements
- user stories
- system design
- testing plan
- UML diagrams
- Flask API code
- website UI and generated image

## Changing the Business Problem

Open `Task1/Task1.ipynb` and edit the `business_problem` variable near the top of the notebook. After changing it, rerun the notebook to generate a new project specification.

## DeepSeek API Support

The notebook can optionally use DeepSeek API for richer generation, but fallback generation is enabled by default.

### Environment variables

Create a `.env` file from `.env.example` and set values only if you want to enable external AI:

```env
DEEPSEEK_API_KEY=your_deepseek_api_key_here
DEEPSEEK_BASE_URL=https://api.deepseek.com
DEEPSEEK_MODEL=deepseek-chat
USE_EXTERNAL_AI=false
```

## Why Fallback Mode Exists

The submitted prototype supports optional DeepSeek API integration. However, fallback generation is enabled by default to ensure reproducibility, testing stability, and deployment reliability.

## Running the Notebook

1. Open `Task1/Task1.ipynb`.
2. Run all cells in order.
3. The notebook will generate the project files inside `Task1/generated_project`.

## Running the Flask App Locally

From the project root or `Task1/generated_project` directory:

```bash
python Task1/generated_project/app.py
```

Then open `http://127.0.0.1:5000`.

## Running Tests

From the project root:

```bash
pytest Task2/tests
```

## GitHub Version Control

Use commits and branches to track development. Capture a screenshot of your commit history for submission.

## GitHub Actions

The GitHub Actions workflow is configured in `.github/workflows/python-app.yml` and copied to `Task2/github_actions_workflow.yml` for coursework evidence.

## Deployment

Deploy to Render, Railway, or PythonAnywhere. If using Render, set environment variables in the service dashboard only if you want external AI support.

## Screenshots to Capture Manually

See `Task2/screenshots/README_screenshots.md` for required screenshot guidance.
