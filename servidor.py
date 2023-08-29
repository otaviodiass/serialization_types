import csv
import json
import socket
import dicttoxml
import toml
import yaml


def json_format(msg):
    msg_json = json.loads(msg)
    print('Json')
    print(msg_json)
    print()


def csv_format(msg):
    print('CSV')
    linhas = msg.split('\n')
    dados_recebidos = csv.reader(linhas)
    for i in dados_recebidos:
        print(i)
    print()


def xml_format(msg):
    x = dicttoxml.dicttoxml(msg)
    print('Xml')
    print(x)
    print()


def yaml_format(msg):
    print('Yaml')
    print(yaml.dump(yaml.load(msg, Loader=yaml.SafeLoader)))
    print()


def toml_format(msg):
    print('Toml')
    f = toml.loads(msg)
    x = toml.dumps(f)
    print(x)


HOST = 'localhost'
PORTA = 3544

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORTA))
s.listen()

print("Aguardando conexão de um cliente")

conn, end = s.accept()

print("Conectado em :", end)

while True:
    data = conn.recv(2048).decode()

    if data.split('@')[0] == 'json':
        json_format(data.split('@')[1])
        conn.sendall('ok'.encode())
    elif data.split('@')[0] == 'info.csv':
        csv_format(data.split('@')[1])
        conn.sendall('ok'.encode())
    elif data.split('@')[0] == 'xml':
        xml_format(data.split('@')[1])
        conn.sendall('ok'.encode())
    elif data.split('@')[0] == 'yaml':
        yaml_format(data.split('@')[1])
        conn.sendall('ok'.encode())
    else:
        toml_format(data)
        break
