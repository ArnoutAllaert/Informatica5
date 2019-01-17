#tweet = str(input('geef tweet: '))
#hashtags = ''
#k = 1


#for i in range(0, len(tweet) - 1):
    #if tweet[i] == '#':
        #while tweet[i + k] != ' ':
            #k += 1
        #if tweet[i + k] == ' ':
            #hashtags += tweet[i + 1: i + k] + '\n'
            #k = 1

#print(hashtags)

tweet = input('geef tweet: ')

i_hashtag = tweet.find('#')

while i_hashtag != -1:  #als i_hashtag == -1 zijn er geen hashtags
    #tweet afknippen na #
    tweet = tweet[i_hashtag +1:]
    i_spatie = tweet.find(' ')
    #hashtag uitknippen (en printen)
    print(tweet[: i_spatie])
    #terug op zoek naar een #
    i_hashtag = tweet.find('#')


