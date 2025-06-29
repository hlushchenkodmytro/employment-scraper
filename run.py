from employment.employment import Employment

with Employment() as bot:
    bot.land_first_page()         # Open the main page
    bot.cookie_skip()             # Skip cookie popup

    bot.report_requirements_all_pages()  # Disabled for now

    bot.save_to_excel()           # Save results to Excel
    print(bot.vacancies)          # Print vacancies list

    input("Done. Press Enter to close the browser...")