from functions.get_files_info import get_files_info
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <prompt>")
        sys.exit(1)

    user_prompt=" ".join(sys.argv[1:])
    file=get_files_info("/home/aetienne/GIT/BOOT.DEV/ai_agent",user_prompt)
    print(file)


if __name__ == "__main__":
    main()