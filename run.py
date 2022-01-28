from syllabusbot.webscrapper import Courses


with Courses() as bot:
    bot.land_first_page()
    print('Exiting...')
