import requests
class Scrapper:
    def getInfo (self, leetcodeSession, csrf, username):
        query = '''
        query skillStats($username: String!) {
        matchedUser(username: $username) {
            tagProblemCounts {
            advanced {
                tagName
                tagSlug
                problemsSolved
            }
            intermediate {
                tagName
                tagSlug
                problemsSolved
            }
            fundamental {
                tagName
                tagSlug
                problemsSolved
            }
            }
        }
        }
        '''
        headers = {
            'Content-Type': 'application/json',
            'Cookie': 'LEETCODE_SESSION=' + leetcodeSession + '; csrftoken=' + csrf
        }
        variables = {
            "username": username
        }
        query = (
        """
        query skillStats($username: String!) {
        matchedUser(username: $username) {
            tagProblemCounts {
            advanced {
                tagName
                tagSlug
                problemsSolved
            }
            intermediate {
                tagName
                tagSlug
                problemsSolved
            }
            fundamental {
                tagName
                tagSlug
                problemsSolved
            }
            }
        }
        }
        """
        )
        data = {
            "query": query,
            "variables": variables
        }
        
        url = "https://leetcode.com/graphql"
        response = requests.post(url, json=data, headers=headers, timeout=30)
        print(response)
        try:
            result = response.json()
        except:
            print("ERROR: failed while getting json")
        return result