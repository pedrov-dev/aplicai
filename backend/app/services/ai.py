"""
This file contains functions for interacting with the OpenAI API to generate cover letter drafts.
"""

import os
from openai import OpenAI
from ..core.config import settings
client = OpenAI()

client.api_key = settings.OPENAI_API_KEY

def generate_cover_letter(prompt: str, model: str = "gpt-4.1-mini") -> str:
    """
    Generate a cover letter draft using the OpenAI API.
    :param prompt: The prompt to send to the model.
    :param model: The OpenAI model to use.
    :return: The generated cover letter text.
    """
    # TODO: Customize parameters as needed
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "developer", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    # TODO: Handle potential errors from the OpenAI API
    # Alternatively, we can return a string:
    # return completion.choices[0].message.content or "x"
    content = completion.choices[0].message.content
    if content is None:
        raise ValueError("No content returned from OpenAI API")
    return content