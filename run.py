from syllabusbot.courses import Courses
import syllabusbot.unconstants as uncons

try:
    with Courses(teardown=True) as bot:
        bot.land_first_page()
        bot.click_student_btn()
        bot.login()
        bot.select_username(uncons.USER)
        bot.select_username_next()
        bot.select_password(uncons.PASS)
        bot.select_password_sign_in()
        bot.bot_wait()
        bot.manage_classes_select()
        bot.refresh()
        bot.extract_classes()
        print('Exiting ...')
except Exception as e:
    raise
