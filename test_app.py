from app import app

def test_index():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
