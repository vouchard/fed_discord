import discord
import json
import requests
class genshin:
    def __init__(self,keyword):
        self.keyword = keyword
        self.api_url = 'https://api.genshin.dev/'
        self.response = requests.get(self.api_url).json()['types']
    def get_info(self):
        api_url = self.api_url
        responses = self.response
        for response in responses:
            url_to_check = api_url + response + '/' + self.keyword
            req = requests.get(url_to_check)
            check = (req).status_code
            print('checking',url_to_check)
            if check == 200:
                print(url_to_check)
                embed=discord.Embed(title="'' Genshin Helper")
                portrait = requests.get(url=url_to_check + '/portrait').status_code
                icon = requests.get(url=url_to_check + '/icon').status_code
                img_url = None
                
                #deciding for image
                if portrait == 200:
                    img_url = url_to_check + '/portrait'
                elif icon == 200:
                    img_url = url_to_check + '/icon'
                
                #artifcat images are all flower of life
                if response == 'artifacts':
                    img_url = url_to_check + '/flower-of-life'


                embed.set_image(url=img_url)
                request_json = req.json()
                for key in request_json:
                    if type(request_json[key]).__name__ == 'str':
                        embed.add_field(name=key.upper(), value=request_json[key], inline=True)


                if img_url != None:
                    embed.add_field(name='IMAGE_LINK', value=img_url, inline=False)
                if response == 'weapons':
                    embed =  self.get_weapon_info(embed)
                return embed
                break
                
            elif response == 'consumables':
                embed = self.get_consumable_info()
                if embed != None:
                    return embed
                    break

    def get_consumable_info(self):
        url_to_check = self.api_url + 'consumables' + '/food'
        req = requests.get(url_to_check)
        request_json = req.json()
        if self.keyword in request_json.keys():
            embed=discord.Embed(title="'' Genshin Helper")
            recipes = ''
            for item in request_json[self.keyword]:
                if type(request_json[self.keyword][item]).__name__ == 'str':
                    embed.add_field(name=item.upper(), value=request_json[self.keyword][item], inline=True)
                if item == 'recipe':
                    # print(request_json[self.keyword]['recipe'])
                    for recip in request_json[self.keyword]['recipe']:
                        recipes = recipes + recip['item'] + '-' + str(recip['quantity']) + '\n'
                    embed.add_field(name='Recipe', value=recipes, inline=False)
            return embed
            
        url_to_check = self.api_url  + 'consumables/potions'
        req = requests.get(url_to_check)
        request_json = req.json()
        
        if self.keyword in request_json.keys():
            embed=discord.Embed(title="'' Genshin Helper")
            recipes = ''
            for item in request_json[self.keyword]:
                if type(request_json[self.keyword][item]).__name__ == 'str':
                    embed.add_field(name=item.upper(), value=request_json[self.keyword][item], inline=True)
                if item == 'crafting':
                    # print(request_json[self.keyword]['recipe'])
                    for recip in request_json[self.keyword]['crafting']:
                        recipes = recipes + recip['item'] + '-' + str(recip['quantity']) + '\n'
                    embed.add_field(name='Crafting', value=recipes, inline=False)
                    embed.set_image(url=self.api_url  + 'consumables/potions/' + self.keyword)
            return embed
    
    def get_weapon_info(self,current_embed):
        url = 'https://api.genshin.dev/materials/weapon-ascension'
        req_json = requests.get(url).json()
        for key in req_json:
            mats = ''
            if self.keyword in req_json[key]['weapons']:
                for item in req_json[key]['items']:
                    mats = mats + item['name'] + '\n'
                    
                mats = mats + 'Availability:' + (','.join(req_json[key]['availability'])) + '\n'
                mats = mats + 'Location:' + req_json[key]['source']
                current_embed.add_field(name='Weapon Ascension Material', value=mats, inline=False)
        url = 'https://api.genshin.dev/materials/common-ascension'
        req_json = requests.get(url).json()
        for key in req_json:
            mats = ''
            if 'weapons' in req_json[key].keys():
                if self.keyword in req_json[key]['weapons']:
                    mats = mats + key + '\n' + 'sources:' + (','.join(req_json[key]['sources']))
                    current_embed.add_field(name='Common Ascension Material', value=mats, inline=False)
        return current_embed
    
    def gi_help(self,kw=None):
        to_send = ''
        if kw == None:
            to_send = 'All characters/artifacts/enemies/foods/potions/weapons are searcheable \n \
                For words with spaces use dash(-) instead \n \
                exampleA: fd.gi diluc   \n \
                exampleB: fd.gi tenacity-of-the-millelith \n \
                exampleC: the-viridescent-hunt \n \n \
                For list of searcheables use the following commands \n \
                fd.help charac \n \
                fd.help weapons \n \
                fd.help foods \n \
                fd.help potions \n \
                fd.help artifacts \n \
                fd.help enemies \n \n \
                --CHARACTER VOICE LINES \n \n \
                fd.gichar  list of genshin characters with voicelines(maybe) \n \n \
                fd.gicommands *characterName* \n \n \
                fd.givoice *command* \n \n '
        elif kw == 'charac':
            resp = requests.get('https://api.genshin.dev/characters').json()
            to_send = 'Characters' + '\n'    
            to_send = to_send + (','.join(resp)) + '\n'
        elif kw == 'weapons':
            resp = requests.get('https://api.genshin.dev/weapons').json()
            to_send = to_send +  'Weapons' + '\n'
            to_send = to_send + (','.join(resp)) + '\n'

        elif kw == 'enemies':
            resp = requests.get('https://api.genshin.dev/enemies').json()

            to_send = to_send +  'Enemies' + '\n'
            to_send = to_send + (','.join(resp)) + '\n' + '\n'
        
        elif kw == 'artifacts':
            resp = requests.get('https://api.genshin.dev/artifacts').json()

            to_send = to_send +  'Artifacts' + '\n'
            to_send = to_send + (','.join(resp)) + '\n' + '\n'

        elif kw == 'foods':
            resp = requests.get('https://api.genshin.dev/consumables/food').json()
            
            to_send = to_send +  'Food' + '\n'
            to_send = to_send + (','.join(list(resp.keys()))) + '\n'+ '\n'
        elif kw == 'potions':
            resp = requests.get('https://api.genshin.dev/consumables/potions').json()
        
            to_send = to_send +  'Potions' + '\n'
            to_send = to_send + (','.join(list(resp.keys()))) + '\n'+ '\n'
        else: to_send = ''
        return to_send

