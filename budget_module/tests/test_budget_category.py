
import pytest

from budget_module.budget_category import (
    create_category,
    display_categories,
    set_monthly_budget,
    calculate_remaining_budget,
    check_overspending
)


def test_create_category():
    categories = []
    create_category(categories, "Food")
    assert "Food" in categories


def test_duplicate_category():
    categories = ["Food"]
    create_category(categories, "Food")
    assert categories.count("Food") == 1


def test_empty_category():
    categories = []
    create_category(categories, "   ")
    assert len(categories) == 0


def test_set_monthly_budget():
    budgets = {}
    set_monthly_budget(budgets, "Food", 3000)
    assert budgets["Food"] == 3000


def test_invalid_budget():
    budgets = {}
    set_monthly_budget(budgets, "Food", -500)
    assert "Food" not in budgets


def test_invalid_budget_text():
    budgets = {}
    set_monthly_budget(budgets, "Food", "abc")
    assert "Food" not in budgets


def test_remaining_budget():
    result = calculate_remaining_budget(3000, 1200)
    assert result == 1800


def test_overspending_calculation():
    result = calculate_remaining_budget(3000, 3500)
    assert result == -500


def test_negative_spending():
    result = calculate_remaining_budget(3000, -100)
    assert result is None


def test_check_overspending(capsys):
    budgets = {"Food": 3000, "Travel": 2000}
    expenses = {"Food": 3500, "Travel": 1000}

    check_overspending(budgets, expenses)

    output = capsys.readouterr()
    assert "Food overspent by: 500.0" in output.out


def test_no_overspending(capsys):
    budgets = {"Food": 3000}
    expenses = {"Food": 2000}

    check_overspending(budgets, expenses)

    output = capsys.readouterr()
    assert "No overspending detected." in output.out
