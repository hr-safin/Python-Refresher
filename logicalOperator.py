#logical operator

has_good_income = False
has_good_credit = True
has_criminal_records = True


if has_good_income and not has_criminal_records:
    print("Eligable for loan")

else:
    print("Not eligable for laon")