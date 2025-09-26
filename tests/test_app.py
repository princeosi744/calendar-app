from app import app

def test_home():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b"Calendar App" in response.data

def test_calendar():
    response = app.test_client().get('/calendar')
    assert response.status_code == 200
    data = response.get_json()
    assert "month" in data
    assert "year" in data
    assert "days" in data
