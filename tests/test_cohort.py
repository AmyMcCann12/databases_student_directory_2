from lib.cohort import Cohort

cohort = Cohort(1, "Cohort 1", '2023-10-21')

"""
Cohort constructs with an id, name and starting_date
"""

def test_cohort_constructs():
    assert cohort.id == 1
    assert cohort.name == "Cohort 1"
    assert cohort.starting_date == '2023-10-21'

"""
We can format cohort strings nicely
"""

def test_cohort_formats_nicely():
    assert str(cohort) == "Cohort(1, Cohort 1, 2023-10-21)"

"""
We can comparte two identical cohorts
And have them to be equal
"""

def test_cohorts_are_equal():
    cohort2 = Cohort(1, "Cohort 1", '2023-10-21')
    assert cohort2 == cohort