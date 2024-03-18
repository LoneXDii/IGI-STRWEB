def sort_words_by_len(string):
    symbs_to_delete = ".,"
    new_string = string
    for ch in symbs_to_delete:
        new_string = new_string.replace(ch, "")
    words = new_string.split()
    words = sorted(words, key=len, reverse=True)
    return words

def count_of_max_len_words(string):
    words = sort_words_by_len(string)
    count = len([x for x in words if len(x) == len(words[0])])
    return count

def words_bef_puct_sign(string):
    words = string.split()
    answ_words = list()
    for word in words:
        if '.' in word or ',' in word:
            answ_words.append(word[:-1])
    return answ_words

def longest_e_ended_word(string):
    words = sort_words_by_len(string)
    for word in words:
        if word[-1] == 'e':
            return word
    return ""

def task4():
    string = "So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her."
    print(count_of_max_len_words(string), "words have max len")
    print(words_bef_puct_sign(string), "are words before . or ,")
    print(longest_e_ended_word(string), "is the longest word ended by e")