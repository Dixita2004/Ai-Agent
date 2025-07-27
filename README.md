Chatboard

->This is a smart AI agent backend project created as part of the "Tacules Screening Test". The project is build using Flask(python),MongoDB,HTML and JavaScript.It simulates a basic AI assistant capable of answering questions, storing logs and providing a chat-based interface.


Features
--Responds to user questions using custom gpt-style logic
--flask APIs for submitting queries and getting responses
--MongoDB database stores all chat logs
--Simple HTML + JavaScript fronted for chatting
--Expandable structure for future integration with OpenAI APIs


Tech Stack
--Backend:Python,Flask,Flask-CORS
--Database:MongoDB
--Frontend:HTML,JavaScript


Project Structure
----chatboard/
  |-app.py(flask API app)
  |-Chatboard_logic.py(custom AI logic)
  |-database.py(mongodb connection)
  |-model.py(chat log formatter)
  |-requirement.txt(python packages)
  |-README.md(project documentation)
  |-templates/
     |-index.html(fronted HTML)
  |-static/
     |-script.js(frontend js)


Setup Instructions

1.Install python 

2.pip install -r requirements.txt

-packages
 Flask
flask-cors
pymongo
dnspython


3.start MongoDB
-momgoDB install 
connect to: mongodb://localhost:27017

start command 
-mongod

run the flask application
-python app.py

visit in browser
-http://127.0.0.1:5000



How to use
-open the web page
-type a question("ex..What is the capital of india?")
-press send
-get AI-style answer on screen


Available API Endpoints


Method      Route     Description

Get         /         Load fronted HTML chat pagew
POST        /query    send query,get response
POST        /agent    create agent setup 
GET         /logs     view stored chat logs




Question to ASK
-Who is the president of India?
-What is the capital of japan?
-Tell me the time?
-Hello
-what is the capital of Germany?

and get answer


logs in mongoDB
-Database:ai_agent
-collection:logs



Notes:

-This project does NOT require OpenAI API
-Logic is written in chatboard_logic.py using keyword-based processing
-easily expendable with GPT-4, gemini API etc
