
# Jyoti (AI personal assistaint)

Jyoti is a user-friendly personal AI assistant that works on your terminal. It is not only capable of answering general knowledge questions, but can also help in various tasks like setting reminders, sending emails, checking the weather, and more. The core strength of Jyoti comes from the powerful ChatGPT by OpenAI, making it reliable and efficient.
## Features and Commands

- **'Hello Jyoti':** To greet and activate the assistant.
- **'Tell me a joke':** Jyoti will share a random joke.
- **'[Any General Knowledge Question]'**: Jyoti will try to provide an answer.
- More commands and features will be added in future updates.

## Implementation

### Prerequisites:
- Python **3.xx** or above installed
- OpenAI API key ([OpenAI's official website](https://www.openai.com/))

### Installation and Steps:
#### Step 1
*Clone the Repository:*
```bash
  git clone https://github.com/suparnobanerjee/jyoti.git
```
#### Step 2
*Navigate to the Directory:*
```bash
  cd jyoti
```
#### Step 3
*Install Required Libraries:*
```bash
  pip install openai colorama
```

#### Step 4
*Set up the OpenAI API Key:*
- *Save your API key in a file named ***'.env'*** in the root directory of the project with the following format:*
```bash
  OPENAI_API_KEY='Your-API-Key-Here'
```
#### Step 5
*Run the Assistant:*
```bash
  python main.py
```
**Note :** The code will address user with my name as it was intended to use by me, so feel free to tweak this code slightly before use.


