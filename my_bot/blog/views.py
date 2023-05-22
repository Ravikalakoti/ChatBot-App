from django.shortcuts import render
from django.http import HttpResponse

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer


bot = ChatBot('chatbot', read_only=False,
	logical_adapters=[
		{
			'import_path':'chatterbot.logic.BestMatch'
			# 'default_response':'Sorry, I dont know what that means',
			# 'maximum_similarity_threshold': 0.90
		}
	])


list_to_train = [

	"hi",
	"hi, there",
	"what's your name?",
	"i'm just a chatbot",
	"whats your fevrote food?",
	"i like cheese"

]

chatterbotCorpusTrainer = ChatterBotCorpusTrainer(bot)
chatterbotCorpusTrainer.train('chatterbot.corpus.english')
# list_trainer = ListTrainer(bot)
# list_trainer.train(list_to_train)

def index(request):
	return render(request, 'blog/index.html')

def getResponse(request):
	userMessage = request.GET.get('userMessage')
	chatResponse = str(bot.get_response(userMessage))
	return HttpResponse(chatResponse)

#https://www.youtube.com/watch?v=AeDsCnbnXbA