class genshin_voicelines:
    def __init__(self):
        fl = open('genshin_voice_lines.json','r')
        self.data = json.load(fl)
        fl.close()
    def char_list(self):
        to_r = []
        for dt in self.data:
            to_r.append(dt['Character'])
        return ','.join(to_r)
    def voice_list(self,character):
        char = None
        for dt in self.data:
            #print(dt['Character'].upper())
            if (dt['Character']).upper() == character.upper():
                char = dt
        if char == None:
            return 'Invalid Genshin Character'
        else:
            vl = char['VoiceLines']
            counter = 0
            ls = ['Voice >> Command']
            for voice in vl:
                for keys in voice.keys():       
                    data = keys + ' >> ' + character + '-' + str(counter)
                    ls.append(data)
                    counter+=1
            return ('\n').join(ls)
        

    def voice_get_url(self,command):
        charac = command.split('-')[0]
        command = int(command.split('-')[1])
        char = None
        for dt in self.data:
            #print(dt['Character'].upper())
            if (dt['Character']).upper() == charac.upper():
                char = dt
        if char == None:
            return 'Invalid Genshin Character'
        else:
            vl = char['VoiceLines']
            counter = 0
            ls = ['Voice >> Command']
            url = None
            for voice in vl:
                for keys in voice.keys():       
                    if counter == command:
                        url = voice[keys]
                    counter +=1
            return (url)
    






