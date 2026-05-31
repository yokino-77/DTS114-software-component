# System Design

## System Overview
A Flask application that exposes a web UI and API endpoints. It validates input and generates AI-style reports with optional DeepSeek support.

## Workflow
- User submits match data through the website.
- Flask API validates required fields.
- The analyzer generates a report using local logic or DeepSeek.
- The website displays the structured results and review note.

## Flask API Structure
- GET / - renders the website.
- GET /api/sample-report - returns a sample JSON report.
- POST /api/analyse - validates input and returns a generated report.

## AI Integration Point
- The analyzer can use DeepSeek chat completions when configured.

## Data Validation
- Required fields: team_a, team_b, score, shots, possession, events.

## Human Review
- Every report includes a human review note and a review-required flag.

## DeepSeek API Design
- Optional external service with environment variables.
- Safe fallback if the API is unavailable.

## Local Fallback Design
- All functionality works through deterministic logic when no external AI is available.