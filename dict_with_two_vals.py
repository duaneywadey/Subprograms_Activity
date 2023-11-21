# Accessing a key with two values

reg_users_and_password = {
    "user_1": ["admin1234", 20000],
    "user_2": ["admin1234", 20000],
    "user_3": ["admin1234", 20000],
    "user_4": ["admin1234", 20000],
}

first_value = reg_users_and_password.get("user_1")

# Getting the username only
get_user = first_value[0]
print(get_first)

# Getting the balance olny
get_bal = first_value[1]
print(get_first)