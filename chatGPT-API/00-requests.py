import secrets
import openai

## connect chat gpt
# response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo", messages=[{"role":"user", "content":"Hello!"}]
# )

# print(response)
# print(response.choices[0].message.content)

#create chat completion

def chat_bot():
    message = []

    openai.api_key=secrets.OPENAL_API_KEY

    while True:
        content = input("user : ")
        if content == "종료":
            break

        message.append({"role":"user", "content":content})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages= message)
        
        assistant_content = response.choices[0].message.content

        message.append({"role":"assistant", "content": f"{assistant_content}"})

        print(f"Answer : {assistant_content}")

        continue

    

chat_bot()