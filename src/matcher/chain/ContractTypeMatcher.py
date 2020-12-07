from src.matcher.chain.AbstractMatcherChain import AbstractMatcherChain
from src.matcher.chain.contracttype.AnnulmentContractTypeMatcher import AnnulmentContractTypeMatcher
from src.matcher.result.MatchResult import MatchResult


class ContractTypeMatcher(AbstractMatcherChain):
    __first_pattern = '((proje|geliştirme görevleri|uygulama|geliştirme|(yazılım)([\w\s]+)|hizmet([\w\s]+)kapsam)|(anlaşması|sözleşmesi))'
    __last_pattern = '((lisans|satın al[\w]*)[\w\s]+(anlaşması|sözleşmesi)|hizmetlerini yerine getirir)'
    __delimiter = '[\w\s]+'

    __patterns = [
        __first_pattern + __delimiter + __last_pattern,
        __last_pattern + __delimiter + __first_pattern,
    ]
    __instance = None

    @staticmethod
    def get_instance():
        if ContractTypeMatcher.__instance is None:
            ContractTypeMatcher.__instance = ContractTypeMatcher()
        return ContractTypeMatcher.__instance

    def __init__(self):
        super(ContractTypeMatcher, self).__init__(self.__patterns)

    def get_next(self):
        return AnnulmentContractTypeMatcher.get_instance()

    def on_match(self, match_result: MatchResult) -> MatchResult:
        match_result.matches = 'SERVICE-PRODUCT'
        return match_result
