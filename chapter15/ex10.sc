; Write a Scheme function that takes two atoms and a list as parameters
; and returns a list identical to the parameter list except all occurrences of
; the first given atom in the list are replaced with the second given atom,
; no matter how deeply the first atom is nested.

; cons build pairs, not lists.
; car yields the first element of a list
; cdr yields the list without the first element
(define (find-replace a b list)
    (cond
        ; if it is empty, leave it
        ((null? list) '())
        ; if it is a list then call the function recursively
        (
            (list? (car list))
            (cons
                (find-replace a b (car list))
                (find-replace a b (cdr list))
            )
        )
        ; if the first element i the old value
        ; add the new value and call recursively the rest of the list
        (
            (eq? (car list) a)
            (cons b (find-replace a b (cdr list)))
        )
        ; else just add the element and keep searching recursively
        (else
            (cons
                (car list)
                (find-replace a b (cdr list))
            )
        )
    )
)
(display (find-replace 4 8 '(1 2 (2 3 4 (3 4 5)) 4 5 6)))
(newline) 
