# -*- coding: cp1251 -*-
import json

import vk_api
import time
from course import Course
from K_VK_1 import *
from K_VK_2 import *

token = "vk1.a.atb_9VCYLCxNGKnswdygybIoNVKsS6JOi2KcKAHCa_U7y4i0K6xyGJueGVhuXJqoUOsjY8r1YsJOnFzMBD7bM_YwmheXEisELxTNW_lH8ZyQIjnHI3X0Z_lWNYr69wskZOkNsihPHGeq9y5rqS45d-buuZxDuKdyIoyn31Ib97PXJvOT40TI0JkwKl8j1x_HVnTBUW9Ytrw99J6zhKbZOQ"

vk = vk_api.VkApi(token=token)
#vk._auth_token()
#messages = vk.method("messages.getConversations", {"count": 20, "filter": "unanswered"})
#print(messages)

#with open("data.json", "w", encoding="utf-8") as file:
#    json.dump(messages, file, indent=4, ensure_ascii=False)



while True:
    try:
        messages = vk.method("messages.getConversations", {"count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            messages_id = messages["items"][0]["last_message"]["id"]
            messages_text = messages["items"][0]["last_message"]["text"]
            if messages_text.lower() == "курс":
                vk.method("messages.send", {"peer_id": id, "random_id": messages_id, "message": Course("R01035")})
            if messages_text.lower() == "корабли":
                vk.method("messages.send", {"peer_id": id, "random_id": messages_id, "message": check_func})




            else:
                vk.method("messages.send", {"peer_id": id, "random_id": messages_id, "message": "что ты от меня хочешь?"})
    except vk_api.exceptions.ApiError as e:
        print(e)
        e.try_method()
