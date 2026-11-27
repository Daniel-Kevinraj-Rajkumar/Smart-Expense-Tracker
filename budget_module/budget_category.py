
def create_category(categories, category_name):
    category_name = category_name.strip()

    if category_name == "":
        print("Category name cannot be empty.")

    elif category_name in categories:
        print("Category already exists.")

    else:
        categories.append(category_name)
        print("Category added successfully.")

    return categories


def display_categories(categories):
    if len(categories) == 0:
        print("No categories available.")

    else:
        print("Available Categories:")
        for category in categories:
            print(category)


def set_monthly_budget(budgets, category_name, amount):
    if amount <= 0:
        print("Budget amount must be greater than zero.")

    else:
        budgets[category_name] = amount
        print("Monthly budget set successfully.")

    return budgets


def calculate_remaining_budget(budget, spent):
    remaining = budget - spent

    if remaining >= 0:
        print("Remaining budget:", remaining)

    else:
        print("Overspending amount:", abs(remaining))

    return remaining

def check_overspending(budgets, expenses):
    found = False

    for category in budgets:
        spent = expenses.get(category, 0)

        if spent > budgets[category]:
            extra = spent - budgets[category]
            print(category, "overspent by:", extra)
            found = True

    if found == False:
        print("No overspending detected.")
