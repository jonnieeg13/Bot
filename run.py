from syllabusbot.courses import Courses
import syllabusbot.unconstants as uncons
import syllabusbot.constants as cons

try:
    with Courses() as bot:
        bot.land_first_page()
        bot.click_student_btn()
        bot.login()
        bot.select_username(uncons.USER)
        bot.select_username_next()
        bot.select_password(uncons.PASS)
        bot.select_password_sign_in()
        bot.manage_classes_select()
        bot.refresh()
        bot.extract_classes()
        print('Exiting...')
except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            f'    set PATH=%PATH%;{cons.DRIVER_PATH} \n \n'
            'Linux: \n'
            f'    PATH=$PATH:{cons.DRIVER_PATH}')
    else:
        raise
