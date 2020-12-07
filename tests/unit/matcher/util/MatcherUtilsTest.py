import unittest
from src.matcher.util.MatcherUtils import MatcherUtils


class MatcherUtilsTest(unittest.TestCase):

    def testClearText(self):
        text = '“X” ``Y´´ \'\'Z\'\' faaliyetlerini kapsamaktadır\t\n'
        res = MatcherUtils.clear_text(text)

        self.assertEqual('"X" "Y" "Z" faaliyetlerini kapsamaktadır  ', res)

    def testTokenizeSentences(self):
        sentences = ['Ömer mısır sever', 'Ömer mısır yer', 'Ali ata bak']
        text = '{}. {}. {}.'

        results = MatcherUtils.tokenize_sentences(text.format(sentences[0], sentences[1], sentences[2]))
        key: int = 0
        for result in results:
            self.assertTrue(sentences[key] in result)
            key += 1


    def testExpand(self):
        pattern = '[\w\s\.]ömer|Proje|şemsiye|öğün'
        pattern = MatcherUtils.expand(pattern)

        self.assertEqual('[\wığüşiöçĞÜŞİÖÇ\s\.][oö]mer|Pr[oö]je|[sş]em[sş][ıi]ye|[oö][gğ][uü]n', pattern)