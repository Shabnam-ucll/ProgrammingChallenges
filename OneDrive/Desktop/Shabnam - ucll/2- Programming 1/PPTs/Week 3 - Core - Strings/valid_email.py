
def valid_email(email):
    # It must contain an @, which cannot be at the first position
    index_at = email.find("@")
    if index_at <=0:
        return f"{email} is invalid"
    # There must be at least one letter after the @
    ## first check if @ is at the last position, to avoid 'index out of range'
    index_last = len(email) - 1 
    if index_at == index_last:
        return f"{email} is invalid"
    ## then check if the one character after @ is a letter
    if not 'a' <= email[index_at+1].lower() <= 'z':
        return f"{email} is invalid"
    # The address must end with a . followed by exactly 2 characters
    if email[-3] != '.':
        return f"{email} is invalid"
    # We survived all the condition-checks!
    return f"{email} is valid"

print(valid_email("test@example.be"))       # Valid
print(valid_email("@example.be"))           # Invalid
print(valid_email("test@"))                 # Invalid 
print(valid_email("test@.be"))              # Invalid 
print(valid_email("test@example.com"))      # Invalid

