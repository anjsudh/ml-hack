import mechanicalsoup


def get_diseases_data():
    br = mechanicalsoup.StatefulBrowser()
    rangeLetters = map(chr, range(ord('c'), ord('f') + 1))
    disease_to_symptoms = {}
    file_write = open("workfile.txt", "a+")
    for letter in rangeLetters:
        htm = "https://www.medicinenet.com/symptoms_and_signs/alpha_" + letter + ".htm"
        print htm
        r = br.open(htm)
        diseases = r.soup.find_all(class_="AZ_results")
        a_symptoms = diseases[0].find_all('ul')[0].find_all('li')

        for a_symptom in a_symptoms:
            symptom_link = a_symptom.find_all('a')[0]
            symptom_name_link = symptom_link['href']
            symptom_name = symptom_name_link.split('/')[1]
            print symptom_name
            s = br.open('https://www.medicinenet.com' + symptom_name_link)
            divs = s.soup.find_all(class_='apPage article-extra')
            for div in divs:
                a = div.find('ul').find('a')
                if a is not None and a.has_attr('name'):
                    links = div.find_all('a')
                    for link in links:
                        if link.has_attr('href'):
                            replaced_string = link['href'].replace("https://www.medicinenet.com/", "")
                            data = replaced_string.split('/')
                            if data[0] not in disease_to_symptoms:
                                disease_to_symptoms[data[0]] = [symptom_name]
                            else:
                                existing_symptoms = disease_to_symptoms[data[0]]
                                existing_symptoms.append(symptom_name)
        for item in disease_to_symptoms.items():
            file_write.write(item[0])
            file_write.write('|')
            file_write.write(",".join(item[1]))
            file_write.write('\n')


get_diseases_data()
