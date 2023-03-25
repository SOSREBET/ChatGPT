# Introduction

The purpose of this repository is an easy way to interact with ChatGPT (with a dialog context) in python.

# Usage

Because it uses the asynchronous way of chatting with ChatGPT, you will need an asynchronous context.

```python
chat = ChatGPT()
r = await chat.ask_question(message="test")
print(r["context")

# Output: This is just a test message. Please ignore it. Thank you.
```

But also ask_question can be called with asyncio

```python
import asyncio
chat = ChatGPT()
r = asyncio.run(chat.ask_question(message="test"))
print(r["content"])

# Output: This is just a test message. Please ignore it. Thank you.
```
