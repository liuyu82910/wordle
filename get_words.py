
def get_word():
    in_path = 'words.txt'
    out_path = 'five_letter_words.txt'
    five_letter_words = []
    with open(in_path, 'r') as f:
        for line in f.readlines():
            w = line.strip()
            if len(w) == 5:
                five_letter_words.append(w)
    with open(out_path, 'w') as f:
        for word in sorted(five_letter_words):
            f.write(word + '\n')
    print(f'We have {len(five_letter_words)} words')

if __name__ == '__main__':
    get_word()