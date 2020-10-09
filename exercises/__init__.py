from abc import ABC, abstractmethod
from typing import Tuple

from exercises.types import Question, Answer


class Exercise(ABC):
    @abstractmethod
    def __call__(self) -> Tuple[Question, Answer]:
        pass
