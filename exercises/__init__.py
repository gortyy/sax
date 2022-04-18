from abc import ABC, abstractmethod
from typing import Protocol, TypeAlias


Question: TypeAlias = str
Answer: TypeAlias = str


class Exercise(Protocol):
    def __call__(self) -> tuple[Question, Answer]:
        ...
