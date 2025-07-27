***Functional Test Cases
Greeting Test:
Input: "Hello"
Expected Output: Agent should reply with a friendly greeting like "Hi there!" or "Hello! How can I help you?"

Capital City Test – India:
Input: "What is the capital of India?"
Expected Output: "The capital of India is New Delhi."

Capital City Test – France:
Input: "What is the capital of France?"
Expected Output: "The capital of France is Paris."

Unknown Question Test:
Input: "Who won IPL 2017?"
Expected Output: A generic fallback message like "Sorry, I don’t have an answer for that."

Time Response Test:
Input: "Tell me the time"
Expected Output: Agent should return current system time.

Agent Identity Test:
Input: "What is your name?"
Expected Output: "I am your AI Agent Assistant 🤖"

Empty Query Test:
Input: Blank or whitespace
Expected Output: Agent should respond with a message like "Sorry, I couldn't understand that."

*** API Test Cases
/query Endpoint Test:
Send a POST request to /query with a sample question in JSON format.
Expected Output: JSON response containing an appropriate answer string.

/agent Endpoint Test:
Send a POST request to /agent with { "name": "TestAgent" }.
Expected Output: Confirmation message: "Agent 'TestAgent' created successfully".

/logs Endpoint Test:
Send a GET request to /logs.
Expected Output: JSON array containing all previous queries and responses stored in MongoDB.

***MongoDB Test Cases
Log Entry Creation Test:
After sending a query, check MongoDB (ai_agent > logs collection).
Expected: New document should be inserted with fields: query, response, and timestamp.

Log View Test:
Use MongoDB Compass or shell to view the logs.
Expected: All past queries with corresponding AI responses should be visible.

***Frontend UI Test Cases
Chat UI Load Test:
Open the browser at http://127.0.0.1:5000.
Expected: Chat interface with input box and "Send" button loads properly.

Message Send/Receive Test:
Enter any question and click "Send".
Expected: User message and agent response appear on the chat window instantly.

Chat Scroll Test:
Send multiple messages.
Expected: Chat window should scroll automatically to show latest messages.


***Notes:
All test cases were manually tested and successfully passed.
This confirms that the system works as expected in both backend and frontend.
The agent logic can handle basic intelligence and fallback cases, fulfilling the challenge requirements.











