import csv
import json
import socket
import dicttoxml
import toml
import yaml


def json_format(msg, c):
    msg_json = json.loads(msg)
    print(msg_json)
    c.close()


def csv_format(msg, c):
    linhas = msg.split('\n')
    dados_recebidos = csv.reader(linhas)
    for i in dados_recebidos:
        print(i)
    c.close()


def xml_format(msg, c):
    x = dicttoxml.dicttoxml(msg)
    print(x)
    c.close()


def yaml_format(msg, c):
    print(yaml.dump(yaml.load(msg, Loader=yaml.SafeLoader)))
    c.close()


def toml_format(msg, c):
    f = toml.loads(msg)
    x = toml.dumps(f)
    print(x)
    c.close()


HOST = 'localhost'
PORTA = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORTA))
s.listen()

vet = []

print("Aguardando conexão de um cliente")

conn, end = s.accept()

print("Conectado em :", end)

while True:
    data = conn.recv(2048).decode()

    json_format(data, conn)
    csv_format(data, conn)
    xml_format(data, conn)
    yaml_format(data, conn)
    toml_format(data, conn)
    break
