import requests
import json

def main():
    find_url = "https://shazam.p.rapidapi.com/search"
    reccomendation_url = "https://shazam.p.rapidapi.com/songs/list-recommendations"
    results = 'n'
    
    print('Welcom to song finder!')
    
    while results == 'n':
        user_inp = input('find a song: ')
        file = song_find(find_url, user_inp)
        id = parse_song_finder(file)
        results = input('Is your song listed (y or n)? ')
        if results != 'n' or results != 'y':
            print('Please use proper input')
        elif results == 'n':
            print('Try searching again with more specific query')
    
    id_num = int(input('Which number correlates with desired song? '))
            
    song = song_rec(reccomendation_url, id[id_num])
    #print(song['tracks'][0]['title'])
    parse_reccomendations(song)

    



def song_find(url, search_term):
    querystring = {"term":search_term,"locale":"en-US","offset":"0","limit":"50"}

    headers = {
	    "X-RapidAPI-Key": "249c8fc227msh1756ab4a57f1babp1fcd90jsn52bc1ee8640d",
	    "X-RapidAPI-Host": "shazam.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response_text = response.text
    json_bas = json.loads(response_text)

    return json_bas

def parse_song_finder(json_txt):
    song_list = json_txt['tracks']['hits']
    id = []
    
    for i in range(len(song_list)):
        print('%s. %s by %s'% (i, song_list[i]['track']['title'], song_list[i]['track']['subtitle']))
        id.append(song_list[i]['track']['key'])
        
    return id
    
    
def song_rec(url, song_key):
    querystring = {"key": song_key,"locale":"en-US"}

    headers = {
        "X-RapidAPI-Key": "249c8fc227msh1756ab4a57f1babp1fcd90jsn52bc1ee8640d",
        "X-RapidAPI-Host": "shazam.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response_text = response.text
    json_bas = json.loads(response_text)
    
    return json_bas

def parse_reccomendations(txt):
    print('\n----------Song reccomendations loading----------\n')
    songs = txt['tracks']
    for i in range(len(songs)):
        print('%s by %s' % (songs[i]['title'], songs[i]['subtitle']))
    
if __name__ == '__main__':
    main()
    

