def the_glue(*args, glue=':'):
    args3 = str()
    for item in args:
        if len(item) == 3:
            args3 += item + glue 
    print(args3[:-1])
            

the_glue('123', 'asd', 'fffh', '53g')


