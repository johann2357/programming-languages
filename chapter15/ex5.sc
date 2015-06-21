; Write a Scheme function that returns the number of zeros in a given
; simple list of numbers.

;cdr yields the list without the first element
(define (length list)
    (if (null? list)
       0
       (+ 1 (length (cdr list)))
    )
)
(display (length '(a b c d e f g h)))
(newline) 
