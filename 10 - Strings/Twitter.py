tweet = str(input('geef tweet: '))
hashtags = ''


for i in range(0, len(tweet) - 1):
    if tweet[i] == '#':
        hashtags += tweet[i + 1] + '\n'

print(hashtags)
