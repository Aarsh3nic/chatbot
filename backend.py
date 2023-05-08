import openai


class Chatbot:
    def __init__(self):
        openai.api_key = "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"

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5
        ).choices[0].text
        # temperature - closer to 0 has less unique answers-more accuracy
        return response

if __name__ =="__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a compliment for a teenage girl")
    print(response)