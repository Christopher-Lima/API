from passlib.context import CryptContext

pass_context = CryptContext(schemes=['bcrypt'])

def generate_hash(text):
    return pass_context.hash(text)

def check_hash(text, hash):
    return pass_context.verify(text, hash)