import dis

# 3x3 matrix
x = [
    [1, 7, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# 3x4 matrix
y = [
    [5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]
]
# result is 3x4
result = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]


def test():
    for i in xrange(len(x)):
        for j in xrange(len(y[0])):
            for k in xrange(len(y)):
                result[i][j] += x[i][k] * y[k][j]


if __name__ == "__main__":
    test()
    for r in result:
        print r

    print "\n Disassembler:"
    dis.dis(test)

"""
Segun el output mostrado abajo, se puede ver que cuando se quiere
accesar a algun elemento de una lista se llama a BINARY_SUBSCR que
implementa `TOS = TOS1[TOS]`, cuya implementacion es la siguiente:
        ...
        case BINARY_SUBSCR:
            w = POP();
            v = TOP();
            if (PyList_CheckExact(v) && PyInt_CheckExact(w)) {
                /* INLINE: list[int] */
                Py_ssize_t i = PyInt_AsSsize_t(w);
                if (i < 0)
                    i += PyList_GET_SIZE(v);
                if (i >= 0 && i < PyList_GET_SIZE(v)) {
                    x = PyList_GET_ITEM(v, i);
                    Py_INCREF(x);
                }
                else
                    goto slow_get;
            }
            else
                slow_get:
                x = PyObject_GetItem(v, w);
            Py_DECREF(v);
            Py_DECREF(w);
            SET_TOP(x);
            if (x != NULL) continue;
            break;
        ...
        ...
            PyObject *
            PyList_GetItem(PyObject *op, Py_ssize_t i)
            {
                if (!PyList_Check(op)) {
                    PyErr_BadInternalCall();
                    return NULL;
                }
                if (i < 0 || i >= Py_SIZE(op)) {
                    if (indexerr == NULL) {
                        indexerr = PyUnicode_FromString(
                            "list index out of range");
                        if (indexerr == NULL)
                            return NULL;
                    }
                    PyErr_SetObject(PyExc_IndexError, indexerr);
                    return NULL;
                }
                return ((PyListObject *)op) -> ob_item[i];
            }
        ...

La comparacion del segundo if de PyList_GetItem en assembler es la siguiente:
_list_item:
    subq    $8, %rsp
    testq   %rsi, %rsi
    js  L227
    cmpq    16(%rdi), %rsi
    jl  L228
L227:
    ... <error reporting and exit > ...
L228:
    movq    24(%rdi), %rax
    movq    (%rax,%rsi,8), %rax
    addq    $1, (%rax)
    addq    $8, %rsp
    ret

Se puede ver que se chequea cada vez si es que es un indice valido,
esto brinda una mayor seguridad, sin embargo esto requiere un par de
comparaciones mas lo cual hace que sea un poco mas lento. En C o C++
al no haber esto, simplemente se accede al elemento siendo mas rapido, pero
mas inseguro.

OUTPUT:
[59, 72, 49, 5]
[74, 97, 73, 14]
[119, 157, 112, 23]

Disassembler:
 24           0 SETUP_LOOP             128 (to 131)
              3 LOAD_GLOBAL              0 (xrange)
              6 LOAD_GLOBAL              1 (len)
              9 LOAD_GLOBAL              2 (x)
             12 CALL_FUNCTION            1
             15 CALL_FUNCTION            1
             18 GET_ITER            
        >>   19 FOR_ITER               108 (to 130)
             22 STORE_FAST               0 (i)

 25          25 SETUP_LOOP              99 (to 127)
             28 LOAD_GLOBAL              0 (xrange)
             31 LOAD_GLOBAL              1 (len)
             34 LOAD_GLOBAL              3 (y)
             37 LOAD_CONST               1 (0)
             40 BINARY_SUBSCR       
             41 CALL_FUNCTION            1
             44 CALL_FUNCTION            1
             47 GET_ITER            
        >>   48 FOR_ITER                75 (to 126)
             51 STORE_FAST               1 (j)

 26          54 SETUP_LOOP              66 (to 123)
             57 LOAD_GLOBAL              0 (xrange)
             60 LOAD_GLOBAL              1 (len)
             63 LOAD_GLOBAL              3 (y)
             66 CALL_FUNCTION            1
             69 CALL_FUNCTION            1
             72 GET_ITER            
        >>   73 FOR_ITER                46 (to 122)
             76 STORE_FAST               2 (k)

 27          79 LOAD_GLOBAL              4 (result)
             82 LOAD_FAST                0 (i)
             85 BINARY_SUBSCR       
             86 LOAD_FAST                1 (j)
             89 DUP_TOPX                 2
             92 BINARY_SUBSCR       
             93 LOAD_GLOBAL              2 (x)
             96 LOAD_FAST                0 (i)
             99 BINARY_SUBSCR       
            100 LOAD_FAST                2 (k)
            103 BINARY_SUBSCR       
            104 LOAD_GLOBAL              3 (y)
            107 LOAD_FAST                2 (k)
            110 BINARY_SUBSCR       
            111 LOAD_FAST                1 (j)
            114 BINARY_SUBSCR       
            115 BINARY_MULTIPLY     
            116 INPLACE_ADD         
            117 ROT_THREE           
            118 STORE_SUBSCR        
            119 JUMP_ABSOLUTE           73
        >>  122 POP_BLOCK           
        >>  123 JUMP_ABSOLUTE           48
        >>  126 POP_BLOCK           
        >>  127 JUMP_ABSOLUTE           19
        >>  130 POP_BLOCK           
        >>  131 LOAD_CONST               0 (None)
            134 RETURN_VALUE        
"""
