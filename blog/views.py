from django.shortcuts import render
from django.http import HttpResponse
from collections.abc import Hashable


from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

bot = ChatBot('chatbot', read_only=False, logic_adapters=[
    {
        'import_path': 'chatterbot.logic.BestMatch',
        #'default_response': 'Sorry, I don\'t know what you mean?',
        #'maximum_similarity_threshold': 0.90
    }
])

list_to_train = [
    "hi",
    "hi, there",
    "what's your name?",
    "I am just a chatbot",
    "how are you?",
    "I'm doing well, thank you!",
    "what can you do?",
    "I can help you with answering questions and engaging in conversation.",
    "tell me a joke",
    "Why don't scientists trust atoms? Because they make up everything!",
    "where are you from?",
    "I am a virtual assistant, so I don't have a physical location.",
    "what is the meaning of life?",
    "The meaning of life is subjective and can vary from person to person.",
    "how old are you?",
    "I am a program, so I don't have an age.",
    "what is your favorite color?",
    "As a chatbot, I don't have preferences, including favorite colors.",
    "can you help me with programming?",
    "Certainly! I can assist you with programming questions and provide guidance.",
    "what is the capital of France?",
    "The capital of France is Paris.",
    "who is the president of the United States?",
    "I'm sorry, I don't have the ability to provide real-time information. Please check the latest news for the current president.",
]

chatterbotCorpusTrainer = ChatterBotCorpusTrainer(bot)

chatterbotCorpusTrainer.train('chatterbot.corpus.english')


#list_trainer = ListTrainer(bot)
#list_trainer.train(list_to_train)



def index(request):
    return render(request, 'blog/index.html')

def specific(request):
    number = 30
    return HttpResponse(number)

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)

