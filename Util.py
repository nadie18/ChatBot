def GetTextUser(message):
    text = ""
    typeMessage = message ["type"]

    if typeMessage == "text":
        text = (message["text"])["body"]

    elif typeMessage == "interactive":
        interactiveObject = message ["interactive"]
        typeInteractive = interactiveObject["type"]
        
        if typeInteractive == "button_reply":
            text = (interactiveObject ["button_reply"])["title"]
        elif typeInteractive == "list_reply":
            text = (interactiveObject ["list_reply"])["title"]
        else:
            print("sin mensaje")

    else:
        print ("sin mensaje")

    return text

def TextMessage(text, number):
    data = {
                "messaging_product": "whatsapp",
                "to": number,
                "text": {
                    "body": text
                },
                "type": "text"
            }
    return data

def TextFormatMessage(number):
    data = {
                "messaging_product": "whatsapp",
                "to": number,
                "text": {
                    "body": "Hola 🐶"
                },
                "type": "text"
            }
    return data

def ImageMessage(number):
    data = {
                "messaging_product": "whatsapp",
                "to": number,
                "type": "image",
                "image": {
                    "link": "https://biostoragecloud.blob.core.windows.net/resource-udemy-whatsapp-node/image_whatsapp.png"
                },
            }
    return data

def AudioMessage(number):
    data = {
                "messaging_product": "whatsapp",
                "to": number,
                "type": "audio",
                "audio": {
                    "link": "https://biostoragecloud.blob.core.windows.net/resource-udemy-whatsapp-node/audio_whatsapp.mp3"
                },
            }
    return data

def VideoMessage(number):
    data = {
                "messaging_product": "whatsapp",
                "to": number,
                "type": "video",
                "video": {
                    "link": "https://biostoragecloud.blob.core.windows.net/resource-udemy-whatsapp-node/video_whatsapp.mp4"
                },
            }
    return data

def DocumentMessage(number):
    data = {
                "messaging_product": "whatsapp",
                "to": number,
                "type": "document",
                "document": {
                    "link": "https://biostoragecloud.blob.core.windows.net/resource-udemy-whatsapp-node/document_whatsapp.pdf"
                },
            }
    return data

def LocationMessage(number):
    data = {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": number,
                "type": "location",
                "location": {
                "latitude": "14.649894354836782",
                "longitude": "-90.48080515033526",
                "name": "Casa Del Maltes 🐶",
                "address": "JGX9+RHM, Cdad. de Guatemala"
                }
            }
    return data

def ButtonsMessage(number):
    data = {
    "messaging_product": "whatsapp",
    "recipient_type": "individual",
    "to": number,
    "type": "interactive",
    "interactive": {
        "type": "button",
        "body": {
            "text": "¿Quieres hacer una Cita el día de hoy?"
        },
        "action": {
            "buttons": [
                {
                    "type": "reply",
                    "reply": {
                        "id": "001",
                        "title": "Si 😁"
                    }
                },
                {
                    "type": "reply",
                    "reply": {
                        "id": "002",
                        "title": "No 😔"
                    }
                }
            ]
        }
    }
}
    return data

def ListMessage(number):
    data = {
    "messaging_product": "whatsapp",
    "to": number,
    "type": "interactive",
    "interactive": {
        "type": "list",
        "body": {
            "text": "✅ Opciones"
        },
        "footer": {
            "text": "Selecciona una opcion"
        },
        "action": {
            "button": "Ver Opciones",
            "sections": [
                {
                    "title": "Precios y Horarios",
                    "rows": [
                        {
                            "id": "main-grooming",
                            "title": "Precios para grooming",
                            "description": "Marca esta opcion si deseas conocer los precios del grooming"
                        },
                        {
                            "id": "main-Horarios",
                            "title": "Horarios",
                            "description": "Mira Nuestros Horarios de atencion"
                        }
                    ]
                },
                {
                    "title": "📍Atencion al cliente",
                    "rows": [
                        {
                            "id": "main-agency",
                            "title": "Agencia",
                            "description": "Quieres Visitar nuestra Sucursal"
                        },
                        {
                            "id": "main-contact",
                            "title": "Contactanos 🐶",
                            "description": "Presiona aqui si quieres que un representante te atienda"
                        }
                    ]
                }
            ]
        }
    }
}
    return data