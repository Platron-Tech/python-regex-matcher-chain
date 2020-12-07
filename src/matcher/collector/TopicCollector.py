from src.matcher.collector.AbstractCollector import AbstractCollector
from src.matcher.result.MatchResult import MatchResult


class TopicCollector(AbstractCollector):
    __instance = None

    @staticmethod
    def get_instance():
        if TopicCollector.__instance is None:
            TopicCollector.__instance = TopicCollector()
        return TopicCollector.__instance

    def collect(self, match_result: MatchResult) -> MatchResult:
        """"
            able to do modification, extraction etc. with match result
        """
        match_result.matches = match_result.sentence
        return match_result
