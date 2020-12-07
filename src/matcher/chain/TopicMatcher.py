from src.matcher.chain.AbstractMatcherChain import AbstractMatcherChain
from src.matcher.chain.topic.TopicAgreementSubjectMatcherChain import TopicAgreementSubjectMatcherChain
from src.matcher.collector.TopicCollector import TopicCollector


class TopicMatcher(AbstractMatcherChain):
    __pattern = r"(.*?)\s((hizmet[\w]*)\s(vermek))"

    __instance = None

    @staticmethod
    def get_instance():
        if TopicMatcher.__instance is None:
            TopicMatcher.__instance = TopicMatcher()
        return TopicMatcher.__instance

    def __init__(self):
        super(TopicMatcher, self).__init__(self.__pattern)
        super().register_collector(TopicCollector())

    def get_next(self):
        return TopicAgreementSubjectMatcherChain.get_instance()
