import requests
import json

class Orca:
    def gen_single(s:str)->str:
        prompt = """Follow the given format below, you are a question generating AI, don't add any other words, make questions only from the INFORMATION section:
        Follow this Format
        FORMAT:
        ```
        Single Answer Questions:
        Q1 {question number}. {the questions based on INFORMATION only!}
        Q2 {question number}. {the questions based on INFORMATION only!}
        Q3 {question number}. {the questions based on INFORMATION only!}
        Q4 {question number}. {the questions based on INFORMATION only!}
        Q5 {question number}. {the questions based on INFORMATION only!}
        ```
        the questions must be single line
        answers must be single line

        now use the following piece of information to generate questions:
        """ + f"""INFORMATION:
        ```
        {s}
        ```
        INSTRUCTIONS to you:
        Questions should be based on the information under INFORMATION only
        Follow the format
        """
        resp = requests.post(url='http://127.0.0.1:11434/api/generate',data=json.dumps({
    "model": "orca-mini",
    "prompt":prompt
   }))  
        # print(resp.text)
        # l = resp.text.split()
        l = (resp.text.split('\n'))[:-1]
        j = ''
        for i in l:
            k = json.loads(i)
            j+=k['response']
        print(j)
        return j[1:]