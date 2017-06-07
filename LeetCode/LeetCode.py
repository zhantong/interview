import urllib.request
import urllib.parse
import http.cookiejar
import re
import json
import configparser


class LeetCode:
    def __init__(self):
        self.base_url = 'https://leetcode.com/'
        cj = http.cookiejar.CookieJar()
        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        self.opener.addheaders = [
            ('Host', 'leetcode.com'),
            ('User-Agent',
             'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'),
            ('Referer', 'https://leetcode.com/accounts/login/')
        ]

    def login_from_config(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        return self.login(config['DEFAULT']['UserName'], config['DEFAULT']['Password'])

    def login(self, user_name, password):
        with self.opener.open(self.base_url + 'accounts/login/') as f:
            content = f.read().decode('utf-8')
        token = re.findall("name='csrfmiddlewaretoken'\svalue='(.*?)'", content)[0]
        post_data = {
            'csrfmiddlewaretoken': token,
            'login': user_name,
            'password': password
        }
        post_data = urllib.parse.urlencode(post_data)
        with self.opener.open(self.base_url + 'accounts/login/', data=post_data.encode()) as f:
            if f.read().decode().find('Successfully signed in') != -1:
                print('Successfully signed in')

    def get_problem_list(self):
        with self.opener.open(self.base_url + 'api/problems/algorithms/') as f:
            content = f.read().decode('utf-8')
        content = json.loads(content)
        result = []
        for problem in content['stat_status_pairs']:
            result.append({
                'id': problem['stat']['question_id'],
                'title': problem['stat']['question__title'],
                'slug': problem['stat']['question__title_slug'],
                'difficulty': problem['difficulty']['level'],
                'total_submitted': problem['stat']['total_submitted'],
                'total_acs': problem['stat']['total_acs'],
                'acceptance': problem['stat']['total_acs'] / problem['stat']['total_submitted'],
                'paid_only': problem['paid_only'],
                'status': True if problem['status'] else False,
            })
        result.sort(key=lambda x: x['id'])
        return result


if __name__ == '__main__':
    leetCode = LeetCode()
    leetCode.login_from_config()
    for item in leetCode.get_problem_list():
        print(item)
