# Try/Except блоки

Очень полезная конструкция, которая позволяет программе `не умирать`, когда вылетает ошибка.

Что бы её использовать, нужно обернуть тот участок кода который может вызвать ошибку в данную конструкцию.

Например:

```python
def unbeattable_comparison(a, b):
    try:
        return a>b
    except:
        print('Какой то больной псих сравнивает несравнимое, вызывайте копов!!')
        return False

print(unbeattable_comparison(1, '1'))
```

С такой функцией можно сравнивать хоть лопаты с магазинами (хотя я всё равно настоятельно не рекомендую так делать), она всё равно выдержит.

---

## Обрабатываем ошибки

Вообще, конструкцию try/except лучше не вызывать, если нет возможности обработать ошибку должным образом. В противном случае лучше вообще не использовать эту конструкцию и предоставить возможность обработать ошибку на более высоком уровне абстракции.


```python
import traceback

def unbeattable_comparison(a, b):
    try:
        return a>b
    except:
        print(traceback.format_exc())
        return False

print(unbeattable_comparison(1, '1'))

print('программа закончила работу без траблов :D')
```


---

## Интерпретатор

<iframe src="https://trinket.io/embed/python" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>