import os

from barcode import EAN13
from barcode import errors
from barcode.writer import SVGWriter


def check_name(country_number):
    if 1 <= country_number <= 19:
        return "USA"
    elif 20 <= country_number <= 29:
        return "Ograniczona dystrybucja"
    elif 30 <= country_number <= 39:
        return "USA (leki)"
    elif 40 <= country_number <= 49:
        return "Ograniczona dystrybucja"
    elif 55 <= country_number <= 59:
        return "USA (zarezerwowane)"
    elif 60 <= country_number <= 139:
        return "USA"
    elif 200 <= country_number <= 299:
        return "Ograniczona dystrybucja"
    elif 300 <= country_number <= 379:
        return "Francja"
    elif 380 == country_number:
        return "Bułgaria"
    elif 383 == country_number:
        return "Słowenia"
    elif 385 == country_number:
        return "Chorwacja"
    elif 387 == country_number:
        return "Bośnia i Hercegowina"
    elif 389 == country_number:
        return "Czarnogóra"
    elif 400 <= country_number <= 440:
        return "Niemcy"
    elif 450 <= country_number <= 459 or 490 <= country_number <= 499:
        return "Japonia"
    elif 460 <= country_number <= 469:
        return "Rosja"
    elif 470 == country_number:
        return "Kirgistan"
    elif 471 == country_number:
        return "Tajwan"
    elif 474 == country_number:
        return "Estonia"
    elif 475 == country_number:
        return "Łotwa"
    elif 476 == country_number:
        return "Azerbejdżan"
    elif 477 == country_number:
        return "Litwa"
    elif 478 == country_number:
        return "Uzbekistan"
    elif 479 == country_number:
        return "Sri Lanka"
    elif 480 == country_number:
        return "Filipiny"
    elif 481 == country_number:
        return "Białoruś"
    elif 482 == country_number:
        return "Ukraina"
    elif 483 == country_number:
        return "Turkmenistan"
    elif 484 == country_number:
        return "Mołdawia"
    elif 485 == country_number:
        return "Armenia"
    elif 486 == country_number:
        return "Gruzja"
    elif 487 == country_number:
        return "Kazahstan"
    elif 488 == country_number:
        return "Tadżykistan"
    elif 489 == country_number:
        return "Chiny / Hong Kong"
    elif 500 <= country_number <= 509:
        return "Wielka Brytania"
    elif 520 <= country_number <= 521:
        return "Grecja"
    elif 528 == country_number:
        return "Lebanon"
    elif 529 == country_number:
        return "Cypr"
    elif 530 == country_number:
        return "Albania"
    elif 531 == country_number:
        return "Macedonia"
    elif 535 == country_number:
        return "Malta"
    elif 539 == country_number:
        return "Irlandia"
    elif 540 <= country_number <= 549:
        return "Belgia i Luxemburg"
    elif 560 == country_number:
        return "Portugalia"
    elif 569 == country_number:
        return "Islandia"
    elif 570 <= country_number <= 579:
        return "Dania"
    elif 590 == country_number:
        return "Polska"
    elif 594 == country_number:
        return "Rumunia"
    elif 599 == country_number:
        return "Węgry"
    elif 600 <= country_number <= 601:
        return "RPA"
    elif 603 == country_number:
        return "Ghana"
    elif 604 == country_number:
        return "Senegal"
    elif 605 <= country_number <= 606 or 610 == country_number or 614 == country_number or 623 == country_number or 758 == country_number or 894 == country_number:
        return "Ograniczona dystrybucja"
    elif 607 == country_number:
        return "Oman"
    elif 608 == country_number:
        return "Bahrajn"
    elif 609 == country_number:
        return "Mauritius"
    elif 611 == country_number:
        return "Maroko"
    elif 613 == country_number:
        return "Algieria"
    elif 615 == country_number:
        return "Nigeria"
    elif 616 == country_number:
        return "Kenia"
    elif 617 == country_number:
        return "Kameron"
    elif 618 == country_number:
        return "Wybrzeże Kości Słoniowej"
    elif 619 == country_number:
        return "Tunezja"
    elif 620 == country_number:
        return "Tanzania"
    elif 621 == country_number:
        return "Syria"
    elif 622 == country_number:
        return "Egipt"
    elif 624 == country_number:
        return "Libia"
    elif 625 == country_number:
        return "Jordania"
    elif 626 == country_number:
        return "Iran"
    elif 627 == country_number:
        return "Kuwejt"
    elif 628 == country_number:
        return "Arabia Saudyjska"
    elif 629 == country_number:
        return "ZEA"
    elif 630 == country_number:
        return "Katar"
    elif 631 == country_number:
        return "Namibia"
    elif 640 <= country_number <= 649:
        return "Finlandia"
    elif 680 <= country_number <= 681 or 690 <= country_number <= 699:
        return "Chiny"
    elif 700 <= country_number <= 709:
        return "Norwegia"
    elif 729 == country_number:
        return "Izrael"
    elif 730 <= country_number <= 739:
        return "Szwecja"
    elif 740 == country_number:
        return "Gwatemala"
    elif 741 == country_number:
        return "Salwador"
    elif 742 == country_number:
        return "Honduras"
    elif 743 == country_number:
        return "Nikaragua"
    elif 744 == country_number:
        return "Kostaryka"
    elif 745 == country_number:
        return "Panama"
    elif 746 == country_number:
        return "Dominikana"
    elif 750 == country_number:
        return "Meksyk"
    elif 754 <= country_number <= 755:
        return "Kanada"
    elif 759 == country_number:
        return "Wenezuela"
    elif 760 <= country_number <= 769:
        return "Szwajcaria"
    elif 770 <= country_number <= 771:
        return "Kolumbia"
    elif 773 == country_number:
        return "Urugwaj"
    elif 775 == country_number:
        return "Peru"
    elif 777 == country_number:
        return "Boliwia"
    elif 778 <= country_number <= 779:
        return "Argentyna"
    elif 780 == country_number:
        return "Czile"
    elif 784 == country_number:
        return "Paragwaj"
    elif 786 == country_number:
        return "Ekwador"
    elif 789 <= country_number <= 790:
        return "Brazylia"
    elif 800 <= country_number <= 839:
        return "Włochy"
    elif 840 <= country_number <= 849:
        return "Hiszpania"
    elif 850 == country_number:
        return "Kuba"
    elif 858 == country_number:
        return "Słowacja"
    elif 859 == country_number:
        return "Czechy"
    elif 860 == country_number:
        return "Serbia"
    elif 865 == country_number:
        return "Mongolia"
    elif 867 == country_number:
        return "Korea Północna"
    elif 868 <= country_number <= 869:
        return "Turcja"
    elif 870 <= country_number <= 879:
        return "Holandia"
    elif 880 <= country_number <= 881:
        return "Korea Południowa"
    elif 883 == country_number:
        return "Birma"
    elif 884 == country_number:
        return "Kambodża"
    elif 885 == country_number:
        return "Tajlandia"
    elif 888 == country_number:
        return "Singapur"
    elif 890 == country_number:
        return "Indie"
    elif 893 == country_number:
        return "Wietnam"
    elif 896 == country_number:
        return "Pakistan"
    elif 899 == country_number:
        return "Indonezja"
    elif 900 <= country_number <= 919:
        return "Austria"
    elif 930 <= country_number <= 939:
        return "Australia"
    elif 940 <= country_number <= 949:
        return "Nowa Zelandia"
    elif 950 == country_number:
        return "Specjalne"
    elif 951 == country_number:
        return "Specjalne"
    elif 952 == country_number:
        return "Używany w celach demonstracyjnych"
    elif 955 == country_number:
        return "Malezja"
    elif 958 == country_number:
        return "Makau, Chiny"
    elif 960 <= country_number <= 969:
        return "Specjalne"
    elif 978 <= country_number <= 979:
        return "Numer ISBN"
    elif 981 <= country_number <= 983:
        return "Kupon"
    elif 977 == country_number:
        return "Numer ISSN"
    elif 980 == country_number:
        return "Refundowane recepty"
    elif 999 == country_number:
        return "Kupon"
    return "Kod zarezerwowany na przyszły uzytek"


