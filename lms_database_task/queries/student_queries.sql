-- Retrieves all students enrolled in a given course based on course_id
SELECT u.first_name, u.last_name, s.id AS student_id
FROM "Enrollments" e
JOIN "Student" s ON e.student_id = s.id
JOIN "User" u ON s.user_id = u.id
WHERE e.course_id = 1; -- Replace with the specific course_id


-- Retrieves the progress of each student in terms of lessons completed per course
SELECT u.first_name, u.last_name, c.name AS course_name, COUNT(lc.lesson_id) AS lessons_completed
FROM "Enrollments" e
JOIN "Student" s ON e.student_id = s.id
JOIN "User" u ON s.user_id = u.id
JOIN "Courses" c ON e.course_id = c.id
LEFT JOIN "Lesson_Completion" lc ON lc.student_id = s.id AND lc.lesson_id IN (
    SELECT id FROM "Lessons" WHERE course_id = e.course_id
)
WHERE e.course_id = 1  -- Replace with the specific course_id
GROUP BY u.first_name, u.last_name, c.name;


