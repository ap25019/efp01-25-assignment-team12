#main.py

from services import MovieManager

def main():
    manager = MovieManager()
    print("Καλωσήρθατε στο σύστημα PyFlix ")

    while True:
        print("\n1. Αναζήτηση Ταινίας/Σειράς")
        print("2. Είσοδος Διαχειριστή & Προσθήκη Περιεχομένου")
        print("0. Έξοδος")

        choice = input("Επιλογή: ")

        if choice == "1":

            search_title = input("Δώστε τον τίτλο της ταινίας/σειράς: ")
            result = manager.search_tittle(search_title)

            if result:
                print("\n---ΒΡΕΘΗΚΕ---")
                print(f"Τίτλος: {result.title}")
                print(f"Ημερομηνία: {result.release_dates}") 
                print(f"Περίληψη: {result.storyline}")
                print(f"Βαθμολογία: {result.avr_rating}/10")

                if result.directors: 
                    for director in result.directors:
                        print(f"Σκηνοθέτης: {director.full_name}")
                
                if result.cast:
                    for actor in result.cast:
                        print(f"Ηθοποιοί: {actor.full_name}")

            else:
                print("\n Δεν βρέθηκε τέτοιο έργο!!.\n")

            
        elif choice == "2":
            print("\n--- ΣΥΝΔΕΣΗ ΔΙΑΧΕΙΡΙΣΤΗ ---")
            
            if manager.login():
                while True:
                    print("\n=== ΜΕΝΟΥ ΔΙΑΧΕΙΡΙΣΤΗ ===")
                    print("1. Προσθήκη Ταινίας")
                    print("2. Προσθήκη Σειράς")
                    print("3. Προσθήκη Ηθοποιού/Σκηνοθέτη & σύνδεση με έργο")
                    print("0. Αποσύνδεση (Επιστροφή στο Αρχικό Μενού)")

                    admin_choice = input("Επιλογή Διαχειριστή: ")

                    if admin_choice == "1":
                        print("\n--- Καταχώρηση Νέας Ταινίας ---")
                        new_title = input("Δώσε τίτλο: ")
                        new_release_date = input("Πότε βγήκε η ταινία; ")
                        new_story = input("Δώσε περίληψη: ")
                    
                        manager.add_work(new_title,new_release_date,new_story,[],0.0)
                        print(f"Η ταiνία με όνομα '{new_title}' καταχωτήθηκε με επιτυχία!")


                    elif admin_choice == "2":
                        print("\n--- Καταχώρηση Νέας Σειράς ---")
                        new_title = input("Δώσε τίτλο: ")
                        new_release_date = input("Πότε βγήκε η σειρά; ")
                        new_story = input("Δώσε περίληψη: ")
                        new_last_air_date = input("Ημερομηνία τελευταίας προβολής: ")
                        new_season_count = input("Πόσες σεζόν θα έχει; ")
                        new_episodes_count = input("Πόσα επεισόδια έχει στο σύνολο; ")
                    
                        manager.add_serie(new_title,new_release_date,new_story,[],0.0,new_last_air_date,new_season_count,new_episodes_count)
                        print(f"Η σειρά με όνομα '{new_title}' καταχωτήθηκε με επιτυχία!")


                    elif admin_choice == "3":
                        print("\n--- Καταχώρηση Ηθοποιού/Σκηνοθέτη ---")

                        new_name = input("Ονοματεπώνυμο: ")
                        new_date = input("Ημερομηνία Γέννησης: ")
                        new_place = input("Τόπος Γέννησης: ")
                        new_web = input("Ιστοσελίδα: ")
                        new_bio = input("Σύντομο Βιογραφικό: ")

                        manager.add_person(new_name,new_date,new_place,new_web,new_bio)
                        print(f"Η σειρά με όνομα '{new_name}' καταχωτήθηκε με επιτυχία!")\

                        print("--- Σύνδεση με Έργο ---")
                        w_title = input(f"Σε ποια ταινία/σειρά συμμετέχει ο/η {new_name}; (Δώσε τίτλο): ")
                        print("Τι ρόλο έχει;")
                        print("1. Ηθοποιός")
                        print("2. Σκηνοθέτης")
                        role = input("Επιλογή (1 ή 2): ")
                        
                        manager.link_person_to_work(new_name, w_title, role)
                        print(f" Ο/Η {new_name} συνδέθηκε με το '{w_title}'.")


                    elif admin_choice == "0":
                        print("Επιστροφή στο κεντρικό μενού!!!.")
                        break 
                    
                    else:
                        print("Λάθος επιλογή, προσπάθησε ξανά.")
                        

        elif choice == '0':
            print("Καλή συνέχεια σας περιμενουμε συντομα!")
            break 

        else:
            print("Κατι πάτησες λάθος ξαναπροσπάθησε!!")



if __name__ == "__main__":
    main()
