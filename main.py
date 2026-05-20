from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage

llm = ChatOllama(model="qwen3:8b",
                base_url="http://localhost:11434")

def main():
    while True:
        user_input = input("질문을 입력하세요 (종료: exit) : ")
        if user_input.lower() == "exit":
            break

        messages = [HumanMessage(content=user_input)]

        response = llm.invoke(messages)

        print(response)

if __name__ == "__main__":
    main()
