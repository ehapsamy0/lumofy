# Backend Engineer Technical Assessment

This repository contains multiple sections to assess backend development skills, problem-solving abilities, and familiarity with Django, Django REST Framework, PostgreSQL, and more. Each section focuses on a specific aspect of backend engineering, with the links to the relevant repositories and tasks.

## Objective

This assessment evaluates the candidate’s backend development skills across several areas:
- **Database Design & SQL**: Proficiency in database schema design and query writing.
- **Python/Django**: Ability to build features using Django and Django REST Framework.
- **API Design**: Creating, updating, and retrieving data via APIs.
- **Code Review**: Understanding of security, performance, and maintainability.
- **React Integration**: (Optional) Implementing frontend components that interact with the backend.

---

## Section 1: General Coding & Problem Solving (60 minutes)

### 1. SQL and Database Design (30 minutes)

**Problem**: Design a database schema for a Learning Management System (LMS) that supports:
- Multiple courses
- Students enrolling in courses
- Teachers assigned to multiple courses
- Each course having multiple lessons
- Students tracking lesson completion status

**Tasks**:
- Provide the database schema design (ER diagram optional).
- Write SQL queries to:
  1. Retrieve all students enrolled in a given course.
  2. Get the progress of each student per course based on lesson completion.
  3. Retrieve the courses a teacher is assigned to.

**Tech Stack**: PostgreSQL

For detailed documentation and setup instructions for this task, see the following repository:
[**SQL and Database Design Task**](https://github.com/ehapsamy0/lumofy/blob/main/lms_database_task/README.md)

---

### 2. Python/Django Problem (30 minutes)

**Problem**: Implement a feature where users can upload files and access them later.

**Tasks**:
- Create a Django model that supports file uploads.
- Implement a basic Django REST API to:
  - Upload a file
  - List all uploaded files
  - Retrieve a specific file by ID
- Bonus: Add file size validation and allow filtering files by type (e.g., PDF, image).

**Tech Stack**: Django, Django REST Framework

For detailed documentation and setup instructions for this task, see the following repository:
[**File Upload Task**](https://github.com/ehapsamy0/lumofy/blob/main/lumofy_task/README.md)

---

## Section 2: API Design & Implementation (60 minutes)

**Problem**: You’re building an API for managing learning modules in an LMS.

**Tasks**:
- Implement a Django REST API for:
  1. Creating a course (POST)
  2. Retrieving the list of all courses (GET)
  3. Adding/removing lessons from a course (PUT)
  4. Tracking progress of students (GET)
- Handle edge cases like invalid input, missing resources, and unauthorized access.

**Tech Stack**: Django, Django REST Framework

*This section is still under development and will be updated soon.*

---

## Section 3: Code Review & Engineering Mindset (45 minutes)

**Problem**: Review a Django view that handles user registration, identify potential improvements, and refactor the code.

**Tasks**:
- Highlight at least 3 potential improvements in terms of performance, security, and maintainability.
- Refactor the code to address the issues you found.

*This section is still under development and will be updated soon.*

---

## Section 4: React Integration (Optional, 30 minutes)

**Problem**: Implement a simple React component that fetches the list of courses from the Django REST API and displays them in a list format.

**Bonus**: Implement pagination to handle a large number of courses.

*This section is still under development and will be updated soon.*

---

## Assessment Submission Guidelines

- Provide the code for each section in a GitHub repository or as a zip file.
- Ensure your code is modular, well-documented, and includes necessary tests.
- Mention any assumptions or design decisions you’ve made.
  
---

**Note**: As more tasks are completed, this README will be updated with additional links and details for each section.

