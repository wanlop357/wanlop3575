from messengerbot import MessengerClient, messages, attachments, templates, elements

# Manully initialise client
messenger = MessengerClient(access_token='EAADrcnA0YAIBAMfwcg2wUmk6BG2IHZAthghXZBqYwE4Arb5uYz8M7foLlm1cfPsNdlj8JIlNmE8n7isZCAhn2b7ZChWoJxyentZC5aqRtIMfR4ich')

# With env var export MESSENGER_PLATFORM_ACCESS_TOKEN=your_token
from messengerbot import messenger

recipient = messages.Recipient(recipient_id='123')

# Send text message
message = messages.Message(text='Hello World')
request = messages.MessageRequest(recipient, message)
messenger.send(request)

# Send button template
web_button = elements.WebUrlButton(
   title='Show website',
   url='https://petersapparel.parseapp.com'
)
postback_button = elements.PostbackButton(
   title='Start chatting',
   payload='USER_DEFINED_PAYLOAD'
)
template = templates.ButtonTemplate(
   text='What do you want to do next?',
   buttons=[
       web_button, postback_button
   ]
)
attachment = attachments.TemplateAttachment(template=template)

message = messages.Message(attachment=attachment)
request = messages.MessageRequest(recipient, message)
messenger.send(request)
