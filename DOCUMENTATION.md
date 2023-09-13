

# Task Management API Documentation

## Table of Contents

- [Introduction](#introduction)
- [Endpoints](#endpoints)
  - [Create Task](#create-task)
  - [Update Task](#update-task)
  - [Delete Task](#delete-task)
  - [Read Task](#read-task)
- [Sample Usage](#sample-usage)
- [Known Limitations and Assumptions](#known-limitations-and-assumptions)
- [Setup and Deployment](#setup-and-deployment)

## Introduction

The Task Management API allows users to manage tasks. It provides endpoints for creating, updating, deleting, and reading tasks.

## Endpoints

### Create Task

- **Endpoint**: `/api`
- **Method**: POST
- **Request Format**:
  ```json
  {
    "name": "Task Name"
  }
  ```
- **Response Format**:
  - Success (HTTP Status Code: 200):
    ```json
    {
      "response": "Task Name created successfully",
      "id": 1,
      "name": "Task Name",
      "username": "RandomlyGeneratedUsername"
    }
    ```
  - Error (HTTP Status Code: 400):
    ```json
    {
      "response": "Task Name contains an integer, not allowed"
    }
    ```

### Update Task

- **Endpoint**: `/api/<int:id>`
- **Method**: PUT
- **Request Format**:
  ```json
  {
    "name": "New Task Name",
    "username": "New Username"
  }
  ```
- **Response Format**:
  - Success (HTTP Status Code: 200):
    ```json
    {
      "response": "User update",
      "id": 1,
      "name": "New Task Name",
      "username": "New Username"
    }
    ```
  - Error (HTTP Status Code: 404):
    ```json
    {
      "response": "User with id = <id> not found"
    }
    ```
    OR
  - Error (HTTP Status Code: 400):
    ```json
    {
      "response": "New Task Name contains an integer, not allowed"
    }
    ```

### Delete Task

- **Endpoint**: `/api/<int:id>`
- **Method**: DELETE
- **Response Format**:
  - Success (HTTP Status Code: 204):
    No response body.

### Read Task

- **Endpoint**: `/api/<int:id>`
- **Method**: GET
- **Response Format**:
  - Success (HTTP Status Code: 200):
    ```json
    {
      "id": 1,
      "name": "Task Name",
      "username": "RandomlyGeneratedUsername"
    }
    ```
  - Error (HTTP Status Code: 404):
    ```json
    {
      "response": "No Result with id=<id> Found"
    }
    ```

## Sample Usage

Here are some sample API requests and their expected responses:

1. **Create Task**
   - Request:
     ```json
     POST /api
     {
       "name": "Task 1"
     }
     ```
   - Response (Success):
     ```json
     {
       "response": "Task 1 created successfully",
       "id": 1,
       "name": "Task 1",
       "username": "RandomlyGeneratedUsername"
     }
     ```

2. **Update Task**
   - Request:
     ```json
     PUT /api/1
     {
       "name": "Updated Task 1",
       "username": "NewUsername"
     }
     ```
   - Response (Success):
     ```json
     {
       "response": "User update",
       "id": 1,
       "name": "Updated Task 1",
       "username": "NewUsername"
     }
     ```

3. **Delete Task**
   - Request:
     ```json
     DELETE /api/1
     ```
   - Response (Success):
     No response body.

4. **Read Task**
   - Request:
     ```
     GET /api/1
     ```
   - Response (Success):
     ```json
     {
       "id": 1,
       "name": "Updated Task 1",
       "username": "NewUsername"
     }
     ```

## Known Limitations and Assumptions

- The API generates a random username when creating a task. Therefore, the actual username may vary.
- The API assumes that the `name` field should not contain integers, and it will return an error if an integer is detected in the `name`.

## Setup and Deployment

Follow these steps to set up and deploy the API:

1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Set the environment variables for the Flask app:
   - `SECRET_KEY`: A secret key for Flask.
   - `SQLALCHEMY_DATABASE_URI`: The URI for the SQLite database (e.g., `'sqlite:///project.db'`).
4. Run the API using `python app.py`.

The API will be accessible at `http://localhost:5000`. You can test the API using the provided endpoints and sample requests.
