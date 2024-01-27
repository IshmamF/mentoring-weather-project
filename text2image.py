import requests
import json

def generate_image(location, weather, country, description):
  url = "https://stablediffusionapi.com/api/v3/text2img"

  payload = json.dumps({
    "key": "I8CCXlMZmJWAPecrDlTUHp2EtuXgf4aL55LxtZJdo59aHk4o6qk8mzLj4t8S",
    "prompt": f"scenary or famous landmark in {location},{country} with the weather consisting of {weather} and {description}",
    "negative_prompt": None,
    "width": "512",
    "height": "512",
    "samples": "1",
    "num_inference_steps": "20",
    "seed": None,
    "guidance_scale": 7.5,
    "safety_checker": "yes",
    "multi_lingual": "no",
    "panorama": "no",
    "self_attention": "no",
    "upscale": "no",
    "embeddings_model": None,
    "webhook": None,
    "track_id": None
  })

  headers = {
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  return response.json()["output"][0]