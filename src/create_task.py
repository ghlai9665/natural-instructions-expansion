import json
from datasets import load_dataset

# get instances
dataset = load_dataset(
    'wiki_auto', 'auto_acl')
Instances = []
for i in range(1000):
    normal_sentence = dataset['full'][i]['normal_sentence']
    simple_sentence = dataset['full'][i]['simple_sentence']
    Instances.append({
        'input': normal_sentence,
        'output': [simple_sentence]
    })

# write the rest of the json
task_json = {
    "Contributors": ["Gary Haizhi Lai"],
    "Source": ["wiki_auto"],
    "Categories": ["Style Transfer"],
    "Definition": "In this task, we ask you to rewrite the sentence in simple English without changing its meaning",
    "Positive Examples": [
        {
            "input": "In early work , Rutherford discovered the concept of radioactive half-life, the radioactive element radon, and classified three types of radiations: alpha, beta and gamma radiation .\n",
            "output": "Rutherford discovered the radioactive half-life, the chemical element radon, and the three parts of radiation which he named Alpha , Beta , and Gamma .\n",
            "explanation": "The output sentence is a simplified version of the input sentence."
        },
        {
            "input": "The Inheritance Cycle is a tetralogy of young adult high fantasy novels written by American author Christopher Paolini.",
            "output": "The Inheritance Cycle is a series of fantasy books written by Christopher Paolini.",
            "explanation": "The output sentence is a bit more general and uses simpler words. It is easier to read than the input sentence."
        }
    ],
    "Negative Examples": [{"input": "Boryla was not in the 1952 playoffs.", "output": "Boryla did not participate in the 1952 playoffs.",  "explanation": "The output sentence uses more complex words than the input sentence. It is the opposite of what we want."},
                          {"input": "The population in China increased to around 2,000 in 2005.",
                           "output": "By 2005, the population decreased to about 2,000.",
                           "explanation": "The output sentence changed the meaning of the input sentence."
                           }
                          ],
    "Instances": Instances
}

# export
with open('mytask.json', 'w') as fp:
    final_json = json.dumps(task_json, indent=4, ensure_ascii=False)
    print(final_json, file=fp)
