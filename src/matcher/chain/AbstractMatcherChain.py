import re
from abc import ABC, abstractmethod

from src.matcher.collector.AbstractCollector import AbstractCollector
from src.matcher.result.MatchResult import MatchResult
from src.matcher.util.MatcherUtils import MatcherUtils


class AbstractMatcherChain(ABC):
    __collector = None

    def __init__(self, pattern):
        self.__compile_patterns(pattern)

    def __compile_patterns(self, patterns):
        self.__patterns = list()

        if isinstance(patterns, list):
            for pattern in patterns:
                pattern = MatcherUtils.expand(pattern)
                self.__patterns.append(re.compile(pattern, flags=re.MULTILINE | re.IGNORECASE))
        else:
            patterns = MatcherUtils.expand(patterns)
            self.__patterns.append(re.compile(patterns, flags=re.MULTILINE | re.IGNORECASE))

    def match_iterable(self, text) -> MatchResult:
        sentences = MatcherUtils.tokenize_sentences(text)
        for sentence in sentences:
            match_result = self.match(sentence)
            if match_result.is_matched():
                return match_result

        return MatchResult()

    def match(self, sentence) -> MatchResult:

        for pattern in self.__patterns:
            match_result = pattern.findall(sentence)

            if match_result:
                match_groups = pattern.search(sentence)
                return self.on_match(MatchResult(sentence, match_result, match_groups))

        _next = self.__get_next()
        if _next is not None:
            return _next.match(sentence)

        return MatchResult()

    def __get_next(self):
        _next = self.get_next()
        if _next is None:
            return None

        if self.__collector is not None:
            _next.register_collector(self.__collector)

        return _next

    def on_match(self, match_result: MatchResult) -> MatchResult:
        if self.__collector is None:
            return match_result

        return self.__collector.collect(match_result)

    def register_collector(self, collector: AbstractCollector):
        self.__collector = collector

    @abstractmethod
    def get_next(self):
        pass
