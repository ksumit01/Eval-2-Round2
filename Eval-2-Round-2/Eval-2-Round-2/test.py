class TestApp(unittest.TestCase):
  def test_add(self):
    self.app = app.test_client()

def test_add():
  self.app = app.test_client()
  self.assertEqual(200, self.app.get("/add").status_code)

  def test_deletePost():
    self.app = app.test_client()
    self.assertEqual(200, self.app.get("/deletePost").status_code)

  if __name__ == "__main__":
    unittest.main() 