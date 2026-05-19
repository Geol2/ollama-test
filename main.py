import ollama

def main():
    print("Hello from ollama!")

    result = ollama.generate(model='qwen3.8b', prompt='왜 하늘은 파랗죠?')
    print(result['response'])    

if __name__ == "__main__":
    main()
