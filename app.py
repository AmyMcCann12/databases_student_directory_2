from lib.database_connection import DatabaseConnection
from lib.cohort_repository import CohortRepository

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/student_directory_2.sql")

    def run(self):
        cohort = CohortRepository(self._connection)
        result = cohort.find_with_students(4)
        print(f"Cohort ID: {result.id} \nCohort Name: {result.name}\nCohort Start Date: {result.starting_date}\nStudents: {result.students}")

if __name__ == '__main__':
    app = Application()
    app.run()