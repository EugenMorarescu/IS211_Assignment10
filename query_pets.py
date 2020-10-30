import sqlite3 as lite
import sys


def print_names():
    con = lite.connect('pets.db')
    ans = input("What ID are you looking for? Enter '-1' to exit \n")
    while ans != '-1':
        with con:
            try:
                cur = con.cursor()
                per_data = cur.execute("SELECT first_name,last_name,age FROM person WHERE person.id=?",[ans])
                per_rows = per_data.fetchone()
                
                pet_data = cur.execute("SELECT pet.name,pet.breed,pet.age,pet.dead FROM pet INNER JOIN person_pet ON person_pet.pet_id=pet.id INNER JOIN person ON person.id=person_pet.person_id WHERE person.id=?",[ans])
                pet_rows = pet_data.fetchall()
                
                if(per_rows==None):
                    print("That user doesn't exist, try again")
                    ans = input("What ID are you looking for? Enter '-1' to exit \n")
                
                else:
                    
                    print("{} {} who is {} years old".format(per_rows[0],per_rows[1],per_rows[2]))
                    
                    for pet_pos in pet_rows:
                                if pet_pos[3] == 1:
                                    w = 'owned'
                                    w2 = 'was'
                                else:
                                    w = 'owns'
                                    w2= 'is'
                                
                                print("{} {}, a {} that {} {} years old".format(w,pet_pos[0],pet_pos[1],w2,pet_pos[2]))
                    ans = input("What ID are you looking for? Enter '-1' to exit \n")
                    
            except lite.Error as e:
                print("Error: {}".format(e))
                sys.exit()
    con.close()

if __name__ == '__main__':
    print_names()
        
        
        