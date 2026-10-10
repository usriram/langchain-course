from dotenv import load_dotenv

load_dotenv()
import os

print("my api key is " + os.getenv("OPENAI_API_KEY"))


def main():
    print("Hello from langchain-course!")


if __name__ == "__main__":
    main()
