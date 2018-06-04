from pyfcm import FCMNotification

push_service = FCMNotification(api_key="AAAADr-ZRdI:APA91bG47NnjmLN_CWmWZ1aDfsW3UC5JkrFzzaM4WrGA0O54eZQzZZ50pn52n0swqbK2TG9_b-B6rGuQQFRRrq7dhVqmaxILGQhei8mreDolGDrFpMTCO0sLRGJ7-Z1OYtzVUVieGmMt")

# OR initialize with proxies
# device reg key: APA91bEVITkv6xiTrgXvS7zAKEI1-ab81b1IDO3_czmlYblgy_3APnGv93owj3rG5tpoC9iJaaDhfGwaGkxd6wOi-8993jtVE7g2iJjWs2sNramzofxi_9pccWRq_4DzIDbqlR5dKURs
# Server key : AAAA8xjBQJY:APA91bFMxftGr2N0tk1ct7Z8XSGiXOHbEdrT4kAElJaPUjr5J1woAGtNgosxkaOqJ6QPWDQqJttmYqDV5X_fZ7_8Yg7aeIXwWe7oD3ml1CPfF_vrVU6WmosC27i0gqV8stQ

# proxy_dict = {
#     "http": "http://192.168.2.85:8000",
#     "https": "http://192.168.2.85:8000",
# }
# push_service = FCMNotification(api_key="<api-key>", proxy_dict=proxy_dict)

# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging

data_message = {
    "Nick" : "Mario",
    "body" : "great match!",
    "Room" : "PortugalVSDenmark"
}

registration_ids = ["APA91bER9gvLorSy2hp-hrP413Pv2ARZLM0Hy8IEkKbm86wSd2VGo3FWLOQFNSUAcR7y788deqK3iBrnH6iXGCfGakJ5NWsowcVATcbs-m88vIlxiTbKOSAVnYdgM4eoJAfdmdrYvSfK"]
message_title = "Test FCM"
message_body = "Hello Nuibb Vai!!"
#result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body, data_message=data_message)

print(result)
# server key : AAAADr-ZRdI:APA91bG47NnjmLN_CWmWZ1aDfsW3UC5JkrFzzaM4WrGA0O54eZQzZZ50pn52n0swqbK2TG9_b-B6rGuQQFRRrq7dhVqmaxILGQhei8mreDolGDrFpMTCO0sLRGJ7-Z1OYtzVUVieGmMt
# device reg key: APA91bER9gvLorSy2hp-hrP413Pv2ARZLM0Hy8IEkKbm86wSd2VGo3FWLOQFNSUAcR7y788deqK3iBrnH6iXGCfGakJ5NWsowcVATcbs-m88vIlxiTbKOSAVnYdgM4eoJAfdmdrYvSfK


