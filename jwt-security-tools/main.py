from api_gateway.gateway import APIGateway
from token_manager.manager import TokenManager

if __name__ == "__main__":
    secret = ""
    manager = TokenManager(secret)
    access_token, refresh_token = manager.generate_tokens("thang")

    print("Access Token:", access_token)
    print("Refresh Token:", refresh_token)

    gateway = APIGateway(secret)
    gateway.run()