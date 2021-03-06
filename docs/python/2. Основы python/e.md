# Циклы

Циклы в питоне позволяют повторять выполнение определенного дейсвтия. В предыдущей главе мы поняли как сделать так, что бы некоторые строки кода не отрабатывали, теперь мы узнаем как сделать так, что бы одна и та же строка отрабатывала несколько раз.

В данной главе будет много примеров кода, сначала нужно подумать что они делают, после чего запустить и проверить. 

Далее нужно попробовать подставить свои числа и модифицировать этот код, что бы лучше понять как работают циклы.

--- 

## Цикл for

Цикл for используется для повторения одного и того же действия несколько раз.


```py
for i in range(10):
    print(i)
```

```py
for i in range(20, 2):
    print(i)
```

```py
for i in range(2, 30, 3):
    print(i)
```

```py
a = 100
for i in range(10, 2, -2):
    print(a)
    a = a - i
```

```py
for x in "banana":
    print(x)
    print("banana")
```

---

## Цикл while

Цикл while позволяет выполнять определенное действие пока действует некоторое условие. Вот примеры:

```py
while True:
    print("stop it plz")
```

```py
a = 10
while a:
    a -= 1
    print(a)
```

---

## continue

Цикл continue приказывает питону перейти к следующей итерации, не дожидаясь выполнения последующей логики.


```py
a = 10
while a != 0:
    if 1%2:
        print(a)
    else:
        continue
    a -= 1
```

---

## break

Данный оператор позволяет остановить выполнение цикла.


```py
a = 20
while a != 0:
    if a == 10:
        break
    print(a)
    a -= 1
```

---

Каждый из представленных выше кусочков кода нужно запустить, модифицировать и хотя бы немного с ним поиграть, подставляя собственные значения.


---

## Интерпретатор

<iframe src="https://trinket.io/embed/python" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>