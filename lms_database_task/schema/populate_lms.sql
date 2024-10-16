-- Insert sample data into the User table
INSERT INTO "User" (id, first_name, last_name, email, phone, role, dob, created_at, updated_at)
VALUES
    (1, 'Alice', 'Smith', 'alice@example.com', '1234567890', 'student', '2000-01-01', NOW(), NOW()),
    (2, 'Bob', 'Johnson', 'bob@example.com', '0987654321', 'teacher', '1980-02-02', NOW(), NOW()),
    (3, 'Charlie', 'Brown', 'charlie@example.com', '1122334455', 'student', '2001-03-03', NOW(), NOW());

-- Insert sample data into the Teacher table
INSERT INTO "Teacher" (id, user_id, specialization)
VALUES
    (1, 2, 'Mathematics');

-- Insert sample data into the Student table
INSERT INTO "Student" (id, user_id, created_at, updated_at)
VALUES
    (1, 1, NOW(), NOW()),
    (2, 3, NOW(), NOW());

-- Insert sample data into the Courses table
INSERT INTO "Courses" (id, name, description, teacher_id, attendance_count, completion_count, created_at)
VALUES
    (1, 'Algebra 101', 'Introduction to Algebra', 1, 0, 0, NOW()),
    (2, 'Calculus 101', 'Introduction to Calculus', 1, 0, 0, NOW());

-- Insert sample data into the Lessons table
INSERT INTO "Lessons" (id, title, content, course_id, attendance_count)
VALUES
    (1, 'Lesson 1', 'Content for Lesson 1', 1, 0),
    (2, 'Lesson 2', 'Content for Lesson 2', 1, 0),
    (3, 'Lesson 1', 'Content for Lesson 1', 2, 0);

-- Insert sample data into the Enrollments table
INSERT INTO "Enrollments" (id, student_id, course_id, status)
VALUES
    (1, 1, 1, 1),  -- 1 means enrolled
    (2, 2, 2, 1);

-- Insert sample data into the Lesson_Completion table
INSERT INTO "Lesson_Completion" (id, student_id, lesson_id, completion_date)
VALUES
    (1, 1, 1, NOW()),  -- Student 1 completed Lesson 1 in Course 1
    (2, 2, 3, NOW());  -- Student 2 completed Lesson 1 in Course 2
