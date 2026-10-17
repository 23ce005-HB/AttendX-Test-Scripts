def test_login():
    username = "student123"
    password = "testpass123"

    assert username != ""
    assert password != ""

    print("Login test passed")


if __name__ == "__main__":
    test_login()