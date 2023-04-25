list = 'abcsdsdsdsdsd abcsdsdsdsdsd abcsdsdsdsdsd abcsdsdsdsdsd abcsdsdsdsdsd abcsdsdsdsdsd abcsdsdsdsdsd abcsdsdsdsdsd abcsdsdsdsdsd abcsdsdsdsdsd abcsdsdsdsdsd'

a = list.split()

if (n := len(a)) > 10:
    print(f"List is too long ({n} elements, expected <= 10)")

    # Walrus saves lines of code, if not using it we'll need to do a line defining n = len(a))