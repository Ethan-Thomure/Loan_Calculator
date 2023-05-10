from math import ceil, log


def request_loan_principal():
    return int(input("Enter the loan principal:\n"))


def request_monthly_payment():
    return int(input("Enter the monthly payment:\n"))


def request_number_months():
    return int(input("Enter the number of months\n"))


def request_loan_interest():
    return int(input("Enter the loan interest:\n"))


def calc_number_monthly_payments():
    P = request_loan_principal()
    A = request_monthly_payment()
    i = request_loan_interest() / 120
    return ceil(log(A / (A - i * P), 1 + i))


def calc_monthly_payment():
    P = request_loan_principal()
    n = request_number_months()
    i = request_loan_interest() / 120
    return ceil(P * (i * (1 + i) ** n) / ((1 + i) ** n - 1))


def calc_loan_principal():
    A = request_monthly_payment()
    n = request_number_months()
    i = request_loan_interest() / 120
    return ceil(A / ((i * (1 + i) ** n) / ((1 + i) ** n - 1)))


def add_s(number):
    return 's' if number > 1 else ''


def menu():
    decision = input("""What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for the loan principal:\n""")

    if decision == "n":
        total_months = calc_number_monthly_payments()
        years = total_months // 12
        months = total_months % 12
        print(f"It will take {years} year{add_s(years)} {f'and {months} month{add_s(months)}' if months > 0 else ''}!")

    elif decision == "a":
        print(f"Your monthly payment = {calc_monthly_payment()}!")

    elif decision == "p":
        print(f"Your loan principal = {calc_loan_principal()}")


menu()
