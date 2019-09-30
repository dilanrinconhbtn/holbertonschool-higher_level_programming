def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except Exception as error:
        sys.stderr.write("Exception: " + str(error) + "\n")
        return False
