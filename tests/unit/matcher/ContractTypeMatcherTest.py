import unittest

from src.matcher.chain.ContractTypeMatcher import ContractTypeMatcher


class ContractTypeMatcherTest(unittest.TestCase):
    __matcher = ContractTypeMatcher.get_instance()

    def testContractType_shouldFindAnnulmentContract(self):
        text = 'falan falan fesih ohbıojb ıbıj sözleşmesi.'
        match_result = self.__matcher.match_iterable(text)
        self.assertEqual('ANNULMENT', match_result.matches)
        self.assertEqual('falan falan fesih ohbıojb ıbıj sözleşmesi.', match_result.sentence)

    def testContractType_shouldFindServiceProductContract(self):
        text3 = 'falan filan proje sözleşmesi ıjnj ınj satın alımı sözleşmesi.'
        text4 = 'falan filan danışmanlık sözleşmesi ıjnj ınj satın alımı sözleşmesi.'
        text5 = 'falan filan ubuh hizmetlerini yerine getirir ubh satın alımı anlaşması.'

        match_result3 = self.__matcher.match_iterable(text3)
        match_result4 = self.__matcher.match_iterable(text4)
        match_result5 = self.__matcher.match_iterable(text5)

        self.assertEqual('SERVICE-PRODUCT', match_result3.matches, text3)
        self.assertEqual('SERVICE-PRODUCT', match_result4.matches, text4)
        self.assertEqual('SERVICE-PRODUCT', match_result5.matches, text5)

        self.assertEqual('falan filan proje sözleşmesi ıjnj ınj satın alımı sözleşmesi.', match_result3.sentence, text3)
        self.assertEqual('falan filan danışmanlık sözleşmesi ıjnj ınj satın alımı sözleşmesi.', match_result4.sentence,
                         text4)
        self.assertEqual('falan filan ubuh hizmetlerini yerine getirir ubh satın alımı anlaşması.',
                         match_result5.sentence, text5)


if __name__ == '__main__':
    unittest.main()
