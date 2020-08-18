# old code
def print_owing(invoice):
    out_standing = {"customer": "john", "amount": 100}

    print(out_standing.get("customer"))
    print(out_standing.get('account'))


# new code
def new_print_owing():
    out_standing = {"customer": "john", "amount": 100}
    print_detail(out_standing)


def print_detail(out_standing):
    print(out_standing.get("customer"))
    print(out_standing.get('account'))
