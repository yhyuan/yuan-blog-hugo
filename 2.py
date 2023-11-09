import os
dir_path = r'content/posts/leetcode'
# json_path = r'src/components/LeetCode/data.json';
res = []
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)
res = list(filter(lambda filename: filename[-3:] == ".md", res))
res = list(map(lambda filename: filename.split("_"), res))
res = list(filter(lambda items: len(items) >= 3, res))
res = list(map(lambda items: int(items[1]), res))
res = list(filter(lambda id: id > 0 and id < 9000, res))
ids = set(res)

print(len(ids))

start = '''
<svg width="800" height="400" xmlns="http://www.w3.org/2000/svg">
  <!-- Create a 10x10 grid -->
  <g stroke="#ccc" stroke-width="1">
    <!-- Rows -->
'''
rows = "\n".join(list(map(lambda y: '    <line x1="0" y1="{}" x2="800" y2="{}"/>'.format(y, y), range(0, 401, 10)))) + "\n"
columns = "\n".join(list(map(lambda x: '    <line x1="{}" y1="0" x2="{}" y2="800"/>'.format(x, x), range(0, 801, 10)))) + "\n"
end = '''  </g>
'''
rects = "" 
for j in range(0, 401, 10):
    for i in range(0, 801, 10):
        index = i * 80 + j
        color = "#00ff00" if (index + 1) in ids else "#ffff00"
        rects += '<rect x="{}" y="{}" width="10" height="10" fill="{}" />'.format(j, i, color)

'''</svg>'''

with open("static/img/leetcode.svg", 'w', encoding="utf8") as outputf:
    outputf.write(start + rows + columns + end + rects + '''</svg>''' )
