# Revision

:x: Éxécuter Python

```
$ python monprogramme.py
```

:o: Big O Notation

<img src="images/bigO.png" width="580" height="341"></img>


:a: Structures

<img src="images/Structures.png" width="580" height="341"></img>


:one: Structure de donnees

* Variable

```
>>> x = 5
```

* Tuple

```
>>> x = ( 5, 'Oriane')
```

* Unpacking (Affectation multiple)

```
>>>  age, prenom = x
```

```
>>> l = [ x for x in range(10)]
>>> h, *t = l
```

```
>>> { 4, 3, 8, 4, 9, 4, 5, 1}
{1, 3, 4, 5, 8, 9}
```

:two: Structure de controle

* Recursive Case

```python
>>> def loop(x):
...    loop(x)
...
>>> loop(10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in loop
  File "<stdin>", line 2, in loop
  File "<stdin>", line 2, in loop
  [Previous line repeated 996 more times]
RecursionError: maximum recursion depth exceeded
```

* Base Case

```
Condition qui arrete la recursion
```

* Anonymous function

```
>>> list(map(lambda x: x * 2, [x for x in range(10)]))
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
>>> set(map(lambda x: x * 2, [x for x in range(10)]))
{0, 2, 4, 6, 8, 10, 12, 14, 16, 18}
```
