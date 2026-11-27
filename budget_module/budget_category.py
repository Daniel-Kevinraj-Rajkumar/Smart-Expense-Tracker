
def create_category(categories, category_name):
    try:
        category_name = category_name.strip()

        if category_name == "":
            print("Category name cannot be empty.")

        elif category_name in categories:
            print("Category already exists.")

        else:
            categories.append(category_name)
            print("Category added successfully.")

    except AttributeError:
        print("Please enter a valid category name.")

    return categories


def display_categories(categories):
    if len(categories) == 0:
        print("No categories available.")

    else:
        print("Available Categories:")
        for category in categories:
            print(category)


def set_monthly_budget(budgets, category_name, amount):
    try:
        category_name = category_name.strip()
        amount = float(amount)

        if category_name == "":
            print("Category name cannot be empty.")

        elif amount <= 0:
            print("Budget amount must be greater than zero.")

        else:
            budgets[category_name] = amount
            print("Monthly budget set successfully.")

    except ValueError:
        print("Please enter a valid budget amount.")

    except AttributeError:
        print("Please enter a valid category name.")

    return budgets


def calculate_remaining_budget(budget, spent):
    try:
        budget = float(budget)
        spent = float(spent)

        if budget < 0 or spent < 0:
            print("Budget and spending cannot be negative.")
            return None

        remaining = budget - spent

        if remaining >= 0:
            print("Remaining budget:", remaining)

        else:
            print("Overspending amount:", abs(remaining))

        return remaining

    except (ValueError, TypeError):
        print("Please enter valid numeric values.")
        return None


def check_overspending(budgets, expenses):
    found = False

    for category in budgets:
        try:
            budget = float(budgets[category])
            spent = float(expenses.get(category, 0))

            if budget < 0 or spent < 0:
                print("Invalid amount for category:", category)
                continue

            if spent > budget:
                extra = spent - budget
                print(category, "overspent by:", extra)
                found = True

        except (ValueError, TypeError):
            print("Invalid budget or expense for:", category)

    if found == False:
        print("No overspending detected.")
