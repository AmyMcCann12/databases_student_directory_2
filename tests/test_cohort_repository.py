from lib.cohort_repository import CohortRepository
from lib.cohort import Cohort
from lib.student import Student
import datetime

"""
When we call CohortRepository#all
We get a list of Cohort objects reflecting the seed data
"""

def test_get_all_records(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repository = CohortRepository(db_connection)
    cohorts = repository.all()
    assert cohorts == [
        Cohort(1,'Cohort1', datetime.date(2023,10,21)),
        Cohort(2,'Cohort2', datetime.date(2022,10,21)),
        Cohort(3,'Cohort3', datetime.date(2021,10,21)),
        Cohort(4,'Cohort4', datetime.date(2020,10,21)),
    ]

"""
When we call CohortRepository#find
We get a single Cohort object reflecting the seed data
"""

def test_find_single_cohort(db_connection):
    db_connection.seed('seeds/student_directory_2.sql')
    repository = CohortRepository(db_connection)
    cohort = repository.find(2)
    assert cohort == Cohort(2, 'Cohort2', datetime.date(2022,10,21))

"""
When we call CohortRepository#create
We get a new record in the database.
"""

def test_create_record(db_connection):
    db_connection.seed('seeds/student_directory_2.sql')
    repository = CohortRepository(db_connection)

    repository.create(Cohort(None, "Cohort5", '2000-12-12'))

    result = repository.all()
    assert result == [
        Cohort(1,'Cohort1', datetime.date(2023,10,21)),
        Cohort(2,'Cohort2', datetime.date(2022,10,21)),
        Cohort(3,'Cohort3', datetime.date(2021,10,21)),
        Cohort(4,'Cohort4', datetime.date(2020,10,21)),
        Cohort(5,'Cohort5', datetime.date(2000,12,12))
    ]

"""
When we call CohortRepository#delete
We remove a record from the database.
"""

def test_delete_record(db_connection):
    db_connection.seed('seeds/student_directory_2.sql')
    repository = CohortRepository(db_connection)
    repository.delete(3)
    result = repository.all()
    assert result == [
        Cohort(1,'Cohort1', datetime.date(2023,10,21)),
        Cohort(2,'Cohort2', datetime.date(2022,10,21)),
        Cohort(4,'Cohort4', datetime.date(2020,10,21)) 
    ]

"""
When I call #find_with_students with an cohort id
Then I get the cohort with a list of their students, populated
"""

def test_find_with_students(db_connection):
    db_connection.seed('seeds/student_directory_2.sql')
    repository = CohortRepository(db_connection)
    result = repository.find_with_students(2)
    assert result == Cohort(2, 'Cohort2', datetime.date(2022,10,21), [
        Student(2, 'Student2', 2),
        Student(5, 'Student5', 2)
    ])