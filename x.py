import os
import shutil

import pika
import requests

print(1)
print('вася')
print(True)

class Duck:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Я утка по имени ' + self.name

print(Duck('cola'))
