"""Documentação deste módulo

Ele não faz nada, mas é só um exemplo para você.
Typing -= https://docs.python.org/3/library/typing.html
"""
from typing import Union

x: int = 10
y: float = 10.5
z: bool = False


def funcao(p1: float, p2: str, p3: dict):
    return p1, p2, p3


funcao(10.5, 'Marco', {})
print(funcao(10.4, 'Mariane', {}))


def fun() -> Union[list, dict]:
    return []

