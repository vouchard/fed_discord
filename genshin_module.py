import discord
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
                embed=discord.Embed(title="Solar System Genshin Helper")
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
            embed=discord.Embed(title="Solar System Genshin Helper")
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
            embed=discord.Embed(title="Solar System Genshin Helper")
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