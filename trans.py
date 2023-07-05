import json

input_file = 'testable_samples.jsonl'
output_file = 'python_code.py'

with open(input_file, 'r') as jonsl, open(output_file, 'w') as tran:
    for line in jonsl:
        json_obj = json.loads(line)
        id = json_obj["id"]
        python_code = json_obj["python"]
        tran.write(id + ' | ' + python_code + '\n\n')