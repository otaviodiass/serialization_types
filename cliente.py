import json
import socket
import dicttoxml


def format_json(conn):
    info = {'nome': 'otavio',
            'cpf': '999.888.777-66',
            'idade': '45',
            'mensagem': 'segue o comprovante de entrega.'}

    info_json = json.dumps(info)

    conn.send(info_json.encode())


def format_csv(conn):
    info = [['nome', 'otavio'],
            ['cpf', '999.888.777-66'],
            ['idade', '45'],
            ['mensagem', 'segue o comprovante de entrega.']]

    info_csv = '\n'.join([','.join(linha) for linha in info])

    conn.send(info_csv.encode())


def format_xml(conn):
    info = {'nome': 'otavio',
            'cpf': '999.888.777-66',
            'idade': '45',
            'mensagem': 'segue o comprovante de entrega.'}

    info_xml = dicttoxml.dicttoxml(info)

    conn.send(info_xml)


def format_yaml(conn):
    info = """
    nome: otavio,
    cpf: 999.888.777-66,
    idade: 45,
    mensagem: segue o comprovante de entrega.
    """

    conn.send(info.encode())


def format_toml(conn):
    info = """
    nome = "otavio"
    cpf = "999.888.777-66"
    idade = "45"
    mensagem = "segue o comprovante de entrega."
    """

    conn.send(info.encode())


HOST = 'localhost'
PORTA = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORTA))

format_json(s)
format_csv(s)
format_xml(s)
format_yaml(s)
format_toml(s)
