def check_eligibility(age, has_degree):
    if age<18:
        print("You're too young to apply")
    elif age>=18 and has_degree:
        print("Eligible for a job")

    elif age>18 and not has_degree:
        print("Need a degree to be eligible")

check_eligibility(19, True)
check_eligibility(20, False)
check_eligibility(16, True)
