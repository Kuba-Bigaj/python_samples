from smartcard.System import readers
from smartcard.util import toBytes
from smartcard.util import toHexString

SELECT = [0xA0, 0xA4, 0x00, 0x00, 0x02]
DF_TELECOM = [0x7F, 0x10]
EF_PHONEBOOK = [0x6f, 0x3b]
EF_SMS = [0x6f, 0x3c]
GET_RESPONSE = [0xa0, 0xc0, 0x00, 0x00]
GET_RECORD = [0xa0, 0xb2]
READ_BIN = [0xa0, 0xb0]

r = readers()
for i in range(0, len(r)):
    print(str(i) + " " + str(r[i]))
chosen_reader = int(input("Wpisz numer czytnika:\n"))

connection = r[chosen_reader].createConnection()
connection.connect()

while (True):
    print("Podłączono do " + str(r[chosen_reader]))
    print("Co chcesz zrobić?\n0: Nadaj wiadomość\n1: Wyświetl książkę telefoniczną\n2: Wyświetl SMS-y\n3: Wyjdź z programu")
    action = int(input())
    if action == 0:
        while True:
            message = input("Podaj wiadomość do wysłania:\n")
            if (message == "exit"):
                break
            try:
                data, sw1, sw2 = connection.transmit(toBytes(message))
                print("%x %x" % (sw1, sw2))
                print(toHexString(data))
            except:
                print("BLAD!")
    if action == 1:
        try:
            data, sw1, sw2 = connection.transmit(SELECT + DF_TELECOM)
            if sw1 != 0x9f:
                print("SELECT ERROR!")
            else:
                data, sw1, sw2 = connection.transmit(GET_RESPONSE + [sw2])
                data, sw1, sw2 = connection.transmit(SELECT + EF_PHONEBOOK)
                data, sw1, sw2 = connection.transmit(GET_RESPONSE + [sw2])
                print("%x %x" % (sw1, sw2))
                print(toHexString(data))
                record_size = data[-1]
                file_size = data[2]*256 + data[3]
                record_num = int( file_size / record_size)
                print("Rozmiar jednego rekordu: ", record_size)
                print("Rozmiar wszystkich rekordow: ", file_size)
                print("Liczba rekordow: ", record_num)
                for i in range(0, record_num):
                    read_record, sw1, sw2 = connection.transmit(GET_RECORD + [0x00, 0x02, record_size])
                    print("%x %x" % (sw1, sw2))
                    print(read_record)
        except:
            print("ERROR")
    if action == 2:
        try:
            data, sw1, sw2 = connection.transmit(SELECT + DF_TELECOM)
            if sw1 != 0x9f:
                print("SELECT ERROR!")
            else:
                data, sw1, sw2 = connection.transmit(GET_RESPONSE + [sw2])
                data, sw1, sw2 = connection.transmit(SELECT + EF_SMS)
                data, sw1, sw2 = connection.transmit(GET_RESPONSE + [sw2])
                print("%x %x" % (sw1, sw2))
                print(toHexString(data))
                record_size = data[-1]
                file_size = data[2] * 256 + data[3]
                record_num = int(file_size / record_size)
                print("Rozmiar jednego rekordu: ", record_size)
                print("Rozmiar wszystkich rekordow: ", file_size)
                print("Liczba rekordow: ", record_num)
                for i in range(0, record_num):
                    read_record, sw1, sw2 = connection.transmit(GET_RECORD + [0x00, 0x02, record_size])
                    print("%x %x" % (sw1, sw2))
                    print(read_record)
        except:
            print("ERROR")
    if action == 3:
        break

