import re

def preprocess_conversation(conversation):
    conversation = conversation.lower()
    conversation = re.sub(r'\s+', ' ', conversation)
    
    user_messages = re.findall(r'user:.*?(?=assistant:|$)', conversation)
    assistant_messages = re.findall(r'assistant:.*?(?=user:|$)', conversation)
    
    preprocessed = ' '.join(user_messages + assistant_messages)
    return preprocessed