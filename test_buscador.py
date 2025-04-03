import unittest
from buscador_articulos import app

class TestBuscadorArticulos(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_busqueda_valida(self):
        response = self.app.get('/buscar?q=IA')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Introduccion a la IA", response.get_data(as_text=True))

    def test_busqueda_sin_resultados(self):
        response = self.app.get('/buscar?q=xyz123')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), [])

    def test_busqueda_vacia(self):
        response = self.app.get('/buscar?q=')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.get_json()) > 0)

if __name__ == '__main__':
    unittest.main()
