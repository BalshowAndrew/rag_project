import os

from dotenv import load_dotenv

load_dotenv()

print(os.getenv('API_KEY'))


def main():
    print("Hello from rag-studying!")


if __name__ == "__main__":
    main()
