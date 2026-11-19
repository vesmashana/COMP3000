#helpers for API calls to FS8B Model
import requests
URL = "http://10.244.135.76:11434/api/chat"
MODEL = "fs-8b"

def make_message(message, role="user"):
    return {"role": role, "content": message}


def fs8b(user_msg, messages=None):
    if messages is None:
        messages = []
    user_msg = make_message(user_msg)
    
    payload = {
        "model": MODEL,
        "messages": messages + [user_msg],
        "stream": False

    }
    resp = requests.post(URL, json=payload, timeout=(5, 300))
    resp.raise_for_status()
    LLM_msg = resp.json()["message"]
    print(LLM_msg)
    messages.append(user_msg)
    messages.append(LLM_msg)
    return messages


    


