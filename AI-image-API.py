# AI text generator
import openai

from api_keys import openai_api_key

openai.api_key = openai_api_key
response = openai.Image.create(
  prompt="duck on tomato",
  n=5,
  size="512x512"
)
image_url = response['data'][0]['url']
print(image_url)