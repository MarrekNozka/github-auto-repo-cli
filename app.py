from create_repo import create_repo

prompt = '> '

conf = False

while conf is False:
    for i in range(5):
        abs_path = input("\n[ABSOLUTE PATH]" +
                         "\n(for example: /home/jack/Desktop)\n" +
                         "(paths are case sensitive)\n" +
                         f"\n{prompt}")
        if not abs_path:
            print("** You have to provide an absolute " +
                  "path for the repository **")
            continue
        else:
            break
    else:
        print("\nTOO MANY INVALID ATTEMPTS, TRY AGAIN.")
        break
    for i in range(5):
        repo_name = input("\n[REPOSITORY NAME]\n" +
                          prompt)
        if not repo_name:
            print("** You have to provide a name for the repository **")
            continue
        elif ' ' in repo_name:
            print("** A repo's name must not include white space\n"
                  "Please, seperate words with dashes/underscores **")
            continue
        else:
            break
    else:
        print("\nTOO MANY INVALID ATTEMPTS, TRY AGAIN.")
        break

    create_repo(abs_path, repo_name)
    conf = True
