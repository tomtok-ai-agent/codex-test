import os
from datetime import date
import openai
import click

# Entry point for the console application
@click.command()
def main() -> None:
    """Generate a poem about today's date using OpenAI."""
    # Get the current date
    today = date.today().isoformat()

    # Prepare the prompt for the language model
    prompt = f"Write a short poem about the date {today}."

    # Retrieve API key from environment
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set")

    # Configure OpenAI client
    openai.api_key = api_key

    # Call the API to get a poem
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )

    poem = response.choices[0].message.content
    click.echo(poem)

if __name__ == "__main__":
    main()
