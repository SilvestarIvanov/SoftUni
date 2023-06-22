class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


# emails = []
# data = input()

# while data != "Stop":
#     sender, receiver, content = data.split()
#     email = Email(sender, receiver, content)
#     emails.append(email)
#     data = input()
#
# indexes_of_emails = [int(el) for el in input().split(", ")]
# for index, email in enumerate(emails):
#     if index in indexes_of_emails:
#         emails[index].send()
#     print(f"{email.sender} says to {email.receiver}: {email.content}. Sent: {email.is_sent}")
#

emails = []
indices = []
while True:
    data = input().split()
    if data[0] == "Stop":
        break
    sender, receiver, content = data
    email = Email(sender, receiver, content)
    emails.append(email)

indices = [int(i) for i in input().split(", ")]

for index in indices:
    if 0 <= index < len(emails):
        emails[index].send()
for email in emails:
    print(email.get_info())
