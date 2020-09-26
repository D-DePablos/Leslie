import json 
import getpass

def create_secrets():
    """
    Simple utility to prompt user for api_key and secret_key
    """
    api_key = input("Please include your api key here: ")

    if api_key.lower() != 'n':
        secret_key = getpass.getpass("Please include your secret key: ")

        _secrets = {"API_KEY": api_key,
                    "SECRET_KEY": secret_key}
        
        with open("Secrets.json", "w") as file:
            json.dump(_secrets, file)
            print("Successfully saved all your secrets...")

    else:
        print("It appears you have no more secrets to record.")


def main():
    create_secrets()


if __name__ == '__main__':
    main()
