# Lumofy Task:

## First : Learning Management System (LMS) Database Design

### Entity Relationship Diagram (ERD):
![alt erd](https://github.com/ehapsamy0/lumofy/blob/main/lms_database_task/images/lms_db_schema.jpeg)


### Objective

This repository contains the database design and SQL scripts for a Learning Management System (LMS). The LMS supports:

- Multiple courses
- Students enrolling in courses
- Teacher assignments to multiple courses
- Multiple lessons per course
- Student lesson completion tracking

### Project Structure

```
lms_database_task/
    │
    ├── schema/
    │   ├── lms_schema.sql              # SQL file for setting up the database schema
    │   └── populate_lms.sql            # SQL file for inserting initial data into the database
    │
    ├── queries/
    │   ├── student_queries.sql         # SQL queries related to student data
    │   └── teacher_queries.sql         # SQL queries related to teacher data
    │
    └── images/
        └── lms_schema_diagram.png      # Optional ER diagram of the database schema
```

### Database Schema Design

The LMS database consists of the following key tables:

- User: Holds general user data with fields for first_name, last_name, email, and role (either student or teacher).
- Teacher: Contains data specific to teachers, with a foreign key linking to the User table.
- Student: Contains data specific to students, also linked to the User table.
- Courses: Represents courses, including name, description, and the assigned teacher_id.
- Lessons: Each course contains multiple lessons.
- Enrollments: A join table tracking which students are enrolled in which courses.
- Lesson_Completion: Tracks which lessons each student has completed.

### Setup Instructions

1. Clone the Repository:
    ```
    git clone <repository_url>
    cd lms_database_task
    ```

2. Create the Database: Connect to PostgreSQL and create a database for the LMS::

    ```
    CREATE DATABASE lu_lms;
    ```
3. Run the Schema Script: Create the tables by running the schema script:
    ```
    psql -U postgres -d lu_lms -f schema/lms_schema.sql
    ```
4. Populate the Database: Populate the database with initial data using:
    ```
    psql -U postgres -d lu_lms -f schema/populate_lms.sql
    ```
5. Run the SQL Queries: After setting up the database, you can run the provided queries.
   - Teacher Queries:

       ```
       psql -U postgres -d lu_lms -f queries/teacher_queries.sql
       ```

   - Student Queries:

       ```
       psql -U postgres -d lu_lms -f queries/student_queries.sql
       ```

### SQL Queries Explained

The following SQL queries have been included:

1. Retrieve All Students Enrolled in a Given Course:
    - Located in student_queries.sql
    - This query fetches student details for a specific course by joining the Enrollments, Student, and User tables.

2. Get Student Progress per Course:
    - Located in student_queries.sql
    - This query calculates each student’s progress by counting lessons completed per course, joining Lesson_Completion,     Enrollments, and Lessons.

3. Retrieve Courses Assigned to a Teacher:
    - Located in teacher_queries.sql
    - This query lists all courses assigned to a specific teacher by joining the Courses and Teacher tables.

### Notes

- Case Sensitivity: Table and column names are case-sensitive. Use double quotes for table names like `User`, `Teacher`, and `Courses` in your queries to ensure compatibility.
- Foreign Key Constraints: Ensure data is inserted in the correct order as per foreign key relationships. The `populate_lms.sql` file has been structured accordingly.
