from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
 
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage

from .scraper import IFoodie
 
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
 
 
@csrf_exempt
def callback(request):
 
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
 
        try:
            events = parser.parse(body, signature) 
            print(events)

        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
 
        for event in events:
            if isinstance(event, MessageEvent):  

                text = event.message.text

                if "地區：" in text and "類別：" in text:
                    area, category = text.split("地區：")[1].split("類別：")

                    food = IFoodie(area, category)
                    response = food.scrape()

                    line_bot_api.reply_message(  
                        event.reply_token,
                        TextSendMessage(text=response)
                    )

                else:
                    response = "請按照以下格式輸入：\n地區：XXX 類別：YYY"
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=response)
                    )
                    
        return HttpResponse()
    else:
        return HttpResponseBadRequest()