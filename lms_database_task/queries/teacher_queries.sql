-- Retrieves all courses that a teacher is assigned to
SELECT c.name AS course_name, c.description
FROM "Courses" c
JOIN "Teacher" t ON c.teacher_id = t.id
JOIN "User" u ON t.user_id = u.id
WHERE t.id = 1; -- Replace with the specific teacher_id


