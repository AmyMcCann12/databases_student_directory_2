from lib.cohort import Cohort
from lib.student import Student

class CohortRepository():
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * FROM cohorts')
        cohorts = []
        for row in rows:
            item = Cohort(row['id'], row['name'], row['starting_date'])
            cohorts.append(item)
        print(cohorts)
        return cohorts
    
    def find(self, cohort_id):
        rows = self._connection.execute('SELECT * FROM cohorts WHERE id = %s', [cohort_id])
        row = rows[0]
        return Cohort(row['id'], row['name'], row['starting_date'])
    
    def find_with_students(self, cohort_id):
        rows = self._connection.execute("""SELECT cohorts.id AS cohort_id, 
                                        cohorts.name AS cohort_name, 
                                        cohorts.starting_date, 
                                        students.id, 
                                        students.name AS student_name, 
                                        students.cohort_id 
                                        FROM cohorts 
                                        JOIN students 
                                        ON cohorts.id = students.cohort_id 
                                        WHERE cohorts.id = %s""", [cohort_id])
        students = []
        for row in rows:
            student = Student(row['id'], row['student_name'], row['cohort_id'])
            students.append(student)
        cohort = Cohort(rows[0]['cohort_id'], rows[0]['cohort_name'], rows[0]['starting_date'], students)
        return cohort
    
    def create(self, cohort):
        self._connection.execute('INSERT INTO cohorts (name, starting_date) VALUES (%s, %s)', [cohort.name, cohort.starting_date])
        return None
    
    def delete(self, cohort_id):
        self._connection.execute('DELETE FROM cohorts WHERE id = %s', [cohort_id])
        return None
    
