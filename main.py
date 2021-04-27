import requests
import json
import argparse
from fcache.cache import FileCache
from datetime import datetime


class starwars_character:
   
    def __init__(self, search=None, world=False):
        if search != None:
            self.search = search
            self.world = world
            self.caching()
        
    def do_the_request(self):
        people_api = "https://www.swapi.tech/api/people/?name="
        request = requests.get(people_api+self.search).text
        request = json.loads(request)
        self.data = request['result']
        self.get_the_data()
    
    def get_the_data(self):
        if self.data:
            self.pass_world_to_cache()
            self.initialize_cache()
            self.prints()
            if self.world:
                self.homeworld()

        else:
            print("The force is not strong within you")
        
        self.stars_cache.close()

    def prints(self):
        print('Name: ',     self.stars_cache[self.search][0])
        print('Height: ',   self.stars_cache[self.search][1])
        print('Mass: ',     self.stars_cache[self.search][2])
        print('Birthday: ', self.stars_cache[self.search][3])

    def homeworld(self):
        w_name = self.stars_cache[self.search][5]
        earth_year = self.stars_cache[self.search][6]
        earth_day  = self.stars_cache[self.search][7]
        
        print(f"On {w_name} 1 year on earth is {earth_year} and 1 day {earth_day} days.")
    

    def caching(self):
        self.stars_cache = FileCache('SWars.txt', flag='cs')

        if self.search in self.stars_cache:
            self.prints()
            if self.world:
                self.homeworld()
            print(f"Cached: {self.stars_cache[self.search][8]}")
        else:
            
            self.do_the_request()
    
    def initialize_cache(self):
        self.stars_cache[self.search] = []
        self.stars_cache[self.search] = [
            self.data[0]['properties']['name'],
            self.data[0]['properties']['height'],
            self.data[0]['properties']['mass'],
            self.data[0]['properties']['birth_year'],
            self.data[0]['properties']['homeworld'],
            self.home_name,
            self.orbital_period,
            self.rotation_period,
            datetime.now()
        ]
    
    def pass_world_to_cache(self):
        home_req = requests.get(self.data[0]['properties']['homeworld']).text
        home_req = json.loads(home_req)
        self.home_name = home_req['result']['properties']['name']
        self.orbital_period = float(home_req['result']['properties']['orbital_period'])/365
        self.rotation_period = float(home_req['result']['properties']['rotation_period'])/24
    
    def clear_cache(self):
        self.stars_cache = FileCache('SWars.txt', flag='cs')
        self.stars_cache.clear()
        print("Removed cache.")
        self.stars_cache.close()

if __name__ == "__main__":

    # initialize the parser
    parser = argparse.ArgumentParser()

    # Add the parameters
    parser.add_argument('-s', '--search',  help="Your search query.", type=str)
    parser.add_argument('-w', '--world', 
                        help="Convert the characters` Homeworld year to Earth year", 
                        action='store_true')
    parser.add_argument('-c', '--clear_cache', 
                        help="Cleans the search cache. Dont use it with other arguments.",
                        action='store_true')

    # Parse the arguments
    args = parser.parse_args()
    
    if args.clear_cache:
        clean_the_cache = starwars_character()
        clean_the_cache.clear_cache()
    else:
        person = starwars_character(args.search, args.world)
