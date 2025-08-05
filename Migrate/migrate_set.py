import sqlite3 as sq
class MigrateSet:
    def add_student(name, surname, rating):
       with sq.connect("Академия_65.db") as base:
           cursor = base.cursor()
           cursor.execute('''
INSERT INTO "Students"("имя","фамилия","рейтинг") VALUES (?,?,?)


''',(name, surname, rating))


    def add_teacher(name, surname, salary):
       with sq.connect("Академия_65.db") as base:
           cursor = base.cursor()
           cursor.execute('''
INSERT INTO "Teacher"("имя","фамилия","ставка") VALUES (?,?,?)


''',(name, surname, salary))
           
    def delete_teacher(id):
       with sq.connect("Академия_65.db") as base:
           cursor = base.cursor()
           cursor.execute('''
DELETE FROM Teacher WHERE id=?


''',(id,))
           

    def delete_student(id):
       with sq.connect("Академия_65.db") as base:
           cursor = base.cursor()
           cursor.execute('''
DELETE FROM Students WHERE id=?


''',(id,))
           
    def change_teacher(name, surname, salary, id):
        with sq.connect("Академия_65.db") as base:
           cursor = base.cursor()
           cursor.execute('''
UPDATE Teacher
SET имя = ?,
    фамилия = ?,
    ставка = ?
WHERE id = ?


''',(name, surname, salary, id))

MigrateSet.change_teacher("Василий", "Прокофьев", 99000, 3)

