DROP TABLE IF EXISTS students;
DROP SEQUENCE IF EXISTS students_id_seq;
DROP TABLE IF EXISTS cohorts;
DROP SEQUENCE IF EXISTS cohorts_id_seq;


-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS cohorts_id_seq;
CREATE TABLE cohorts (
    id SERIAL PRIMARY KEY,
    name text,
    starting_date date
);

CREATE SEQUENCE IF NOT EXISTS students_id_seq;
CREATE TABLE students (
id SERIAL PRIMARY KEY,
  name text,
  cohort_id int,
  constraint fk_cohort foreign key(cohort_id) references cohorts(id) on delete cascade
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO cohorts (name, starting_date) VALUES ('Cohort1', '2023-10-21');
INSERT INTO cohorts (name, starting_date) VALUES ('Cohort2', '2022-10-21');
INSERT INTO cohorts (name, starting_date) VALUES ('Cohort3', '2021-10-21');
INSERT INTO cohorts (name, starting_date) VALUES ('Cohort4', '2020-10-21');

INSERT INTO students (name, cohort_id) VALUES ('Student1', 1);
INSERT INTO students (name, cohort_id) VALUES ('Student2', 2);
INSERT INTO students (name, cohort_id) VALUES ('Student3', 3);
INSERT INTO students (name, cohort_id) VALUES ('Student4', 4);
INSERT INTO students (name, cohort_id) VALUES ('Student5', 2);
INSERT INTO students (name, cohort_id) VALUES ('Student6', 1);
INSERT INTO students (name, cohort_id) VALUES ('Student7', 3);
INSERT INTO students (name, cohort_id) VALUES ('Student8', 3);
INSERT INTO students (name, cohort_id) VALUES ('Student9', 4);
INSERT INTO students (name, cohort_id) VALUES ('Student10', 3);