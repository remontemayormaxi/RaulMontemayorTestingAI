from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest

class TestBusquedaArticulos(unittest.TestCase):
    def setUp(self):
        # Configurar el navegador (requiere ChromeDriver o GeckoDriver)
        self.driver = webdriver.Chrome()  # O usa webdriver.Firefox() si prefieres Firefox
        self.driver.get("http://127.0.0.1:5000")  # URL del sistema local

    def test_busqueda_articulo(self):
        driver = self.driver
        search_box = driver.find_element(By.NAME, "q")  # Suponiendo que el campo de búsqueda tiene name="q"
        search_box.send_keys("IA")
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)  # Esperar que carguen los resultados
        
        resultados = driver.find_elements(By.CLASS_NAME, "resultado")  # Suponiendo que los resultados tienen esta clase
        self.assertTrue(len(resultados) > 0, "No se encontraron resultados en la búsqueda")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
