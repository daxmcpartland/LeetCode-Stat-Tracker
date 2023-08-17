import requests
from scraper import Scraper
import matplotlib.pyplot as plt
import numpy as np

def getColor(level):
    match level:
        case 'fundamental':
            return 'green'
        case 'intermediate':
            return 'blue'
        case 'advanced':
            return 'orange'
        case _:
            return 'yellow'

def main():
    sc = Scraper()
    username = input('Username: ')
    sessionID = input('LeetCode Session: ')
    csrf = input('csrf: ')
    result = sc.getInfo(sessionID, csrf, username)

    tag_data = []
    for level in ['advanced', 'intermediate', 'fundamental']:
        for tag in result['data']['matchedUser']['tagProblemCounts'][level]:
            tag_data.append({
                'tag': tag['tagName'],
                'level': level,
                'problemsSolved': tag['problemsSolved']
            })
    print("TAG DATA: ", tag_data)

    levels = list(set(item["level"] for item in tag_data))

    for level in levels:
        fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
        
        level_data = [item for item in tag_data if item["level"] == level]
        problems_solved = [item["problemsSolved"] for item in level_data]
        tags = [item["tag"] for item in level_data]

        theta = np.linspace(0, 2 * np.pi, len(tags), endpoint=False)
        problems_solved.append(problems_solved[0])
        theta = np.append(theta, theta[0]) 

        ax.plot(theta, problems_solved, label=level.capitalize(), color=getColor(level))
        ax.fill(theta, problems_solved, alpha=0.25, facecolor=getColor(level))

        ax.set_xticks(theta[:-1])
        ax.set_xticklabels(tags)

        ax.set_title('User Skill Statistics on LeetCode')
        ax.legend()
    plt.show()
main()