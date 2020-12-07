import unittest

from src.matcher.chain.TopicMatcher import TopicMatcher


class TopicMatcherTest(unittest.TestCase):
    __matcher = TopicMatcher()

    def testTopic_textShouldBeMatchedByUsingServicePattern(self):
        self.assertEqual('Test   hizmetasdşalskdads vermek.',
                         self.__matcher.match_iterable(
                             'ilk cümle. Test \n hizmetasdşalskdads vermek. son cümle').sentence)

    def testTopic_textShouldBeMatchedByUsingAgreementPattern(self):
        self.assertEqual("test   Sözleşmenin konusu xyz.",
                         self.__matcher.match_iterable('ilk cümle. test \n Sözleşmenin konusu xyz. son cümle').sentence)
        self.assertEqual("test   sözleşmenin konusu xyz.",
                         self.__matcher.match_iterable('ilk cümle. test \n sözleşmenin konusu xyz. son cümle').sentence)
        self.assertEqual("test   sozlesmenin konusu xyz.",
                         self.__matcher.match_iterable('ilk cümle. test \n sozlesmenin konusu xyz. son cümle').sentence)
        self.assertEqual("test   Sozlesmenin konusu xyz.",
                         self.__matcher.match_iterable('ilk cümle. test \n Sozlesmenin konusu xyz. son cümle').sentence)

    def testTopic_textShouldBeMatchedByUsingServiceScopePattern(self):
        self.assertEqual("falan filan hizmet kapsamındadır.",
                         self.__matcher.match_iterable(
                             'ilk cümle. falan filan hizmet kapsamındadır. son cümle').sentence)
        self.assertEqual("falan filan hizmet kapsamindadır.",
                         self.__matcher.match_iterable(
                             'ilk cümle. falan filan hizmet kapsamindadır. son cümle').sentence)
        self.assertEqual("falan filan hizmet kapsamindadir.",
                         self.__matcher.match_iterable(
                             'ilk cümle. falan filan hizmet kapsamindadir. son cümle').sentence)
