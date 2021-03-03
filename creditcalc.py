import argparse
import math

blanks = 0
negative = 0
over = 0


# Defining functions
def number_of_periods(pay, inter, pr):
    n_i = inter / 1200
    n = math.ceil(math.log(pay / (pay - n_i * pr), 1 + n_i))
    if n < 12:
        return f"It will take {n} month{'s' if n > 1 else ''} to repay this loan!", n
    elif n % 12 == 0:
        return f"It will take {n // 12} year{'s' if n // 12 > 1 else ''} to repay the loan!", n
    else:
        return f"It will take {n // 12} year{'s' if n // 12 > 1 else ''} " \
               f"and {n - 12 * (n // 12)} month{'s' if n > 1 else ''} to repay the loan!", n


def monthly_payment(pr, per, inter):
    m_i = inter / 1200
    p = math.ceil(pr * ((m_i * math.pow(1 + m_i, per)) / (math.pow(1 + m_i, per) - 1)))
    return f"Your monthly payment = {p}!", p


def loan_principal(pay, per, inter):
    l_i = inter / 1200
    pr = int((pay / ((l_i * math.pow((1 + l_i), per)) / (math.pow((1 + l_i), per) - 1))))  # int instead round???
    return f"Your loan principal = {pr}!", pr


def diff_payment(pr, inter, per):
    d_i = inter / 1200
    m = 0
    total = 0
    values = []
    for _ in range(int(per)):
        m += 1
        total += math.ceil(pr / per + (d_i * (pr - (pr * (m - 1)) / per)))
        values.append(f"Month {m}: payment is " + str(math.ceil(pr / per + (d_i * (pr - (pr * (m - 1)) / per)))))
    return values, total


# Parsing arguments
parser = argparse.ArgumentParser(description="Loan calculator with different types of payment")
parser.add_argument("-t", "--type", help="type of payment")
parser.add_argument("-pay", "--payment", help="monthly payment amount", type=float)
parser.add_argument("-pr", "--principal", help="loan principal", type=float)
parser.add_argument("-per", "--periods", help="number of months needed to repay the loan", type=float)
parser.add_argument("-i", "--interest", help="interest rate", type=float)
args = parser.parse_args()

for i in vars(args).values():
    if i is None:
        blanks += 1
    for x in str(i):
        if x == "-":
            negative += 1

# Handling of invalid parameters
if args.type != "annuity" and args.type != "diff" or \
        args.type == "diff" and args.principal is None or \
        args.type == "diff" and args.periods is None or \
        args.interest is None or \
        blanks > 1 or \
        negative > 0:
    print("Incorrect parameters")

# Counting
else:
    if args.type == "annuity":
        if args.periods is None:
            print(number_of_periods(args.payment, args.interest, args.principal)[0])
            over = args.payment * number_of_periods(args.payment, args.interest, args.principal)[1] - args.principal
        elif args.payment is None:
            print(monthly_payment(args.principal, args.periods, args.interest)[0])
            over = int(monthly_payment(args.principal, args.periods, args.interest)[1]) * args.periods - args.principal
        else:
            print(loan_principal(args.payment, args.periods, args.interest)[0])
            over = args.payment * args.periods - loan_principal(args.payment, args.periods, args.interest)[1]
    else:
        for i in diff_payment(args.principal, args.interest, args.periods)[0]:
            print(i)
        over = diff_payment(args.principal, args.interest, args.periods)[1] - args.principal
    print("Overpayment =", int(over))
