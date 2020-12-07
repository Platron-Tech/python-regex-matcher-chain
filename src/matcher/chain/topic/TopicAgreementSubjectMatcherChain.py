from src.matcher.chain.AbstractMatcherChain import AbstractMatcherChain
from src.matcher.chain.topic.TopicServiceScopeMatcherChain import TopicServiceScopeMatcherChain


class TopicAgreementSubjectMatcherChain(AbstractMatcherChain):
    __pattern = r"(.*?)\ssözleşmenin konusu"
    __instance = None

    @staticmethod
    def get_instance():
        if TopicAgreementSubjectMatcherChain.__instance is None:
            TopicAgreementSubjectMatcherChain.__instance = TopicAgreementSubjectMatcherChain()
        return TopicAgreementSubjectMatcherChain.__instance

    def __init__(self):
        super(TopicAgreementSubjectMatcherChain, self).__init__(self.__pattern)

    def get_next(self):
        return TopicServiceScopeMatcherChain.get_instance()
