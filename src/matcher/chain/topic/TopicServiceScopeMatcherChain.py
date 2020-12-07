from src.matcher.chain.AbstractMatcherChain import AbstractMatcherChain


class TopicServiceScopeMatcherChain(AbstractMatcherChain):
    __pattern = r"(.*?)\s(hizmet kapsamındadır)"
    __instance = None

    @staticmethod
    def get_instance():
        if TopicServiceScopeMatcherChain.__instance is None:
            TopicServiceScopeMatcherChain.__instance = TopicServiceScopeMatcherChain()
        return TopicServiceScopeMatcherChain.__instance

    def __init__(self):
        super(TopicServiceScopeMatcherChain, self).__init__(self.__pattern)

    def get_next(self):
        return None
