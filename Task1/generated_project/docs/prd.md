# Product Requirements Document

## Product Overview

AI Football Match Analyst is a generated web application based on the given business problem.

The system captures input data, validates it, generates an AI-style structured report, and presents the result for human review.

## Target Users

- Coach
- Match Analyst
- System Reviewer

## Main Features

- Match Input
- Data Validation
- AI-style Analysis
- Report Output
- Human Review

## User Flow

1. The user opens the generated website.
2. The user enters the required input data.
3. The Flask API validates the submitted data.
4. The AI-style analysis module generates a structured report.
5. The user reviews the generated report before using it for decision-making.

## API Endpoints

- GET /
- GET /api/sample-report
- POST /api/analyse

## Constraints

- Required fields must be validated before analysis.
- The generated output should be reviewed by a human user.
- The system should run without requiring an external AI API key by using local fallback generation.
- If DeepSeek API is enabled, it can be used to generate richer analysis.

## Success Criteria

- The website loads successfully.
- The generated image is displayed on the website.
- The user can submit valid data.
- The API returns a structured report.
- Missing required fields return a clear error message.
- The generated documentation and UML diagrams are created automatically.
