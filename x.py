import traceback

def unbeattable_comparison(a, b):
    try:
        return a>b
    except:
        print(traceback.format_exc())
        return False

print(unbeattable_comparison(1, '1'))

print('программа закончила работу')