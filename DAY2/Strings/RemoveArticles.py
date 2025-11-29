article=['an','a','the']
sentence=input("Enter the sentence to remove articles: ")

result=sentence

for i in  article:
    result=result.replace(i,'')
    result=result.replace(i.capitalize(),'')

result=' '.join(result.split())

print(result)
