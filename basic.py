
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer

import logging  
logger = logging.getLogger() 
logger.setLevel(logging.CRITICAL)

chatbot = ChatBot('MyChatBot',
                storage_adapter='chatterbot.storage.SQLStorageAdapter',
database_uri=None,
                logic_adapters=[
'chatterbot.logic.MathematicalEvaluation',
#'chatterbot.logic.TimeLogicAdapter',
'chatterbot.logic.BestMatch'
])

trainer = ListTrainer(chatbot)
for _ in range(1):
    trainer.train(['How are you?','I\'m doing great.','That is good to hear.','Thank you.','You\'re welcome.'])
    trainer.train([
        "Hi, can I help you?",
        "Sure, I'd like to book a flight to Iceland.",
        "Your flight has been booked."
    ])

# Training with English Corpus Data 
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
    'chatterbot.corpus.english'
) 

print('Type something to begin...')
while True:
    try:
        bot_input = chatbot.get_response(input())
        print(bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break