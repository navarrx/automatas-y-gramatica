import re
email_regex = r'\b[A-Za-z][A-Za-z0-9._-]+@(?:[A-Za-z0-9]+\.)+(com|gov|edu|net|org)\.(ar|us|uk|br|cl)\b'
alert = "The accepted organization types are: com - gov - edu - net - org"
alert2 = "\nThe allowed countries are: ar - us - uk - br - cl"
alert3 = "\nEmail format is: [name]@[organization].[domain].[country]"
print(alert, alert2, alert3)


def email_evaluator():
    email = str(input("\nInsert your email here: "))
    if re.fullmatch(email_regex, email):
        print(f'The email "{email}" is approved!')
    else:
        print(f'The email "{email}" is denied. Please try again')


email_evaluator()
