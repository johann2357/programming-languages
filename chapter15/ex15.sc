; Write a Scheme function that takes a list as a parameter and returns a
; list identical to the parameter list except with the second top-level ele-
; ment removed. If the given list does not have two elements, the function
; should return ().

; cons build pairs, not lists.
; car yields the first element of a list
; cdr yields the list without the first element

(define (length list)
    (if (null? list)
       0
       (+ 1 (length (cdr list)))
    )
)

(define (delete list)
    (cond
        ((< (length list) 2) '())
        (else
            (cons 
                (car list)
                (cdr (cdr list))
            )
        )
    )
)

(display (delete '(1 (2  3 4) 5 6 7 8)))
(newline) 
