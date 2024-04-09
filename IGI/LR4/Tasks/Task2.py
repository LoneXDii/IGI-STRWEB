import re
from Services.FileService import FileService

class Task2:
    @staticmethod
    def __analyze_sentences_types(text):
        pobud = len(re.findall(r"\!(\s|$)", text))
        povest = len(re.findall(r"\.(\s|$)", text))
        vopr = len(re.findall(r"\?(\s|$)", text))
        return pobud, povest, vopr

    @staticmethod
    def __get_av_sentence_len(text):
        sentences = re.findall(r"([^?!.]+)(\.|\!|\?)", text)
        sentences_len = 0
        for sentence in sentences:
            a = str(sentence[0][2:])
            words = re.findall(r"\b[A-z]+\b", str(sentence))
            for word in words:
                sentences_len += len(word)
        return sentences_len / len(sentences)

    @staticmethod
    def __get_words(text):
        return re.findall(r"\b[A-z]+\b", text)

    @staticmethod
    def __get_av_word_len(text):
        words = Task2.__get_words(text)
        words_len = 0
        for word in words:
            words_len += len(word)
        av_len = round(words_len / len(words))
        return av_len

    @staticmethod
    def __get_word_of_len(text, w_len):
        words = Task2.__get_words(text)
        l_words = list()
        for word in words:
            if len(word) == w_len:
                l_words.append(word)
        return l_words

    @staticmethod
    def __get_ev_7th_word(text):
        words = Task2.__get_words(text)
        i = 1
        ev_7th_word = list()
        for word in words:
            if i % 7 == 0:
                ev_7th_word.append(word)
            i += 1
        return ev_7th_word

    @staticmethod
    def __get_smiles_count(text):
        return len(re.findall(r"(:|;)(\-*)(\(+|\)+|\[+|\]+)", text))

    @staticmethod
    def __get_phone_numbers(text):
        return re.findall(r"29\d{7}\b", text)

    @staticmethod
    def __get_words_for_found(text):
        return re.findall(r"\b[A-z][bcdfghjklmnpqrstvxzBCDFGHJKLMNPQRSTVXZ][aeiouyAEIOUY][A-z]*\b", text)

    @staticmethod
    def __get_count_of_consonant_ended_words(text):
        return len(re.findall(r"\b[A-z]*[bcdfghjklmnpqrstvxzBCDFGHJKLMNPQRSTVXZ]\b", text))

    @staticmethod
    def __analyze_text(text):
        result = ""
        pobud, povestv, vopr = Task2.__analyze_sentences_types(text)
        result += f"В тексте {pobud + vopr + povestv} предложений\n"
        result += f"Повествовательных: {povestv}\n"
        result += f"Побудительных: {pobud}\n"
        result += f"Вопросительных: {vopr}\n\n"

        av_sent_len = Task2.__get_av_sentence_len(text)
        result += f"Средняя длина предложения: {av_sent_len}\n"

        av_word_len = Task2.__get_av_word_len(text)
        result += f"Средняя длина слова: {av_word_len}\n"

        smiles_count = Task2.__get_smiles_count(text)
        result += f"Количество смайликов: {smiles_count}\n"

        phones = Task2.__get_phone_numbers(text)
        result += f"Номера телефонов: {phones}\n"

        find_words = Task2.__get_words_for_found(text)
        result += f"Слова, у которых вторая буква согласная, а третья – гласная: {find_words}\n"

        sogl_count = Task2.__get_count_of_consonant_ended_words(text)
        result += f"Число слов, заканчивающихся на согласную: {sogl_count}\n"

        av_len_w = Task2.__get_word_of_len(text, av_word_len)
        if len(av_len_w) != 0:
            result += f"Cлова, которые имеют среднюю длину: {av_len_w}\n"
        else:
            result += f"Слов длиной {av_word_len} символов в строке нет\n"

        ev_7th = Task2.__get_ev_7th_word(text)
        result += f"Каждое 7-е слово: {ev_7th}"

        return result

    @staticmethod
    def task2():
        source_path = 'Task2text.txt'
        dest_path = 'Task2answer.txt'
        archive_path = 'Task2archive.zip'
        text = str(FileService.read_from_file(source_path))
        result = Task2.__analyze_text(text)
        FileService.save_to_file(dest_path, result)
        FileService.archive_file(dest_path, archive_path)
        FileService.get_archive_info(archive_path)
