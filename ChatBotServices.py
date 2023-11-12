import openai

def GetResponse(text):
    try:
        openai.api_key = "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"
        result = openai.Completion.create(model = "text-davinci-003",
                                          prompt = text,
                                          n = 1,
                                          max_tokens = 500)
        response = result.choices[0].text
        return response

    except Exception as exception:
        print (exception)
        return "error"