; Rewrite the following Scheme function as a tail-recursive function:

(define (doitoriginal n)
    (if (= n 0)
        0
        (+ n (doitoriginal (- n 1)))
    )
)
(display (doitoriginal 19))
(newline)

(define (doit n acc)
    (if (= n 0)
        acc
        (doit (- n 1) (+ n acc))
    )
)
(display (doit 19 0))
(newline)
