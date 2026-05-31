# Testing Plan

## Unit Testing
- Test Flask routes and validation logic.
- Test report generation with valid and invalid data.

## API Testing
- GET / should return 200.
- GET /api/sample-report should return JSON.
- POST /api/analyse should handle valid payloads and reject missing fields.

## Validation Testing
- Confirm required fields are enforced.

## CI/CD Testing
- Use GitHub Actions to install dependencies and run pytest.

## Deployment Testing
- Ensure the site loads locally.
- Confirm the Flask API returns expected JSON responses.