from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"message": "OK"}


class TestSummariesEndpoint:
    big_text_msg = "This message is a random text message to test the endpoint returns exactly ten words, if the length of the text is greater than ten words."
    small_text_msg = "This is a small text message."

    def test_return_empty_string_when_no_text(self):
        response = client.post("/summaries", json={"text": ""})
        assert response.status_code == 200
        result = response.json()
        assert result["summary"] == ""

    def test_return_full_text_when_text_is_short(self):
        response = client.post("/summaries", json={"text": self.small_text_msg})
        assert response.status_code == 200
        result = response.json()
        assert result["summary"] == self.small_text_msg

    def test_return_exactly_ten_words_if_text_is_long(self):
        response = client.post(
            "/summaries",
            json={"text": self.big_text_msg},
        )
        assert response.status_code == 200
        result = response.json()
        assert len(result["summary"].split(None)) == 10

    def test_has_timestamp(self):
        response = client.post(
            "/summaries",
            json={"text": self.small_text_msg},
        )
        assert response.status_code == 200
        result = response.json()
        assert "timestamp" in result
