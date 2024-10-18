# Lumofy Task: File Upload Feature with Django REST API

## Objective

This task implements a Django REST API that allows users to:
- Upload files
- List all uploaded files
- Retrieve a specific file by its ID
- Bonus: File size validation using environment variables and filtering files by type (e.g., PDF, images) using `django-filter`.


## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository_url>
cd lumofy_task
```
### 2. Set Up Your Environment Variables

Go to a .envs folder and .local or .production folder and open .django file and set the maximum file size in megabytes:
```bash
MAX_FILE_SIZE_MB=5
```

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

##### The API provides the following endpoints for file upload and management:

### 1. Upload a File

- Endpoint: /api/files/upload/
- Method: POST
- Body: Send the file in a multipart/form-data request under the file key.

##### Example
```
curl -X POST http://localhost:8000/api/files/upload/ \
  -F 'file=@/path/to/your/file.pdf'
```

### 2. List All Uploaded Files
- Endpoint: /api/files/
- Method: GET

##### You can also filter by file type (e.g., pdf, jpg, etc.):
```
curl http://localhost:8000/api/files/?file_type=pdf
```
### 3. Retrieve a File by ID

- Endpoint: /api/files/<id>/
- Method: GET

Example:
```
    curl http://localhost:8000/api/files/1/
```


### Makefile Commands

### The provided Makefile contains common commands for managing Docker containers and Django operations.

- Build and run containers: make upbuild
- Start containers: make up
- Run migrations: make migrate
- Create superuser: make superuser
- Open Django shell: make shell
- Run tests: make test
- Stop containers: make down
- Destroy containers and volumes: make destroy

## ** You can run any of the above commands easily by typing the desired make command. ** 
