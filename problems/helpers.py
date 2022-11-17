
def comparator(*func, inpt):
    """
    Compare two functions given the same input and returns metrics based on the performance
    :param func:
    :param inpt:
    :return:
    """
    summary = dict()
    for f in func:
        # Run function
        start = time.time()
        f(*inpt)
        end = time.time()

        # Calculate summary
        total = end -start
        summary[f.__name__] = total

        # Get best function
    best_f = min(summary, key=summary.get)
    difference = round(sorted(summary.values())[1] - summary[best_f], 2)
    print(f"The fastest function is {best_f} it took {difference} seconds less than the second best.\n")
    for k, v in summary.items():
        print(f"{k}: {v}")