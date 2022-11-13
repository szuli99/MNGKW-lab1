import unittest
import csv
from main import segregation



class tests(unittest.TestCase):
    counter_all = 0 #ZMIENNA PRZECHOWUJACA ILOSC WSZYSTKICH MATCHY
    def test_1_flat_list(self): #TEST FUNKCJI KONWERTUJACEJ TABLICE DWUWYMIAROWA NA JEDNOWYMIAROWA
        #given
        test_list=[[1],[2]]
        expected_list=[1,2]
        #then
        test_object=segregation()
        result_list=test_object.flat_list(test_list)
        #expect
        self.assertEqual(expected_list,result_list,msg='Converting two-dimensional list to one-dimensional failed')

    def test_2_reg_no(self): #TEST FUNKCJI Z REGEXEM DLA KOLUMNY NO
        counter=0 #ZMIENNA PRZECHOWUJACA ILOSC ZGODNYCH KOMOREK (KOLUMNA NO)
        regex = "(?<=iss\.\s)\d*|(?<=no\.\s)\d*|(?<=No\.\s)\d*|(?<=[^(]nr\s)\d+|(?<=num\.\s)\d*|(?<=issue\s)\d*|(?<=Issue\s)\d*|(?<=Issue:\s)\d*|(?<=Nr\s)\d*"
        with open('details.csv', 'r', encoding='utf-8') as source_file: #OTWARCIE PLIKU
            reader = csv.reader(source_file, delimiter=",")
            for line in reader: #WCZYTYWANIE PO WIERSZU DANYCH Z PLIKU WEJSCIOWEGO
                data = line[0]+line[1]
                test_object=segregation()
                result=test_object.reg(data,regex)
                if(result==line[2]):    #WARUNEK POROWNUJACY WARTOSC ZWROCONA PRZEZ FUNKCJE Z WARTOSCIA KOLUMNY NO Z PLIKU
                    counter+=1
        tests.counter_all+=counter
        print('-'*100)
        expected_results=700 #LICZBA OCZEKIWANYCH MATCHY
        self.assertEqual(expected_results,counter,msg=print('Column no: ',round(counter/700*100,2),'% correct matches'))

        #KOLEJNE TESTY DZIALAJA NA TEJ SAMEJ ZASADZIE, ROZNIA SIE JEDYNIE REGEXEM ORAZ KOLUMNA Z KTORA SA POROWNYWANE WYNIKI

    def test_3_reg_vol(self): #TEST FUNKCJI Z REGEXEM DLA KOLUMNY VOL
        counter=0
        regex = "(?<=vol\.\s)\d*|(?<=\st\.\s)\d*|(?<=Vol\.\s)\d*|(?<=\sT\.\s)\d*[^,K]"
        with open('details.csv', 'r', encoding='utf-8') as source_file:
            reader = csv.reader(source_file, delimiter=",")
            for line in reader:
                data = line[0]+line[1]
                test_object=segregation()
                result=test_object.reg(data,regex)
                if(result==line[3]):
                    counter+=1
        tests.counter_all+=counter
        print('-'*100)
        expected_results = 700
        self.assertEqual(expected_results,counter,msg=print('Column vol: ',round(counter/700*100,2),'% correct matches'))

    def test_4_reg_article_no(self): #TEST FUNKCJI Z REGEXEM DLA KOLUMNY ARTICLE NO
        counter=0
        regex = "(?<=nr\sart\.\s)(\w\d*)"
        with open('details.csv', 'r', encoding='utf-8') as source_file:
            reader = csv.reader(source_file, delimiter=",")
            for line in reader:
                data = line[0]+line[1]
                test_object=segregation()
                result=test_object.reg(data,regex)
                if(result==line[4]):
                    counter+=1
        tests.counter_all+=counter
        print('-'*100)
        expected_results = 700
        self.assertEqual(expected_results,counter,msg=print('Column article_no: ',round(counter/700*100,2),'% correct matches'))

    def test_5_reg_pages_in_range(self): #TEST FUNKCJI Z REGEXEM DLA KOLUMNY PAGES IN RANGE
        counter=0
        regex = "(?<=\ss\.\s)(?:\d+-\d+)|(?<=S\.\s)(?:\d+-\d+)"
        with open('details.csv', 'r', encoding='utf-8') as source_file:
            reader = csv.reader(source_file, delimiter=",")
            for line in reader:
                data = line[0]+line[1]
                test_object=segregation()
                result=test_object.reg(data,regex)
                if(result==line[5]):
                    counter+=1
        tests.counter_all+=counter
        print('-' * 100)
        expected_results = 700
        self.assertEqual(expected_results,counter,msg=print('Column pages_in_range: ',round(counter/700*100,2),'% correct matches'))

    def test_6_reg_publisher_name(self): #TEST FUNKCJI Z REGEXEM DLA KOLUMNY PUBLISHER NAME
        counter=0
        regex = "(?<=\:\s)(?:[R][^y]|[A-PS-Z]\.*\w*\.*)(?:\s|\,)*[^0-9\;\,]*"
        with open('details.csv', 'r', encoding='utf-8') as source_file:
            reader = csv.reader(source_file, delimiter=",")
            for line in reader:
                data = line[0]+line[1]
                test_object=segregation()
                result=test_object.reg(data,regex)
                if(result==line[7]):
                    counter+=1
        tests.counter_all+=counter
        print('-'*100)
        expected_results = 700
        self.assertEqual(expected_results,counter,msg=print('Column publisher_name: ',round(counter/700*100,2),'% correct matches'))

    def test_7_reg_publisher_location(self): #TEST FUNKCJI Z REGEXEM DLA KOLUMNY PUBLISHER LOCATION
        counter=0
        regex = "(?:[A-ZŁ][a-uu-ząężźńśćłó]+)(?:-|\,\s|\s\;\s)*(?:[A-ZŁa-ząężźńśćŁłó]+[^u.]\s)*(?=\s\:)"
        with open('details.csv', 'r', encoding='utf-8') as source_file:
            reader = csv.reader(source_file, delimiter=",")
            for line in reader:
                data = line[0]+line[1]
                test_object=segregation()
                result=test_object.reg(data,regex)
                if(result==line[8]):
                    counter+=1
        tests.counter_all+=counter
        print('-'*100)
        expected_results = 700
        self.assertEqual(expected_results,counter,msg=print('Column publisher_location: ',round(counter/700*100,2),'% correct matches'))

    def test_8_reg_publisher_year(self): #TEST FUNKCJI Z REGEXEM DLA KOLUMNY PUBLISHER YEAR
        counter=0
        regex = "(?<=\,\s)(?:\d\d\d\d)"
        with open('details.csv', 'r', encoding='utf-8') as source_file:
            reader = csv.reader(source_file, delimiter=",")
            for line in reader:
                data = line[0]+line[1]
                test_object=segregation()
                result=test_object.reg(data,regex)
                if(result==line[9]):
                    counter+=1
        tests.counter_all+=counter
        print('-'*100)
        expected_results = 700
        self.assertEqual(expected_results,counter,msg=print('Column publisher_year: ',round(counter/700*100,2),'% correct matches'))

    def test_9_print_result(self):
        print('-'*50)
        print('Total: ',round(tests.counter_all/4900*100,2),'% coorect matches')

if __name__ == '__main__':
    unittest.main()