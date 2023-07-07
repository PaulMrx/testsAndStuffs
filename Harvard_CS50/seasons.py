from datetime import date
import inflect

def main():
    """inputs"""
    birthday = date.fromisoformat(input("What is you birth date? "))
    today = date.today()
# birthday = date(1986, 2, 20)

    p = inflect.engine()

    time_to_birthday = abs(birthday - today)
    days = time_to_birthday.days
    minutes = p.number_to_words(days * 24 * 60)
    print(f"You've lived for {minutes} minutes!")

if __name__=="__main__":
    main()