while True:
    print("Wpisz 'read' aby przeanalizować kod ze skanera / wpisany ręcznie")
    print("Wpisz 'write' aby wygenerować nowy kod kreskowy do pliku .svg")
    print("Wpisz 'exit' aby wyjść z programu")

    choice = input()

    if choice == "write":
        filename = input("Wprowadź nazwę pliku (bez rozszerzenia):")
        code = input("Wprowadź kod do zakodowania:")
        with open(filename+".svg", "wb") as f:
            try:
                EAN13(str(code), writer=SVGWriter()).write(f)
                print("Kod kreskowy stworzony!")
            except errors.IllegalCharacterError:
                print("Zły format kodu! Kod składa się tylko z cyfr!")
            except errors.NumberOfDigitsError:
                print("Zły format kodu! Niepoprawna liczba cyfr!")
            os.system('pause')

    elif choice == "read":
        scanned_barcode = input("Zeskanuj kod / Wpisz go ręcznie:")
        try:
            control_digit = int(scanned_barcode[12:13])
            control_sum = 0
            for i in range(0, 12):
                cur_num = int(scanned_barcode[i:(i + 1)])
                if i % 2 == 1:
                    cur_num *= 3
                control_sum += cur_num
            control_sum *= -1
            control_sum %= 10
            if control_sum == control_digit:
                print("Suma kontrolna się zgadza!")
            else:
                print("Suma kontrolna się nie zgadza!")
            country_num = int(scanned_barcode[0:3])
            print("Kraj kodu: " + check_name(country_num))
        except:
            print("Błędny kod!")
        os.system('pause')
    elif choice == "exit":
        exit(0)
    os.system('cls')
