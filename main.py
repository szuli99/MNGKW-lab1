import re
import csv

# REGEXY
no_regex="(?<=iss\.\s)\d*|(?<=no\.\s)\d*|(?<=No\.\s)\d*|(?<=[^(]nr\s)\d+|(?<=num\.\s)\d*|(?<=issue\s)\d*|(?<=Issue\s)\d*|(?<=Issue:\s)\d*|(?<=Nr\s)\d*"
vol_regex="(?<=vol\.\s)\d*|(?<=\st\.\s)\d*|(?<=Vol\.\s)\d*|(?<=\sT\.\s)\d*[^,K]"
article_no_regex="(?<=nr\sart\.\s)(\w\d*)"
pages_in_range_regex="(?<=\ss\.\s)(?:\d+-\d+)|(?<=S\.\s)(?:\d+-\d+)"
publisher_name_regex="(?<=\:\s)(?:[R][^y]|[A-PS-Z]\.*\w*\.*)(?:\s|\,)*[^0-9\;\,]*"
publisher_location_regex="(?:[A-ZŁ][a-uu-ząężźńśćłó]+)(?:-|\,\s|\s\;\s)*(?:[A-ZŁa-ząężźńśćŁłó]+[^u.]\s)*(?=\s\:)"
publisher_year_regex="(?<=\,\s)(?:\d\d\d\d)"

class segregation():

    def flat_list(self,source_list):    #METODA KONWERTUJACA LISTE DWUWYMIAROWA NA JEDNOWYMAIROWA
        flat_list = []
        for element in source_list:
            if type(element) is list:
                for item in element:
                    flat_list.append(item)
            else:
                flat_list.append(element)
        return flat_list

    def reg(self,data,regex):   #METODA WYSZUKUJACA WARTOSCI NA PODSTAWIE REGEXU
        if re.findall(regex, data):
            result = re.findall(regex, data)    #JEZELI REGEX COS ZNAJDZIE TO ZWRACA TA WARTOSC W PRZECIWNYM WYPADKU ZWRACA PUSTA KOMORKE
            return(result[0])
        else:
            return('')

def main():

    header=['no', 'vol', 'article no', 'pages in range', 'publisher name', 'publisher location', 'publisher year']
    with open('result_file.csv', 'w', newline='') as result_file:    #UTWORZENIE PLIKU WYNIKOWEGO I NAGLOWKOW
        writer = csv.writer(result_file)
        writer.writerow(header)

    file= segregation()
    row_list=[] #LISTA PRZECHOWUJACA WIERSZ Z WYNIKAMI
    with open('details.csv', 'r', encoding='utf-8') as source_file: #OTWARCIE PLIKU WEJSCIOWEGO
        reader = csv.reader(source_file, delimiter=",")
        for line in reader: #PETLA POBIERAJACA WIERSZ Z PLIKU WEJSCIOWEGO
            data=line[0]+line[1]    #ZAPIS WARTOSCI Z DWOCH PIERWSZYCH KOLUMN DO ZMIENNEJ DATA
            row_list.append(file.reg(data, no_regex))   #PRZEKAZNIE DANYCH ZE ZMIENNEJ DATA ORAZ REGEXA DO FUNKCJI
            row_list.append(file.reg(data, vol_regex))
            row_list.append(file.reg(data, article_no_regex))
            row_list.append(file.reg(data, pages_in_range_regex))
            row_list.append(file.reg(data, publisher_name_regex))
            row_list.append(file.reg(data, publisher_location_regex))
            row_list.append(file.reg(data, publisher_year_regex))
            
            #print(file.flat_list(row_list))
            with open('result_file.csv', 'a', newline='') as result_file:    #OTWARCIE PLIKU WYNIKOWEGO
                writer = csv.writer(result_file)
                writer.writerow(file.flat_list(row_list)) #ZAPIS WIERSZA DO PLIKU WYNIKOWEGO

            row_list.clear() #CZYSZCZENIE LISTY PRZECHOWUJACEJ WIERSZ Z WYNIKAMI

main()