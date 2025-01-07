from typing import Callable
from abc import ABC, abstractmethod

from chromadb.api.types import EmbeddingFunction

from ..splitters.base import BaseSplitter
from .chunk import Chunk


class BaseChunker(ABC):
    """
    Abstract base class for chunkers.

    To create a custom chunker, implement the ``__call__`` method.
    """

    def __init__(
            self,
            ef: EmbeddingFunction
    ):
        self.ef = ef

    @abstractmethod
    def __call__(self, splits: list[str]) -> list[Chunk]:
        pass

    def __or__(self, other: Callable | BaseSplitter) -> list[Chunk]:
        return self.__call__(other.__call__())
