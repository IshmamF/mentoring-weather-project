import requests
from dotenv import load_dotenv
load_dotenv()
import os
import json
STABLE_API = os.getenv("STABLE_API")

def generate_image(location, weather, country, description):
  url = "https://stablediffusionapi.com/api/v3/text2img"

  payload = json.dumps({
    "key": STABLE_API,
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
