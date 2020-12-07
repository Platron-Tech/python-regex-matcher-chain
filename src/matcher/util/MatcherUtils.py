import nltk


class MatcherUtils:

    @staticmethod
    def clear_text(text):
        text = text.replace('“', '"')
        text = text.replace("”", '"')
        text = text.replace("''", '"')
        text = text.replace("``", '"')
        text = text.replace("´´", '"')
        text = text.replace("’", "'")
        text = text.replace("\u00a0", " ")
        text = text.replace("\t", " ")
        text = text.replace("\n", " ")
        return text

    @staticmethod
    def tokenize_sentences(text):
        text = MatcherUtils.clear_text(text)
        return nltk.sent_tokenize(text)

    @staticmethod
    def expand(pattern: str):
        return pattern \
            .replace('ı', '[ıi]') \
            .replace('i', '[ıi]') \
            .replace('ö', '[oö]') \
            .replace('o', '[oö]') \
            .replace('ğ', '[ğg]') \
            .replace('g', '[ğg]') \
            .replace('ü', '[uü]') \
            .replace('u', '[uü]') \
            .replace('ş', '[sş]') \
            .replace('s', '[sş]') \
            .replace('ç', '[cç]') \
            .replace('c', '[cç]') \
            .replace('İ', '[Iİ]') \
            .replace('I', '[Iİ]') \
            .replace('Ö', '[OÖ]') \
            .replace('O', '[OÖ]') \
            .replace('Ğ', '[ĞG]') \
            .replace('G', '[ĞG]') \
            .replace('Ü', '[ÜU]') \
            .replace('U', '[ÜU]') \
            .replace('Ş', '[SŞ]') \
            .replace('S', '[SŞ]') \
            .replace('Ç', '[CÇ]') \
            .replace('C', '[CÇ]') \
            .replace('[ı[ıi]]', '[ıi]') \
            .replace('[[Iİ]İ]', '[Iİ]') \
            .replace('[ğ[ğg]]', '[gğ]') \
            .replace('[Ğ[ĞG]]', '[GĞ]') \
            .replace('[[uü]ü]', '[uü]') \
            .replace('[Ü[ÜU]]', '[UÜ]') \
            .replace('[[sş]ş]', '[sş]') \
            .replace('[[SŞ]Ş]', '[SŞ]') \
            .replace('[[oö]ö]', '[oö]') \
            .replace('[[OÖ]Ö]', '[OÖ]') \
            .replace('[[cç]ç]', '[cç]') \
            .replace('[[CÇ]Ç]', '[CÇ]') \
            .replace('\[sş]', '\s') \
            .replace('[\w', '[\wığüşiöçĞÜŞİÖÇ')
