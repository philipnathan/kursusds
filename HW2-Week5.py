import mysql.connector

database_movie = (
    mysql
    .connector
    .connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'online_movie_rating'
    )
)

def drop_table(database, table_name):
    drop_query = (
        f"""
        DROP TABLE IF EXISTS {table_name}
        """
    )
    cursor = database.cursor()
    cursor.execute(drop_query)
    database.commit()
    print('table has been dropped!')

def create_table(database):
    movies_table_query = (
    """
        CREATE TABLE movies(
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(100),
        release_year YEAR(4),
        collection_in_mil_dol INT
        )
        """
    )

    reviewer_table_query = (
        """
        CREATE TABLE reviewers(
        id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(100),
        last_name VARCHAR(100)
        )
    """
    )

    cursor = database.cursor()
    cursor.execute(movies_table_query)
    cursor.execute(reviewer_table_query)
    database.commit()
    print('create tables have done!')

def insert_data(database, movie_list):
    insert_query = (
        """
        INSERT INTO movies (title, release_year, collection_in_mil_dol) 
        VALUES (%s, %s, %s)
        """
    )
    cursor = database.cursor()
    cursor.executemany(insert_query, movie_list)
    database.commit()
    print('data inserted!')

def delete_data(database, table_name, id_table):

    delete_query = (
        f"""
        DELETE FROM {table_name} WHERE id= {id_table}
        """
    )

    cursor = database.cursor()
    cursor.execute(delete_query)
    database.commit()
    print('data deleted!')

def search_data(database, table_name, id_table):
    search_query = (
        f"""
        SELECT * FROM {table_name} WHERE id LIKE {id_table}
        """
    )
    cursor = database.cursor()
    cursor.execute(search_query)
    output = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        print(output)

def nyariinya (tabelnya):
    search = (
            f"""
            SELECT * FROM {tabelnya}
        """
        )
    cursor = database_movie.cursor()
    cursor.execute(search)
    output = cursor.fetchall()
    print(output)

def nyariin_ya2 (tabelnya):
    search = (
            f"""
            SELECT id, title FROM {tabelnya}
        """
        )
    cursor = database_movie.cursor()
    cursor.execute(search)
    output = cursor.fetchall()
    print(output)

input1 = int(input("=== APLIKASI DATABASE PYTHON === \n1. Insert Data\n2. Tampilkan Data\n3. Update Data\n4. Hapus Data\n5. Cari Data\n0. Keluar\n--------------\nPilih menu> "))
if input1 == 1:
    cek_input1 = True
    while cek_input1 == True:
        input_i1 = str(input("\nMasukan judul film yang mau di insert!\n"))
        input_i2 = int(input("Masukan tahun release filmnya sob!\n"))
        input_i3 = int(input("Masukin berapa permasukan yang didapetin filmny sob, dalam satuan juta ya!\n"))
        if __name__ == '__main__':
            insert_data(database_movie, movie_list =
            [(input_i1, input_i2,input_i3)])
        input_cek = str(input("Mau masukin data lagi ? (Y/N)"))
        if input_cek == 'Y' or input_cek =='y':
            cek_input1 = True
        else:
            cek_input1 = False

elif input1 == 2:
    input_s1 = int(input("\nTerdapat 2 tabel yaitu:\n1. Tabel Film\n2. Tabel Reviewer\nMau lihat yang mana ? (1/2)\n"))
    if input_s1 == 1:
        tabelnya = "movies"
    else:
        tabelnya = "reviewers"
    print("\nBerikut datanya:\n")
    nyariinya(tabelnya = tabelnya)

#Tombol nomer 3
elif input1 == 3:
    input_s1 = int(input("\nTerdapat 2 tabel yaitu:\n1. Tabel Film\n2. Tabel Reviewer\nMau lihat yang mana ? (1/2)\n"))
    if input_s1 == 1:
        tabelnya = "movies"  
        print("\nBerikut datanya:\n")
        nyariinya (tabelnya=tabelnya)

        #Buat updatenya disini
        input_u1 = int(input("\nMau Update data yang mana ? (Masukan 'id' dari Filmnya)\n"))
        input_u2 = int(input("Mau update apanya ? (1/2/3)\n1. Judul Film\n2. Tahun Rilis\n3. Pendapatan\n"))
        if input_u2 == 1:
            kolom = "title"
            input_u3 = str(input("\nJudulnya mau diubah kemana ?\n"))
        elif input_u2 == 2:
            kolom = "release_date"
            input_u3 = int(input("\nTahunnya mau diubah ke tahun berapa ?\n"))
        elif input_u3 == 3:
            kolom = "collection_in_mil_dol"
            input_u3 = int(input("\nLoh emang pendapatannya berapa sih ? (dalam juta dollar)\n"))
        else:
            print("\nJok ngawur sob, ulang dari awal yo hehehehe\n")
        updatean = (
            f"""
            UPDATE movies
            SET {kolom} = '{input_u3}'
            WHERE id = {input_u1}
            """
        )
        cursor = database_movie.cursor()
        cursor.execute(updatean)
        database_movie.commit()
        print("Data udah di-update sob, aman")
    else:
        nyariinya(tabelnya=tabelnya) 

#tombol no.4 - Hapus Data
elif input1 == 4:
    input_d1 = int(input("\nTerdapat 2 tabel yaitu:\n1. Tabel Film\n2. Tabel Reviewer\nMau hapus yang mana ? (1/2)\n"))
    if input_d1 == 1:
        tabelnya = "movies"  
        print("\nBerikut datanya:\n")
        nyariinya (tabelnya=tabelnya)

        #Buat deletenya lagi disini
        input_dd1 = int(input("\nMau Update data yang mana ? (Masukan 'id' dari Filmnya)\n"))
        delete_data(database_movie, tabelnya, input_dd1)
    elif input_d1 == 2:
        tabelnya = "reviewers"
        print("\nBerikut datanya:\n")
        nyariinya(tabelnya=tabelnya)
    else:
        print("Ngawur yakkkkk :(((")

#tombol no.5 
elif input1 == 5:
    input_nyari1 = int(input("\nTerdapat 2 tabel yaitu:\n1. Tabel Film\n2. Tabel Reviewer\nMau nyari yang mana ? (1/2)\n"))
    if input_nyari1 == 1:
        tabelnya = "movies"
        nyariin_ya2(tabelnya=tabelnya)
        input_nyari11 = int(input("\nMau nyari data lengkap dari judul yang mana sob ?\n(Masukin angka paling depannya)"))
        search_data(database_movie, tabelnya, input_nyari11)
    elif input_nyari1 == 2:
        tabelnya = "reviewers"
    else:
        print("Ngawur terus sobbb, yaampunnnn :((((")
elif input1 == 0:
    print("Matur Suksma Ngih!")
else:
    print("Yoweslah sob :(")
    # insert_data(database_movie, movie_list)
    # drop_table(database_movie, 'reviewers')
    # create_table(database_movie)
    # delete_data(database_movie, 'movies', 2)
    # search_data(database_movie, 'movies', 3)
