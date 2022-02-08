from syllabusbot.webscrapper import Courses
import syllabusbot.unconstants as uncons

with Courses() as bot:
    bot.land_first_page()
    bot.click_student_btn()
    bot.login()
    bot.select_username(uncons.USER)
    bot.select_username_next()
    bot.select_password(uncons.PASS)
    bot.select_password_sign_in()
    bot.manage_classes_select()
    print('Exiting...')
