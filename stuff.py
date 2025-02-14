from csv import reader
from requests import post, codes

with open('app/PORT_CONFIG.txt') as f:
    PORT = int(f.read().strip())
LOGIN_URL = f"http://localhost:{PORT}/login"

PLAINTEXT_BREACH_PATH = "app/scripts/breaches/plaintext_breach.csv"

def load_breach(fp):
    with open(fp) as f:
        r = reader(f, delimiter=' ')
        header = next(r)
        assert(header[0] == 'username')
        return list(r)

def attempt_login(username, password):
    response = post(LOGIN_URL,
                    data={
                        "username": username,
                        "password": password,
                        "login": "Login",
                    })
    return response.status_code == codes.ok

def credential_stuffing_attack(creds):
    # TODO: return a list of credential pairs (tuples) that can successfully login
    pass

def main():
    creds = load_breach(PLAINTEXT_BREACH_PATH)
    print(credential_stuffing_attack(creds))

if __name__ == "__main__":
    main()
