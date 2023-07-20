# Client_Server_TodoList
<b>Client_Server_TodoList</b> is a simple client-server application for managing a todo list. The project consists of two main components: the server and the client. The server handles incoming client requests, while the client interacts with the server to add and retrieve todo list items.

## Features
<ul>
    <li>Add items to the todo list using the client.</li>
    <li>Retrieve the current todo list from the server using the client.</li>
    <li>End the session gracefully and save the todo list to a file on the server.</li>
</ul>

## Requirements
<ul>
    <li>Python 3.x</li>
    <li>The socket module (standard library)</li>
</ul>

Getting Started
## Clone the repository to your local machine:
<ol type=1>
    <li>
        Clone the repository to your local machine: <br>
        <b>
            git clone https://github.com/your-username/Client_Server_TodoList.git <br> 
            cd Client_Server_TodoList
        </b>
    </li>
    <li>
        Make sure you have Python 3.x installed. If not, you can download it from the official Python website:
    </li>
</ol>

## Server
The server is responsible for handling client connections and managing the todo list.

## How to Run the Server
To run the server, execute the following command in the terminal: <br>
<b>python3 todolist.py server</b> <br>
The server will start listening on port 3000 for incoming client connections.

## Client
The client allows users to interact with the server and manage the todo list.

## How to Run the Client
To run the client, execute the following command in the terminal: <br>
<b>python3 todolist.py client</b> <br>
The client will connect to the server at the specified address (by default, it connects to '127.0.0.1' on port 3000).

## Usage
<ul>
    <li>`Type start_list_session;` to begin the session and start adding items to the todo list.</li>
    <li>`Type insert list item: [your todo item]` to add an item to the list.</li>
    <li>`Type show_list;` to retrieve the current todo list from the server and display it.</li>
    <li>`Type end_list_session;` to end the session and save the todo list to the server.</li>
</ul>

# Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please create a new issue or submit a pull request.
