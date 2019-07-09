def print_header():
    header = f"CASH RECEIPT" + "\n" + "------------------------------"
    print(header)


def print_body():
    body = "Charged to____________________" + "\n" + "Received by___________________"
    print(body)


def print_footer():
    footer = "------------------------------" + "\n" + "© SoftUni"
    print(footer)


def print_receipt():
    print_header()
    print_body()
    print_footer()

if __name__ == '__main__':

    print_receipt()


