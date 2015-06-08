type pair = int * int;
type point = int * int;
val x: point = (1, 4);
val y: pair = x;
type person = {name: string, age: int};
type school = {name: string, age: int};
val p: person = {name="Alice", age=22};
val s: school = p;
