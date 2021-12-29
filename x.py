def unbeattable_comparison(a, b):
    try:
        return a>b
    except Exception:
        print('Что ты сравниваешь>??' + Exception)
        return False

print(unbeattable_comparison(1, '1'))