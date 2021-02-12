import requests
import json

if __name__ == '__main__':

	url= "https://i.imgur.com/bxzjHV5.jpeg"
	response = requests.get(url , stream=True)

	with open("imagen_proactica.jpg", 'wb') as file:
		
		for document in response.iter_content():
			file.write(document)


	response.close()






