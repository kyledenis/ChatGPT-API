# AI text generator
import openai

from api_keys import openai_api_key

openai.api_key = openai_api_key
prompt = "Explain quantum computing to me like I am a 5 year old."
response = openai.Completion.create(
    engine = "text-davinci-003",
    prompt = prompt,
    max_tokens = 256,
)
print(response["choices"][0]["text"])

# response = openai.Image.create(
#   prompt="duck on tomato",
#   n=5,
#   size="512x512"
# )
# image_url = response['data'][0]['url']
# print(image_url)