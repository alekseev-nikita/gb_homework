import re


def email_pars(email_address):
    user, domain = re.split('@', email_address)
    RE_DOMAIN = re.compile(r'[a-z]+\.[a-z]{2,3}$')
    if not RE_DOMAIN.match(domain):
        raise ValueError(f'wrong email: {domain}')
    data = {'user': user, 'domain': domain}
    print(data)


email_pars('someone@geekbrains.ru')

