import pymsteams


class SendToTeams:
    def send(message):
        # You must create the connectorcard object with the Microsoft Webhook URL
        myTeamsMessage = pymsteams.connectorcard("https://highpcs.webhook.office.com/webhookb2/14ab7cfd-e26d-473b-a7f3-696042fdb50b@5b309589-37c9-4d57-ada3-542710c037be/IncomingWebhook/24c55a97520147f29a4baa8a50948aa6/40ac87cf-4260-44d2-b8d1-bfba0429cd11")

        # Add text to the message.
        myTeamsMessage.text(message)

        # send the message.
        myTeamsMessage.send()