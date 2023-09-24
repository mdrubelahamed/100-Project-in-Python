#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("project 23/Input/Letters/starting_letter.txt") as mail_head, open("project 23/Input/Names/invited_names.txt") as invited_names:
    mail_contents = mail_head.read()
    name_list = invited_names.readlines()


    for name in name_list:
        name = name.strip("\n")
        final_mail = mail_contents.replace("[name]", name)

        with open(f"project 23/Output/ReadyToSend/letter_for_{name}.txt", mode="w") as readyToSendMail:
            readyToSendMail.write(final_mail)

