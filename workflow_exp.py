def listening_test():
    pass

def reading_test():
    pass

def speaking_test():
    pass

def writing_test():
    pass

def get_to_know():
    pass

def test():
    listening_test_results = listening_test()
    reading_test_results = reading_test()
    speaking_test_results = speaking_test()
    writing_test_results = writing_test()

def prepare_report():
    pass

def prepare_plan():
    pass

def user_decision():
    pass

def get_feedback():
    pass



def main():
    answers = get_to_know()
    test_results = test()
    report = prepare_report(test_results)
    plan = prepare_plan(report, test_results)
    decision = user_decision(plan)
    while decision != "approved":
        feedback = get_feedback()
        plan = prepare_plan(feedback)

    print(f"Proceed with {plan}")