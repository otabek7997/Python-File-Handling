def file_reader(file_path: str) -> str:
    f = open(file_path)
    content = f.read()
    f.close()
    return content

def data_writer(file_path: str, data: str):
    f = open(file_path,'w')
    f.write(data)
    f.close()


file_path = 'Input/numbers.txt'
content = file_reader(file_path)

file_path = 'Output/output01.txt'
data = ', '.join(content.split())
data_writer(file_path, data)