import unittest
import requests

class TestOllamaService(unittest.TestCase):

    
    def test_estimae_tokens(self):
        text = "FastAPI will use this response_model to do all the data documentation, validation, etc"
        response = requests.post("http://localhost:8000/estimate_tokens/", json={"content": text})
        nb_tokens = int(response.json()["nb_tokens"])
        
        self.assertEqual(nb_tokens, 16)


    def test_available_models(self):
        available_models = requests.get("http://localhost:8000/get_models/").json()["available_models"]
        
        self.assertIsInstance(available_models, list)


    def test_generate_questions(self):
        model_name = "phi3:latest"
        text = "FastAPI will use this response_model to do all the data documentation, validation, etc"
        response = requests.post("http://localhost:8000/generate_questions/", json={"model_name": model_name, "content": text})
        questions = response.json()["questions"]

        self.assertIsInstance(questions, list)


if __name__ == '__main__':
    unittest.main()