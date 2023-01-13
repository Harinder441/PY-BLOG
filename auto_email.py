# Learnings
## from yahoo
import smtplib


def send_mail(to_ad="harindersingh2107@gmail.com", massage="",from_ad="harryautoemail@gmail.com", password="dgtkeudhnbowvhli"):
    with smtplib.SMTP("smtp.gmail.com") as con:
        # securing
        con.starttls()
        # login
        con.login(user=from_ad, password=password)
        con.sendmail(from_addr=from_ad, to_addrs=to_ad, msg=massage)


if __name__ == "__main__":
    my_email = "harryautoemail@gmail.com"
    passw = "dgtkeudhnbowvhli"
    msg = "Subject:Hello Sahil \n\n greeting from Harry auto mail"
    to = "basant29082001@gmail.com"
    i = 1
    while (i < 100):
        msg = f"Subject:Hello{i} Basant Singh \n\n greeting from Harry auto mail {i}"
        # send_mail(massage=msg)
        i += 1
