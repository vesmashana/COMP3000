from LLM_communication.FS8B import fs8b
from LLM_communication.WRN import WRN

messages = []
for i in range(3):
    input_msg = input("Enter your message: ")
    messages = WRN(input_msg, messages)

for i in range(3):
    input_msg = input("Enter your message: ")
    messages = fs8b(input_msg, messages)

