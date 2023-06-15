def data_popper(args):
    if not args:
        return
    item = args.pop()
    print(item)
    return data_popper(args)

data_popper([1, 2, 3, 5, 6, ])