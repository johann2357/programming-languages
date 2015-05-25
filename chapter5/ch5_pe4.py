def subprogram1():
    svar1 = 0
    svar1 += 1

    def subprogram2():
        nonlocal svar1
        svar2 = 0
        svar1 += 1
        svar2 += 1

        def subprogram3():
            nonlocal svar1
            nonlocal svar2
            svar3 = 0
            svar1 += 1
            svar2 += 1
            svar3 += 1
            print(svar1)
            print(svar2)
            print(svar3)

        subprogram3()

    subprogram2()
