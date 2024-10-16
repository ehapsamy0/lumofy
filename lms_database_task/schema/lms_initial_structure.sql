CREATE TABLE "Lesson_Completion"(
    "id" BIGINT NOT NULL,
    "student_id" BIGINT NOT NULL,
    "lesson_id" BIGINT NOT NULL,
    "completion_date" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL
);
ALTER TABLE
    "Lesson_Completion" ADD PRIMARY KEY("id");
CREATE TABLE "Enrollments"(
    "id" BIGINT NOT NULL,
    "student_id" BIGINT NOT NULL,
    "course_id" BIGINT NOT NULL,
    "status" BIGINT NOT NULL
);
ALTER TABLE
    "Enrollments" ADD PRIMARY KEY("id");
CREATE TABLE "Student"(
    "id" BIGINT NOT NULL,
    "user_id" BIGINT NOT NULL,
    "created_at" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL,
    "updated_at" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL
);
ALTER TABLE
    "Student" ADD PRIMARY KEY("id");
CREATE TABLE "Courses"(
    "id" BIGINT NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "description" TEXT NOT NULL,
    "teacher_id" BIGINT NOT NULL,
    "attendance_count" BIGINT NOT NULL,
    "completion_count" BIGINT NOT NULL,
    "created_at" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL
);
ALTER TABLE
    "Courses" ADD PRIMARY KEY("id");
CREATE TABLE "Teacher"(
    "id" BIGINT NOT NULL,
    "user_id" BIGINT NOT NULL,
    "specialization" TEXT NOT NULL
);
ALTER TABLE
    "Teacher" ADD PRIMARY KEY("id");
CREATE TABLE "Lessons"(
    "id" BIGINT NOT NULL,
    "title" VARCHAR(255) NOT NULL,
    "content" TEXT NOT NULL,
    "course_id" BIGINT NOT NULL,
    "attendance_count" INTEGER NOT NULL
);
ALTER TABLE
    "Lessons" ADD PRIMARY KEY("id");
CREATE TABLE "User"(
    "id" BIGINT NOT NULL,
    "first_name" VARCHAR(255) NOT NULL,
    "last_name" VARCHAR(255) NOT NULL,
    "email" VARCHAR(255) NOT NULL,
    "phone" VARCHAR(255) NOT NULL,
    "role" VARCHAR(255) CHECK
        ("role" IN ('student', 'teacher')) NOT NULL,
    "dob" DATE NOT NULL,
    "created_at" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL,
    "updated_at" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL
);
ALTER TABLE
    "User" ADD PRIMARY KEY("id");
CREATE INDEX "user_role_index" ON
    "User"("role");
ALTER TABLE
    "Lesson_Completion" ADD CONSTRAINT "lesson_completion_id_foreign" FOREIGN KEY("id") REFERENCES "Student"("id");
ALTER TABLE
    "Courses" ADD CONSTRAINT "courses_teacher_id_foreign" FOREIGN KEY("teacher_id") REFERENCES "Teacher"("id");
ALTER TABLE
    "Teacher" ADD CONSTRAINT "teacher_user_id_foreign" FOREIGN KEY("user_id") REFERENCES "User"("id");
ALTER TABLE
    "Enrollments" ADD CONSTRAINT "enrollments_course_id_foreign" FOREIGN KEY("course_id") REFERENCES "Courses"("id");
ALTER TABLE
    "Lesson_Completion" ADD CONSTRAINT "lesson_completion_lesson_id_foreign" FOREIGN KEY("lesson_id") REFERENCES "Lessons"("id");
ALTER TABLE
    "Student" ADD CONSTRAINT "student_user_id_foreign" FOREIGN KEY("user_id") REFERENCES "User"("id");
ALTER TABLE
    "Lessons" ADD CONSTRAINT "lessons_course_id_foreign" FOREIGN KEY("course_id") REFERENCES "Courses"("id");
ALTER TABLE
    "Enrollments" ADD CONSTRAINT "enrollments_student_id_foreign" FOREIGN KEY("student_id") REFERENCES "Student"("id");