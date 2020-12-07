from abc import ABC, abstractmethod

from src.matcher.result.MatchResult import MatchResult


class AbstractCollector(ABC):

    @abstractmethod
    def collect(self, match_result: MatchResult) -> MatchResult:
        pass
