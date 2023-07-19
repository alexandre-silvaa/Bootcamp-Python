import requests 
import unittest
import json

# Teste de API - Cadastrando e editando usário 
class TestAPI(unittest.TestCase):
    def test_createEdit(self):
        """ CADASTRANDO USUÁRIO """
        url ='http://127.0.0.1:5000/users/create'

        # dados a serem cadastrados
        payload = {
            'name':'name',
            'age':'age',
            'address':'address'
        }
        headers = {'Content-Type':'application/json'}
        response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
        data = response.json()[0]

        print(data)

        self.assertEqual(data['name'], payload['name'])
        self.assertEqual(data['age'], payload['age'])
        self.assertEqual(data['address'], payload['address'])

        """ EDITANDO USUÁRIO CADASTRADO """
        id = data['id']
        url =f'http://127.0.0.1:5000/users/edit/{id}'

        # dados a serem editados
        payload = {
            'name':'name2',
            'age':'age2',
            'address':'address2'
        }

        response = requests.request("PUT", url, headers=headers, data=json.dumps(payload))
        data = response.json()

        print(data)

        self.assertEqual(data['OK'], 'Usuário alterado com sucesso!')

