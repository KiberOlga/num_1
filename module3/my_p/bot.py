# -*- coding: cp1251 -*-
"""import json
import random

import vk_api
import time
from course import Course
#from K_VK_1 import *
from K_VK_2 import *
from vk_api.longpoll import VkLongPoll, VkEventType

token = "vk1.a.atb_9VCYLCxNGKnswdygybIoNVKsS6JOi2KcKAHCa_U7y4i0K6xyGJueGVhuXJqoUOsjY8r1YsJOnFzMBD7bM_YwmheXEisELxTNW_lH8ZyQIjnHI3X0Z_lWNYr69wskZOkNsihPHGeq9y5rqS45d-buuZxDuKdyIoyn31Ib97PXJvOT40TI0JkwKl8j1x_HVnTBUW9Ytrw99J6zhKbZOQ"

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
long_polling = VkLongPoll(vk_session)



#vk._auth_token()
#messages = vk.method("messages.getConversations", {"count": 20, "filter": "unanswered"})
#print(messages)

#with open("data.json", "w", encoding="utf-8") as file:
#    json.dump(messages, file, indent=4, ensure_ascii=False)


for event in long_polling.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        message = event.text
        user_id = event.user_id
        random_id = random.randint(1, 1000000000000000)
        if message == "курс":
            response = f"{Course('R01335')}"
            vk.messages.send(user_id=user_id, random_id=random_id, message=response)"""







import json
import random
import vk_api
import time
from course import Course
from vk_api.longpoll import VkLongPoll, VkEventType

token = "vk1.a.atb_9VCYLCxNGKnswdygybIoNVKsS6JOi2KcKAHCa_U7y4i0K6xyGJueGVhuXJqoUOsjY8r1YsJOnFzMBD7bM_YwmheXEisELxTNW_lH8ZyQIjnHI3X0Z_lWNYr69wskZOkNsihPHGeq9y5rqS45d-buuZxDuKdyIoyn31Ib97PXJvOT40TI0JkwKl8j1x_HVnTBUW9Ytrw99J6zhKbZOQ"

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
long_polling = VkLongPoll(vk_session)

for event in long_polling.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        message = event.text
        user_id = event.user_id
        random_id = random.randint(1, 1000000000000000)
        if message.startswith('-к '):
            response = f"{Course('')}"
            vk.messages.send(user_id=user_id, random_id=random_id, message=response)

