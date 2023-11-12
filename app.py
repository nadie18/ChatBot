from flask import Flask, request 
import Util
import whatsappservice
import ChatBotServices

app = Flask(__name__)
@app.route('/Welcome', methods=['GET'] )
def index():
    return "Bienvenido Gerson"

@app.route('/whatsapp', methods=['GET'] )
def VerifyToken():

    try:
        accessToken = "       "
        token = request.args.get("hub.verify_token")
        challenge =request.args.get("hub.challenge")

        if token != None and challenge != None and token == accessToken:
            return challenge
        else:
            return "", 400
    except:
            return "", 400

@app.route('/whatsapp', methods=['POST'] )
def ReceivedMessage():

    try:
         body = request.get_json()
         entry = (body["entry"]) [0]
         changes = (entry["changes"]) [0]
         value = changes["value"]
         message = (value["messages"])[0]
         number = message["from"]

         text = Util.GetTextUser(message)
         #responseGPT = ChatBotServices.GetResponse(text)

         #if responseGPT != "error":
           #   data = Util.TextMessage(responseGPT, number)
         #else:
          #    data = Util.TextMessage("Lo siento ha ocurrido un problema", number)

         #whatsappservice.SendMessageWhatsapp(data)  
    
         ProcessMessages(text, number)
         print (text)

         return "EVENT_RECEIVED"
    
    except:
            return "EVENT_RECEIVED"
    
def ProcessMessages(text, number):
    text = text.lower()
    listData = []

    if "hola" in text or "buen" in text:
        data = Util.TextMessage("Hola 🐶🐾🐈, ¿cómo te puedo ayudar?", number)
        dataMenu = Util.ListMessage(number)
        dataEncuesta = Util.TextMessage("Al terminar Podrias llenar la siguiente encuesta 😊: *https://docs.google.com/forms/d/1h8PbFsQStp9aqpQGxA1jhZAF5gGInvyP9R0fm8em5gk/edit*", number)

        listData.append(data)
        listData.append(dataMenu)
        listData.append(dataEncuesta)

    elif "gracias" in text:
        data = Util.TextMessage("Gracias por contactarnos, espero leerte pronto! 😁", number)
        dataEncuesta = Util.TextMessage("Prodias llenar esta encuesta de satisfacción 😊: *https://docs.google.com/forms/d/1h8PbFsQStp9aqpQGxA1jhZAF5gGInvyP9R0fm8em5gk/edit*", number)
        listData.append(data)
        listData.append(dataEncuesta)
        

    elif "agencia" in text or "ubicación" in text:
         data = Util.TextMessage("Nos encontramos úbicados en km,4.5 Ruta al Atlántico Comercial Los Álamos plaza No.2, te mando la ubicación 😁", number)
         dataMenu = Util.LocationMessage(number)
         listData.append(data)
         listData.append(dataMenu)

    elif "grooming" in text:
         data = Util.TextMessage("El precio del grooming varia según el tamaño de tu mascota 🐶🐾🐈"
                                 "\nPequeño:       Q100.00"
                                 "\nMediano:       Q125.00"
                                 "\nGrande:          Q150.00"
                                 "\nExtra Grande:  Q175.00", number)
         listData.append(data)

    elif "horarios" in text:
         data = Util.TextMessage("*Nuestos Horarios Son*:\nLunes a Viernes de 09:00 a 19:00\n*Toma en cuenta que si es día festivo o asueto el horario puede variar.*",number)
         listData.append(data)

    elif "contactanos" in text:
         data = Util.TextMessage("Puedes contactarnos al siguiente número:\n*53546127*\nO a nuestro correo:\n*lacasadelmaltes@hotmail.com*",number)
         listData.append(data)

    elif "si" in text:
         data = Util.TextMessage("Puedes comunicarte a este número *53546127* pagara agendar tú cita.", number)
         listData.append(data)

    elif "no" in text:
         data = Util.TextMessage("Espero darte un buen servicio pronto 🐶🐾🐈", number)
         listData.append(data)
     
    else:
        data = Util.TextMessage("No te entiendo 😔 \nTe dejo una lista de las acciones que puedo realizar",number)
        dataMenu = Util.ListMessage(number)
        listData.append(data)
        listData.append(dataMenu)

    for item in listData:
         whatsappservice.SendMessageWhatsapp(item)  



def GenerateMessage(text, number):
    
    text = text.lower()
    if "text" in text:
        data = Util.TextMessage("Text", number)

    if "formate" in text:
         data = Util.TextFormatMessage(number)

    if "image" in text:
         data = Util.ImageMessage(number)

    if "video" in text:
         data = Util.VideoMessage(number)

    if "documento" in text:
         data = Util.DocumentMessage(number)

    if "audio" in text:
         data = Util.AudioMessage (number)

    if "ubicacion" in text:
         data = Util.LocationMessage (number)

    if "botones" in text:
         data = Util.ButtonsMessage (number)

    if "lista" in text:
         data = Util.ListMessage (number)

    whatsappservice.SendMessageWhatsapp(data)      

if(__name__ == "__main__"):
    app.run()