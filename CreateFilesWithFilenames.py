contents = ['print', 'console.log()']
filenames = ['Python.py', 'Javascript.js']

# for i, item in enumerate(content):
#     with open(f'files/{filename[i]}', 'w') as file:
#         file.writelines(item)

for content, filename in zip(contents, filenames):
    with open(f'files/{filename}', 'w') as file:
        file.writelines(content)
