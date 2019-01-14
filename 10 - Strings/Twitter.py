tweet = str(input('geef tweet: '))
hashtags = ''
k = 1


for i in range(0, len(tweet) - 1):
    if tweet[i] == '#':
        while tweet[i + k] != ' ':
            k += 1
        if tweet[i + k] == ' ':
            hashtags += tweet[i + 1: i + k] + '\n'
            k = 1

print(hashtags)


