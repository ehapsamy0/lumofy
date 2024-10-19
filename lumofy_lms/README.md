# Lumofy LMS Task: Learning Management System with Django REST API

## Objective

This project implements a Django REST API for managing learning modules in a Learning Management System (LMS). The API supports:
- Creating, updating, deleting, and retrieving courses
- Adding/removing lessons from a course
- Tracking student progress for each lesson

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository_url>
cd lumofy_lms
```
### 2. Set Up Your Environment Variables


Ensure you have the necessary environment variables set up. If using Docker, place them in the .envs/.local/.django or .envs/.production/.django file:

### 3. Set Up Docker and Start the Project

This project uses Docker for running the application. The provided Makefile simplifies the process.

Build and start the project:
```
make upbuild
```



If you only want to start the containers (without building):
```
make up
```

## API Endpoints

##### Below are the API endpoints for managing courses, lessons, and tracking student progress::

### 1. Create a Course

- Endpoint: /courses/
- Method: POST
- Body: Provide course details in JSON format.

##### Example
```
curl -X POST http://localhost:8000/courses/ \
-H "Content-Type: application/json" \
-d '{
  "lessons": [
    {
      "id": 0,
      "title": "string",
      "content": "string",
      "attendance_count": 2147483647,
      "course": 0
    }
  ],
  "name": "string",
  "description": "string",
  "attendance_count": 9223372036854776000,
  "completion_count": 9223372036854776000,
  "teacher": 0
}'

```

### 2. List All Courses
- Endpoint: /courses/
- Method: GET

```
curl http://localhost:8000/courses/
```
### 3. Retrieve, Update, or Delete a Course

- Endpoint: /courses/<id>/
- Method: `GET`, `PUT`, `PATCH`, `DELETE`

Example:
```
curl -X PUT http://localhost:8000/courses/1/ \
-H "Content-Type: application/json" \
-d '{
  "lessons": [
    {
      "id": 0,
      "title": "string",
      "content": "string",
      "attendance_count": 2147483647,
      "course": 0
    }
  ],
  "name": "string",
  "description": "string",
  "attendance_count": 9223372036854776000,
  "completion_count": 9223372036854776000,
  "teacher": 0
}'
```
## ** Important Note on Course Update and Lesson Management  ** 
When updating a course and its associated lessons, follow the rules below:
- Add New Lessons: To add new lessons to a course, simply include the lesson objects without an `id` in the request body.
- Update Existing Lessons: To update an existing lesson, provide the `id` of the lesson along with its updated data in the request body.
- Delete Lessons: To delete a lesson, omit the lesson object from the request body entirely. Any lesson object not included in the update request will be deleted from the course.

Example:

```
curl -X PUT http://localhost:8000/courses/1/ \
-H "Content-Type: application/json" \
-d '{
      "name": "Advanced Algebra",
      "description": "An updated description",
      "lessons": [
        {"id": 1, "title": "Lesson 1", "content": "Updated content"},  # Existing lesson, will be updated
        {"id": 2, "title": "Lesson 2", "content": "Updated content"},  # Existing lesson, will be updated
        {"title": "New Lesson", "content": "This is a new lesson"}      # New lesson, will be added
      ]
    }'

```
### 4. Track Progress of Students

- Endpoint: /courses/<id>/progress/
- Method: `GET`

Example:

```
curl http://localhost:8000/courses/1/progress/
```

This will return the progress of all students enrolled in the course.


### Makefile Commands

### The provided Makefile contains common commands for managing Docker containers and Django operations.

- Build and run containers: make upbuild
- Start containers: make up
- Run migrations: make migrate
- Create superuser: make superuser
- Open Django shell: make shell
- Run tests: make pytest
- Stop containers: make down
- Destroy containers and volumes: make destroy

## ** You can run any of the above commands easily by typing the desired make command. ** 
