from app import app

def test_home_status_code():
    tester = app.test_client()
    response = tester.get('/api/books')  # hoặc endpoint nào bạn muốn test
    assert response.status_code == 200
