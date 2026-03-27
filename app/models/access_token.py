from dataclasses import dataclass

@dataclass
class AccessToken:
    access_token: str
    token_type: str