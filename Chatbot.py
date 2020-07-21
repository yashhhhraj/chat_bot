import random
from textblob import TextBlob

print('Hello human what is your name?')
name = input()
print('Do you have nickname?')
ans = input()
if 'y' in ans.lower():
  nickname = input('whatis your nickname: ')
  print('Good to meet you ' + nickname)
else:
  nickname = name + name[-1] + 'y'
  print('I will call you '+nickname)


greetings = [
	'How are you today ' + nickname +'?',
	'Howdy ' + nickname + ' how are you feeling?',
	"What's up " + nickname +'?',
	'Greetings ' + nickname +', are you well?',
	'How are things going ' + nickname +'?'
]
print(random.choice(greetings))
ans = input()
blob = TextBlob(ans)

if blob.polarity > 0:
  print('Glad you are doing well')
else:
  print('Sorry to hear that')


topics = [
	'football',
	'Melbourne',
	'AFL',
	'Endgame',
	'Python',
	'Computers',
	'Computer games'
]

questions = [
	'What is your take on ',
	'What do you think about ',
	'How do you feel about ',
	'What do you reckon about ',
	'I would like your opinion on '
]
for i in range(0, random.randint(3,4)):
  question = random.choice(questions)
  questions.remove(question)
  topic = random.choice(topics)
  topics.remove(topic)
  print(question + topic + '?')
  ans = input()
  blob = TextBlob(ans)
    

  if blob.polarity > 0.5:
    print('OMG you really love '+ topic)
  elif blob.polarity > 0.1:
    print('Well, you clearly like '+ topic)
  elif blob.polarity < -0.5:
    print('Woof, you totally hate '+ topic)
  elif blob.polarity < -0.5:
    print("So you don't like "+ topic)
  else:
    print('That is a very neutral view on '+ topic)
  
  if blob.subjectivity > 0.6:
    print('and you are so biased')
  elif blob.subjectivity > 0.3:
    print('and you are a bit bireased')
  else:
    print('and you are quite objective')



goodbyes = [
	'Good talking to you ' + nickname + 'I gotta go now',
	'OK I am bored, I will go watch Netflix',
	'Bye bye Miss American Pie, I am out',
	'Yaaawn . . . I gotta go now',
	'Catch ya later, '+ nickname
]
print(random.choice(goodbyes))
