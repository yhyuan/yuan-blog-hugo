# export NODE_OPTIONS="--max-old-space-size=8192"
# SET NODE_OPTIONS=--max-old-space-size=8192
# pip install awscli
# aws configure

import os, json
dir_path = r'content/posts/leetcode'
# json_path = r'src/components/LeetCode/data.json';
res = []
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)
res = list(filter(lambda filename: filename[-3:] == ".md", res))

'''
f = open(json_path)
  
# returns JSON object as 
# a dictionary
data = json.load(f)
stat_status_pairs = data["stat_status_pairs"]
data_dict = {}
for i in range(len(stat_status_pairs)):
    item = stat_status_pairs[i]
    id = item["stat"]["question_id"]
    data_dict[id] = item
'''
#print(data_dict)
def processFile(filename):
    lines = []
    with open("{}/{}".format(dir_path, filename), encoding="utf8") as f:
        contents = f.read()
        lines = contents.split("\n")
        lines = list(filter(lambda line: not line.startswith("import LeetCode from \"@/components/LeetCode\";"), lines))
        lines = list(filter(lambda line: not line.startswith("import TeX from '@matejmazur/react-katex';"), lines))
        lines = list(filter(lambda line: not line.startswith("<LeetCode.ProblemCard id={"), lines))
        lines = list(map(lambda line: line.strip(), lines))
        in_larger_sign = False
        new_lines = []
        for line in lines:
            if len(line) > 0 and line[0] == ">":
                in_larger_sign = True
            if len(line) > 0 and line[0] == "#":
                new_lines.append("\n")
                in_larger_sign = False
            if in_larger_sign and len(line) == 0:
                continue
            new_lines.append(line)
        lines = new_lines
    with open("{}/{}".format(dir_path, filename), 'w', encoding="utf8") as outputf:
        outputf.write("\n".join(lines))

for filename in res:
    # print(filename)
    processFile(filename)
