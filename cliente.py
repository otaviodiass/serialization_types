import csv
import json
import socket
import dicttoxml


def format_json(conn):
    info = {'nome': 'otavio',
            'cpf': '999.888.777-66',
            'idade': '45',
            'mensagem': 'segue o comprovante de entrega.'}

    info_json = json.dumps(info)

    conn.send(f'json@{info_json}'.encode())


def format_csv(conn):
    with open(info.csv) as arq:
        info_csv = csv.writer(arq)

    conn.send(f'csv@{info_csv}'.encode())


def format_xml(conn):
    info = {'nome': 'otavio',
            'cpf': '999.888.777-66',
            'idade': '45',
            'mensagem': 'segue o comprovante de entrega.'}

    info_xml = dicttoxml.dicttoxml(info)

    conn.send(f'xml@{info_xml}'.encode())


def format_yaml(conn):
    info = """
    nome: otavio,
    cpf: 999.888.777-66,
    idade: 45,
    mensagem: segue o comprovante de entrega.
    """

    conn.send(f'yaml@{info}'.encode())


def format_toml(conn):
    info = """
    nome = "otavio"
    cpf = "999.888.777-66"
    idade = "45"
    mensagem = "segue o comprovante de entrega."
    """

    conn.send(info.encode())


HOST = 'localhost'
PORTA = 3544

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORTA))

format_json(s)
dado = s.recv(2048).decode()
if dado == 'ok':
    format_csv(s)

dado = s.recv(2048).decode()
if dado == 'ok':
    format_xml(s)

dado = s.recv(2048).decode()
if dado == 'ok':
    format_yaml(s)

dado = s.recv(2048).decode()
if dado == 'ok':
    format_toml(s)