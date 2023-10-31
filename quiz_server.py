import socket 
from threading import Thread 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address = "127.0.0.1"
port = 8000

server.bind((ip_address, port))
server.listen()

list_of_clients = []

def clientthread(conn):
    score = 0
    conn.send("Welcome to this quiz game".encode('utf-8'))
    conn.send("You will recieve a question. The answer to that question should be one of the following")
    conn.sent("Good luck!\n\n".encode('utf-8'))
    index, question, asnwer = get_random_question_answer(conn)
    while True:
        try:
            message = conn.recv(2048).decode('utf-8')
            if message:
                if message.lower() == answer:
                    score+=1
                    conn.send("Bravo! Your score is {score}\n\n".encode('utf-8'))
                else:
                    conn.send("Inorrect answer! Better luck next time!\n\n".encode('utf-8'))
                remove_question(index)
                index,question,answer = get_random_question_answer(conn)
            else:
                remove(conn)
        except:
            continue

def get_random_question_answer(conn):
    random_index = random.randint(0, len(questions)-1)
    random_question = questions[random, index]
    random_answer = answers[random_index]
    conn.send(random_question.encode('utf-8'))
    return random_index, random_question, random_answer

def remove_question(index):
    questions.pop(index)
    answers.pop(index )