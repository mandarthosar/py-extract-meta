def getDomain(email):
    domain = email[email.index("@")+1:]
    return domain