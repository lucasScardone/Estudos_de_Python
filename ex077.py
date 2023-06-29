words = ('learn', 'programming', 'language', 'python', 'course', 'free', 'study',
         'practice', 'work', 'market', 'developer', 'future', 'nintendo', 'pudding')
vowels = ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U')
for count in range(len(words)):
    print(f'\nNa palavra {words[count]} temos', end=' ')
    word = list(words[count])
    for letter in range(len(word)):
        if word[letter] in vowels:
            print(f' {word[letter]}', end=' ')
