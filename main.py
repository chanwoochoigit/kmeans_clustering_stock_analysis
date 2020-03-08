import excelify

def main():
    text = open("/home/chanwoo/PycharmProjects/crawler/data.txt", 'r')
    excelify.json_to_csv(text)



if __name__ == '__main__':
    main()