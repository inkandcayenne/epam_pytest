import pyodbc
import pytest
from datetime import date


def connect_to_db():
    """function to connect to local database. Function uses DSN name EPGETBIW0395 in the system and logins under
    testuser return cursor which should be used in queries to DB """
    conn = pyodbc.connect(
        'DSN=EPGETBIW0395;UID=testuser;PWD=TestPassword!;Trusted_Connection=yes;TrustServerCertificate'
        '=yes;DATABASE=TRN')
    cursor = conn.cursor()
    return cursor


def get_result_by_percentage(corrupted_records_amount: int, overall_records_amount: int, description: str):
    """logger function: returns description of a test and reports failed logs vs total logs"""
    if corrupted_records_amount == 0:
        print(f'test failed, {description}: {corrupted_records_amount} out of {overall_records_amount} are wrong')
    else:
        print(f'{description} test passed')


@pytest.fixture
def test_future_dates(cursor_n=connect_to_db()):
    """function checks if employee's hire date is not in the future
    returns counter - count of total rows, records_amount_with_future_values - count of wrong rows
    source: EPGETBIW0395, table hr.employees, field: hire_Date
    checking rules: checking accuracy by validating hire_date<today's date
    algorythm: select * from hr.employees where hire > today
    expected result: records_amount_with_future_values = 0
    """
    cursor_n.execute("""
                       select *
                         from hr.employees
                        """)
    rows = cursor_n.fetchall()
    records_amount_with_future_values = 0
    counter = 0
    for row in rows:
        counter += 1
        if row.hire_date > date.today():
            records_amount_with_future_values += 1
        else:
            pass
    assert records_amount_with_future_values == 0
    return get_result_by_percentage(records_amount_with_future_values, counter,
                                    "employees' hire date is not in the future")


@pytest.fixture
def test_allowed_values(cursor_n=connect_to_db(), allowed_values=(i for i in range(1, 12))):
    """function checks if employee's department is in the range of allowed values (from 1 to 11)
    returns counter - count of total rows, records_amount_with_wrong_department - count of wrong rows
    source: EPGETBIW0395, table hr.employees, field: department_id
    checking rules: checking validity by verifying department_id is in range from 1 to 11
    algorythm: select * from hr.employees where department_id is not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
    expected result: records_amount_with_wrong_department = 0
    """
    cursor_n.execute("""
                       select distinct department_id
                         from hr.employees
                        """)
    rows = cursor_n.fetchall()
    records_amount_with_wrong_department = 0
    counter = 0
    for row in rows:
        counter += 1
        if row.department_id in allowed_values:
            records_amount_with_wrong_department += 1
        else:
            pass
    assert records_amount_with_wrong_department == 0
    return get_result_by_percentage(records_amount_with_wrong_department, counter,
                                    f"employees' department is in the list of allowed values {allowed_values}")


@pytest.fixture
def test_country_length(cursor_n=connect_to_db()):
    """function checks if country's id format is only 2 characters long
    returns counter - count of total rows, records_amount_with_wrong_country_id - count of wrong rows
    source: EPGETBIW0395, table hr.countries, field: country_id
    checking rules: checking validity by verifying country_id in in the right format: only 2 characters long
    algorythm: select * from hr.countries where len(country_id) <> 2
    expected result: records_amount_with_wrong_country_id = 0"""
    cursor_n.execute("""
                    select country_id
                    from hr.countries
                    """)
    rows = cursor_n.fetchall()
    records_amount_with_wrong_country_id = 0
    counter = 0
    for row in rows:
        counter += 1
        if len(row.country_id) != 2:
            records_amount_with_wrong_country_id += 1
        else:
            pass
    assert records_amount_with_wrong_country_id == 0
    return get_result_by_percentage(records_amount_with_wrong_country_id, counter,
                                    f"country_id field is 2 characters long")


@pytest.fixture
def test_postal_codes(cursor_n=connect_to_db()):
    """function checks if postal codes are not empty
    returns counter - count of total rows, empty_postal_codes - count of wrong rows
    source: EPGETBIW0395, table hr.locations, field: postal_code
    checking rules: checking completeness by verifying postal_code is filled in
    algorythm: select * from hr.locations where postal_code is null
    expected result: empty_postal_codes = 0"""
    cursor_n.execute("""
                    select postal_code
                    from hr.locations
                    """)
    rows = cursor_n.fetchall()
    empty_postal_codes = 0
    counter = 0
    for row in rows:
        counter += 1
        if row.postal_code is None:
            empty_postal_codes += 1
        else:
            pass
    assert empty_postal_codes == 0
    return get_result_by_percentage(empty_postal_codes, counter,
                                    f"postal codes are not empty")


@pytest.fixture
def test_country_uniqueness(cursor_n=connect_to_db()):
    """function checks if countries are unique
    returns counter - count of total rows, non_unique_countries - count of wrong rows
    source: EPGETBIW0395, table hr.countries, field: country_name
    checking rules: checking uniqueness by verifying country_name is unique
    algorythm: select country_name, count(*) from hr.countries group by country_name having count(*) > 1
    expected result: non_unique_countries = 0"""
    cursor_n.execute("""
                    select country_name, count(*) as counts
                    from hr.countries
                    group by country_name
                    """)
    rows = cursor_n.fetchall()
    non_unique_countries = 0
    counter = 0
    for row in rows:
        counter += 1
        if row.counts > 1:
            non_unique_countries += 1
        else:
            pass
    assert non_unique_countries == 0
    return get_result_by_percentage(non_unique_countries, counter,
                                    f"countries are unique")


@pytest.fixture
def test_min_max_salary(cursor_n=connect_to_db()):
    """function checks if minimal employees' salary is actually less than maximum salary
    returns counter - count of total rows, incorrect_salary_range - count of wrong rows
    source: EPGETBIW0395, table hr.jobs, field: min_salary, max_salary
    checking rules: checking consistensy by verifying stated salary range: min_salary < max_salary
    algorythm: select min_salary, max_salary from hr.jobs where min_salary < max_salary
    expected result: incorrect_salary_range = 0"""
    cursor_n.execute("""
                    select min_salary, max_salary
                    from hr.jobs
                    """)
    rows = cursor_n.fetchall()
    incorrect_salary_range = 0
    counter = 0
    for row in rows:
        counter += 1
        if row.min_salary <= row.max_salary:
            incorrect_salary_range += 1
        else:
            pass
    assert incorrect_salary_range == 0
    return get_result_by_percentage(incorrect_salary_range, counter,
                                    f"correct salary range")