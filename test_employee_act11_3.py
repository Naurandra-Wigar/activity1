import pytest
from employee import Employee


@pytest.fixture
def employee():
    """Karyawan yang dipakai oleh semua test."""
    return Employee("Budi", "Santoso", 60000)


def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.annual_salary == 65000


def test_give_custom_raise(employee):
    employee.give_raise(10000)
    assert employee.annual_salary == 70000