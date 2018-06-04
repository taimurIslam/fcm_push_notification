from pyfcm import FCMNotification

push_service = FCMNotification(api_key="AAAADr-ZRdI:APA91bG47NnjmLN_CWmWZ1aDfsW3UC5JkrFzzaM4WrGA0O54eZQzZZ50pn52n0swqbK2TG9_b-B6rGuQQFRRrq7dhVqmaxILGQhei8mreDolGDrFpMTCO0sLRGJ7-Z1OYtzVUVieGmMt")

data_message = {
        "payload": {
        "title": "Example",
        "alert": "Sample alert",
        "icon": "little_star",
        "badge": "2",
        "sound": "door_bell",
        "vibrate": True
        }

}

registration_id = "APA91bER9gvLorSy2hp-hrP413Pv2ARZLM0Hy8IEkKbm86wSd2VGo3FWLOQFNSUAcR7y788deqK3iBrnH6iXGCfGakJ5NWsowcVATcbs-m88vIlxiTbKOSAVnYdgM4eoJAfdmdrYvSfK"
message_title = "Test FCM"
message_body = "Hello Nuibb Vai!!"

result = push_service.single_device_data_message(registration_id= registration_id, data_message= data_message)


print(result)

