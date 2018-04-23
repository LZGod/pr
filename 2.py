import os
import re

def sp(filename, path):
    with open(C:\Users\student\Desktop\all-seasons.csv) as csv:
        lines = csv.readlines()
        for line in lines[1:]:
            if re.match('\d+,\d+', line):
                cells = line.split(',')
                if len(cells) == 4:
                    season, episode, character, speech = cells
                    season_path = os.path.join(path, season)
                    if season in os.listdir(path):
                        if episode in os.listdir(season_path):
                            ff = os.path.join(epi_path, character + '.txt')
                            if character+'.txt' in os.listdir(epi_path):
                                with open(ff, 'a') as f:
                                    f.write(speech)
                            else:
                                with open(ff, 'w') as f:
                                    f.write(speech)
                        else:
                            epi_path = os.path.join(season_path, episode)
                            os.mkdir(epi_path)
                    else:
                        os.mkdir(season_path)
                
    
    
    
