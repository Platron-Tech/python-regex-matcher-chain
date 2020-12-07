from src.matcher.chain.AbstractMatcherChain import AbstractMatcherChain
from src.matcher.result.MatchResult import MatchResult


class AnnulmentContractTypeMatcher(AbstractMatcherChain):
    __pattern = r"(fesih)[\w\s]+(anlaşması|sözleşmesi)"
    __instance = None

    @staticmethod
    def get_instance():
        if AnnulmentContractTypeMatcher.__instance is None:
            AnnulmentContractTypeMatcher.__instance = AnnulmentContractTypeMatcher()
        return AnnulmentContractTypeMatcher.__instance

    def __init__(self):
        super(AnnulmentContractTypeMatcher, self).__init__(self.__pattern)

    def get_next(self):
        return None

    def on_match(self, match_result: MatchResult) -> MatchResult:
        match_result.matches = 'ANNULMENT'
        return match_result
