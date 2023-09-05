while True:
    try:
        from random import choice
        from py_rpautom.python_utils import cls


        def print_message_division(size: int):
            message_symbol = '*'
            print(message_symbol, '----' * size, message_symbol)

        ROCK_CHOICE = 'ROCK'
        PAPER_CHOICE = 'PAPER'
        SCISSORS_CHOICE = 'SCISSORS'
        CONTINUE_Y = 'Y'
        CONTINUE_N = 'N'

        choice_options = [
            ROCK_CHOICE,
            PAPER_CHOICE,
            SCISSORS_CHOICE,
        ]

        intro_message = (
            'Hi!',
            '\n',
            'Choice between "Rock", "paper" or "scissors" '
            'and see if you win of the CPU player.',
        )
        input_choise_message = 'Type your choice, please: '
        input_continue_message = 'Continue? (Y / N) '
        return_user_chose = 'You chose'
        return_cpu_chose = 'CPU chose'
        invalid_choice = 'Choice only between "Rock", "paper" or "scissors"!'
        win_message = 'You win! Contratulations!!!'
        lose_message = 'CPU win! But you can to win in the next turn!'
        draw_message = 'Draw! Good move!'

        cls()

        print('\n')
        print_message_division(size = 30)
        for line_message in intro_message:
            print(line_message)
        print_message_division(size = 30)
        print('\n')

        user_choice = str(input(input_choise_message))
        cpu_choice = choice(choice_options)

        if user_choice.upper() == ROCK_CHOICE:
            print(return_user_chose, ROCK_CHOICE)

            if cpu_choice.upper() == PAPER_CHOICE:
                print(return_cpu_chose, PAPER_CHOICE)
                print(lose_message)
            elif cpu_choice.upper() == SCISSORS_CHOICE:
                print(return_cpu_chose, SCISSORS_CHOICE)
                print(win_message)
            else:
                print(return_cpu_chose, cpu_choice.upper())
                print(draw_message)
        elif user_choice.upper() == PAPER_CHOICE:
            print(return_user_chose, PAPER_CHOICE)

            if cpu_choice.upper() == ROCK_CHOICE:
                print(return_cpu_chose, ROCK_CHOICE)
                print(win_message)
            elif cpu_choice.upper() == SCISSORS_CHOICE:
                print(return_cpu_chose, SCISSORS_CHOICE)
                print(lose_message)
            else:
                print(return_cpu_chose, cpu_choice.upper())
                print(draw_message)
        elif user_choice.upper() == SCISSORS_CHOICE:
            print(return_user_chose, SCISSORS_CHOICE)

            if cpu_choice.upper() == PAPER_CHOICE:
                print(return_cpu_chose, PAPER_CHOICE)
                print(win_message)
            elif cpu_choice.upper() == ROCK_CHOICE:
                print(return_cpu_chose, ROCK_CHOICE)
                print(lose_message)
            else:
                print(return_cpu_chose, cpu_choice.upper())
                print(draw_message)
        else:
            raise ValueError(
                invalid_choice
            )
    except Exception as error:
        print('Message of error:', str(error))
    finally:
        continue_validation = False
        while continue_validation is False:
            print('\n')
            continue_option = str(input(input_continue_message))

            if continue_option.upper() == CONTINUE_Y:
                continue_validation = True
            elif continue_option.upper() == CONTINUE_N:
                exit(0)
