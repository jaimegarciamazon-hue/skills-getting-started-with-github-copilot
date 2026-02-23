import random
import string

def random_email():
    return (
        "test_" + ''.join(random.choices(string.ascii_lowercase, k=8)) + "@mergington.edu"
    )

def test_signup_and_unregister_participant(client):
    # Arrange
    email = random_email()
    activity = "Chess Club"

    # Act - Signup
    signup_resp = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert - Signup
    assert signup_resp.status_code == 200
    signup_data = signup_resp.json()
    assert f"Signed up {email} for {activity}" in signup_data["message"]

    # Act - Unregister
    unregister_resp = client.delete(f"/activities/{activity}/unregister?email={email}")

    # Assert - Unregister
    assert unregister_resp.status_code == 200
    unregister_data = unregister_resp.json()
    assert f"Removed {email} from {activity}" in unregister_data["message"]
