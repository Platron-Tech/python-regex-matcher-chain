from src.matcher.chain.AbstractMatcherChain import AbstractMatcherChain
from src.matcher.result.MatchResult import MatchResult


class ProductContractTypeMatcher(AbstractMatcherChain):
    __patterns = [
        "(lisans|satın al[\w]*)([\w\s]+)(anlaşması|sözleşmesi)",
        "(satış)[\w\s]+(anlaşması|sözleşmesi)"
    ]
    __instance = None

    @staticmethod
    def get_instance():
        if ProductContractTypeMatcher.__instance is None:
            ProductContractTypeMatcher.__instance = ProductContractTypeMatcher()
        return ProductContractTypeMatcher.__instance

    def __init__(self):
        super(ProductContractTypeMatcher, self).__init__(self.__patterns)

    def get_next(self):
        return None

    def on_match(self, match_result: MatchResult) -> MatchResult:
        match_result.matches = 'PRODUCT'
        return match_result
